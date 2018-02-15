import sys
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
