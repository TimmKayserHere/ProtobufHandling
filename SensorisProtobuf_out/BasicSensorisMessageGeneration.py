import sys
import os
import zipfile
import uuid
import time

# first of all, we import some basic compiled protobufs
from sensoris.protobuf.types import base_pb2
from sensoris.protobuf.types import source_pb2
from sensoris.protobuf.types import spatial_pb2
from sensoris.protobuf.messages import data_pb2
from sensoris.protobuf.categories import localization_pb2

import define_Version
import define_Submitter
import define_DataMessage

# The SENSORIS-Message basically consists of 3 elements
# #1 version
# #2 submitter
# #3 data message
#
# These three elements will be generated here
# Please go deeper into the python files to see, how these elements are internally generated

# this is the SENSORIS message itself
mySensorisMessage = data_pb2.DataMessages()

# Filling #1 (version)
mySensorisMessage.version.CopyFrom(define_Version.DefineSENSORISVersion(4,5,6,"SENSORIS Test Version"))

# Filling #2 (submitter)
mySensorisMessage.submitter.extend([define_Submitter.DefineSENSORISSubmitter("Audi", "A8", "3.0", "B-Sample")])

# Filling #3 (data message)
mySensorisMessage.data_message.extend([define_DataMessage.DefineSENSORISDataMessage()])

print mySensorisMessage.__unicode__()


# writes the protobuf stream on a binary file on disk
with open('generatedSENSORISmessage.bin', 'wb') as f:
    f.write(mySensorisMessage.SerializeToString())

# display the size of the written file
statinfo = os.stat('generatedSENSORISmessage.bin')
print "Size of written SENSORIS protobuf message is " + str(statinfo.st_size) + " Bytes"

# here we check, if we can read the just dumped data
mySENSORISmessage_rewrite = data_pb2.DataMessages()
with open('generatedSENSORISmessage.bin', 'rb') as f:
    mySENSORISmessage_rewrite.ParseFromString(f.read())

# now we take the binary file from the disk an zip it
output_message_zip = zipfile.ZipFile('generatedSENSORISmessage.zip', 'w')
output_message_zip.write('generatedSENSORISmessage.bin', compress_type=zipfile.ZIP_DEFLATED)
output_message_zip.close()

# display the size of the compressed written file
statinfo = os.stat('generatedSENSORISmessage.zip')
print "Size of written SENSORIS protobuf message is " + str(statinfo.st_size) + " Bytes (compressed via zip)"
