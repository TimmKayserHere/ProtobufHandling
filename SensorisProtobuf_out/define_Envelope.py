import sys
import uuid
import time

# first of all, we import some basic compiled protobufs
from sensoris.protobuf.types import base_pb2
from sensoris.protobuf.types import source_pb2
from sensoris.protobuf.types import spatial_pb2
from sensoris.protobuf.messages import data_pb2
from sensoris.protobuf.categories import localization_pb2

def defineSENSORISEnvelope():

    # the Envelope consists for three elements
    # #1 (identifiers)
    # #2 (adapted factor)
    # #3 (vehicle dimensions)

    # generating a local container for the content
    localEnvelope = data_pb2.DataMessage.Envelope()
    localIdentifyer = base_pb2.MessageEnvelopeIds()
    localVehicleDimensions = spatial_pb2.BoundingBox.Metric()

    # filling the identifiers with life
    localIdentifyer.session_id.value = str(uuid.uuid4())
    # why is the message_id a number, but the rest a string?
    localIdentifyer.message_id.value = 123 
    localIdentifyer.vehicle_fleet_id.value = str(uuid.uuid4())
    localIdentifyer.vehicle_id.value = str(uuid.uuid4())
    localIdentifyer.driver_id.value = str(uuid.uuid4())


    # 2.1 defining the minimum vehicle dimensions
    # this is practially a bounding box around the vehicle
    localminposition = spatial_pb2.Position.Metric()

    # as an example, we take the values of an Audi A8 from year 2017
    # length:   5135mm    (maximum: 5265mm)
    # width:    1945mm     (maximum: 1949mm)
    # height:   1460mm    (maximum: 1473mm)
    localminposition.x_m.value = 5135
    localminposition.y_m.value = 1945
    localminposition.z_m.value = 1460

    # 2.1 defining the minimum vehicle dimensions
    # this is practially a bounding box around the vehicle
    localmaxposition = spatial_pb2.Position.Metric()
    localmaxposition.x_m.value = 5265
    localmaxposition.y_m.value = 1949
    localmaxposition.z_m.value = 1473

    localVehicleDimensions.min_position.CopyFrom(localminposition)
    localVehicleDimensions.max_position.CopyFrom(localmaxposition)

    localMessageFactor = data_pb2.DataMessage.Envelope.Factor()
    # localMessageFactor.field_mask = 1
    localMessageFactor.factor = 5
    # scale factor 3 means, that you interpret all values in "meter" as "millimeter"
    # example: vehicle width=2,5135m is represented as width 2513

    # putting it all together
    localEnvelope.adapted_factor.extend([localMessageFactor])
    localEnvelope.ids.CopyFrom(localIdentifyer)
    localEnvelope.vehicle_dimensions.CopyFrom(localVehicleDimensions)
    
    return localEnvelope