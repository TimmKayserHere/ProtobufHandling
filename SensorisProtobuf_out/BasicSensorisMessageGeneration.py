import sys

# first of all, we import some basic compiled protobufs
from sensoris.protobuf.types import base_pb2
from sensoris.protobuf.types import source_pb2
from sensoris.protobuf.types import spatial_pb2
from sensoris.protobuf.messages import data_pb2
# from protobuf-3.5.1 import python

print "All imports worked."

# generating the SENSORIS message
# a SENSORIS message at the very top has only 3 major components
# (1) its the SENSORIS-version
# (2) its the information on the Submitter
# (3) its the data message itself, which gives further structure
mySensorisMessage = data_pb2.DataMessages()

############### 1 ###############
# we locally define our own version message and append it to the SENSORIS message
# the way, the version message is valid for non-repeated messages
localVersion = base_pb2.Version()
localVersion.major.value = 1
localVersion.minor.value = 2
localVersion.patch.value = 3
localVersion.name.value = "SENSORIS Test Version"

mySensorisMessage.version.CopyFrom(localVersion)

############### 2 ###############
# we locally define our own submitter message and append it to the SENSORIS message
# the way we do that, is valid for repeated messages
localsubmitter = base_pb2.Submitter()
localsubmitter.name.value = "Audi A8"
localsubmitter.type.value = "Awesome Car"
localsubmitter.software_version.value = "3.0"
localsubmitter.hardware_version.value = "B-sample"

mySensorisMessage.submitter.extend([localsubmitter])

############### 3 ###############
# we locally define our first data message and append it later on to the SENSORIS message
# Envelope (single)
# EventGroup (repeated)
# EventRelation (repeated)
# EventSource (repeated)
localDataMessage = data_pb2.DataMessage()

mySensorisMessage.data_message.extend([localDataMessage])

print mySensorisMessage.__unicode__()
