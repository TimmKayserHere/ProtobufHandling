import sys
import uuid
import time

# first of all, we import some basic compiled protobufs
from sensoris.protobuf.types import base_pb2
from sensoris.protobuf.types import source_pb2
from sensoris.protobuf.types import spatial_pb2
from sensoris.protobuf.messages import data_pb2
from sensoris.protobuf.categories import localization_pb2


def defineSENSORISEventGroup():

    # the event group consists of
    # #1 (origin)
    # #2 (localization category)
    # both is being defined here

    # generating the local container for the content
    localEventGroup = data_pb2.EventGroup()

    # putting it together
    localEventGroup.origin.CopyFrom(defineOrigin())
    localEventGroup.localization_category.CopyFrom(defineLocalizationCategory())

    return localEventGroup

def defineOrigin():
    # The Origin consists of 4 elements
    # #1.1 timestamp
    # #1.2 absolute spatial reference system
    # #1.3 position
    # #1.4 orientation
    # All these elements are filled here with life
    localOrigin = data_pb2.EventGroup.Origin()

    # hand over the information from sub-functions
    localOrigin.timestamp.CopyFrom(defineTimestamp())
    localOrigin.absolute_spatial_reference_system.CopyFrom(defineAbsoluteSpatialReferenceSystem())
    localOrigin.position.CopyFrom(definePosition("geometric", "ad"))
    localOrigin.orientation.CopyFrom(defineRotation("euler", "ad"))
    return localOrigin

def defineLocalizationCategory():

    # the localization category consists of mainly 3 items
    # #1 (vehicle position and orientation)
    # #2 (vehicle odometry)
    # #3 (vehicle dynamics)
    # all elements are defined as "repeated", that means, you can link multiple of them together   
    localLocalizationCategory = localization_pb2.LocalizationCategory()

    # START TO WORK HERE!
    # hand over the information from sub-functions
    localLocalizationCategory.vehicle_position_and_orientation.extend([defineVehiclePositionAndOrientation()])
    localLocalizationCategory.vehicle_odometry.extend([defineVehicleOdometry()])
    localLocalizationCategory.vehicle_dynamics.extend([defineVehicleDynamics()])

    return localLocalizationCategory

def defineVehiclePositionAndOrientation():
    localVehiclePositionAndOrientation = localization_pb2.VehiclePositionAndOrientation()
    return localVehiclePositionAndOrientation

def defineVehicleOdometry():
    localVehicleOdometry = localization_pb2.VehicleOdometry()
    return localVehicleOdometry

def defineVehicleDynamics():
    localVehicleDynamics = localization_pb2.VehicleDynamics()
    return localVehicleDynamics


def defineTimestamp():
    localTimestamp = base_pb2.Timestamp()
    getMilliseconds = int(round(time.time() * 1000))
    localTimestamp.posix_time_ms.value = getMilliseconds
    localTimestamp.posix_time_micro_s_fraction.value = 678 # QUESTION: HOW?
    return localTimestamp

def defineAbsoluteSpatialReferenceSystem():
    localAbsoluteSpatialReferenceSystem = spatial_pb2.SpatialReferenceSystem.Absolute()

    # #1.2 (absolute spatial reference system)
    localAbsoluteSpatialReferenceSystem = spatial_pb2.SpatialReferenceSystem.Absolute()
    # be sure, the oneOf will make it possible to only define one or the other system. Its not possible to define multiple of them.spatial_pb2
    # Option 1 (going for WGS_84 or another standard)
    localEpsgCodeSystem = spatial_pb2.SpatialReferenceSystem.Absolute.EpsgCodeSystem()
    localEpsgCodeSystem.code_suffix.value = spatial_pb2.SpatialReferenceSystem.Absolute.EpsgCodeSystem.WGS_84
    localAbsoluteSpatialReferenceSystem.epsg_code_system.CopyFrom(localEpsgCodeSystem)

    # Option 2 (being fully free and simply define a text for the reference system of your joice)
    localWellKnownTextSystem = spatial_pb2.SpatialReferenceSystem.Absolute.WellKnownTextSystem()
    localWellKnownTextSystem.wkt.value = "Well Known Text Definition"
    # localAbsoluteSpatialReferenceSystem.wkt_definition.CopyFrom(localWellKnownTextSystem)

    return localAbsoluteSpatialReferenceSystem

def definePosition(positiontype, accuracyType):
    localPosition = spatial_pb2.Position()

    # The position message consists mainly of 2 elements
    # #1 general type of position (geographic or metric)
    # #2 accuracy
    # both elements are being defined here
    # keep in mind, that this position is the reference point for relative meassurements of objects etc. later on

    # #1
    localGeograhicPosition = spatial_pb2.Position.Geographic()
    localMetricPosition = spatial_pb2.Position.Metric()

    # QUESTION: Wie loesen wir hier Kommawerte auf?
    localGeograhicPosition.longitude_deg.value = 1111111
    localGeograhicPosition.latitude_deg.value = 2222222
    localGeograhicPosition.altitude_m.value = 100

    localMetricPosition.x_m.value = 10
    localMetricPosition.y_m.value = 20
    localMetricPosition.z_m.value = 30

    if positiontype == "geometric":
        localPosition.geographic.CopyFrom(localGeograhicPosition)
        pass

    if positiontype == "metric":
        localPosition.metric.CopyFrom(localMetricPosition)
        pass

    # the position message comes with multiple accuracies
    # these are all "one of", so, you will have to decide
    # accuracy options are
    # #1 (combined horizontal and vertical)
    # #2 (horizontal and vertical)
    # #3 (horizontal confidence ellipse and vertical accuracy)
    # #4 (covariance matrix)
    # #5 (SD1 accuracy)
    # #6 (SD2 accuracy)
    # #7 (HD accuracy)
    # #8 (AD accuracy)

    # #1
    localCombinedHorizontalAndVerticalAccuracy = spatial_pb2.Position.CombinedHorizontalVerticalAccuracy()
    localCombinedHorizontalAndVerticalAccuracy.horizontal_vertical_m.value = 5 #representing 5m accuracy in both dimensions

    # #2
    localHorizontalAndVerticalAccuracy = spatial_pb2.Position.HorizontalVerticalAccuracy()
    localHorizontalAndVerticalAccuracy.horizontal_m.value = 3 # representing 3m in horizontal direction QUESTION: WHAT IS HORIZONTAL?
    localHorizontalAndVerticalAccuracy.vertical_m.value = 10

    # #3
    localHorizontalConfidenceEllipseVerticalAccuracy = spatial_pb2.Position.HorizontalConfidenceEllipseVerticalAccuracy()
    localHorizontalConfidenceEllipseVerticalAccuracy.horizontal_ellipse_major_m.value = 5
    localHorizontalConfidenceEllipseVerticalAccuracy.horizontal_ellipse_minor_m.value = 3
    localHorizontalConfidenceEllipseVerticalAccuracy.horizontal_ellipse_major_heading_deg.value = 10
    localHorizontalConfidenceEllipseVerticalAccuracy.vertical_m.value = 10
    
    # #4
    localCovarianceMatrix = spatial_pb2.Position.CovarianceMatrix()
    localCovarianceMatrix.covariance_m2.a11.value = 1
    localCovarianceMatrix.covariance_m2.a12.value = 2
    localCovarianceMatrix.covariance_m2.a13.value = 3
    localCovarianceMatrix.covariance_m2.a21.value = 4
    localCovarianceMatrix.covariance_m2.a22.value = 5
    localCovarianceMatrix.covariance_m2.a23.value = 6
    localCovarianceMatrix.covariance_m2.a31.value = 7
    localCovarianceMatrix.covariance_m2.a32.value = 8
    localCovarianceMatrix.covariance_m2.a33.value = 9
    # QUESTION: Covariances are usually lower than 1 ... where do I get the scale factor from?

    # #5
    # QUESTION: WHY DO WE NEED THAT? THIS IS SIMILAR TO #1
    localSD1 = spatial_pb2.Position.Sd1Accuracy()
    localSD1.horizontal_and_vertical_m.value = 5

    # #6
    # QUESTION: WHY DO WE NEED THAT THIS IS SIMILAR TO #2
    localSD2 = spatial_pb2.Position.Sd2Accuracy()
    localSD2.horizontal_m.value = 10
    localSD2.vertical_m.value = 10

    # #7 
    # QUESTION: WHY DO WE NEED THAT. THIS IS SIMILAR TO #3
    localHD = spatial_pb2.Position.HdAccuracy()
    localHD.horizontal_ellipse_major_m.value = 7
    localHD.horizontal_ellipse_minor_m.value = 8
    localHD.horizontal_ellipse_major_heading_deg.value = 9
    localHD.vertical_m.value = 10

    # #8
    # QUESTION: WHY DO WE NEED THAT. THIS IS SIMILAR TO #3
    localAD = spatial_pb2.Position.AdAccuracy()
    localAD.inverse_covariance_1_p_m2.a11.value = 1
    localAD.inverse_covariance_1_p_m2.a12.value = 2
    localAD.inverse_covariance_1_p_m2.a13.value = 3
    localAD.inverse_covariance_1_p_m2.a21.value = 4
    localAD.inverse_covariance_1_p_m2.a22.value = 5
    localAD.inverse_covariance_1_p_m2.a23.value = 6
    localAD.inverse_covariance_1_p_m2.a31.value = 7
    localAD.inverse_covariance_1_p_m2.a32.value = 8
    localAD.inverse_covariance_1_p_m2.a33.value = 9

    if accuracyType == "chava":
        localPosition.combined_horizontal_vertical_accuracy.CopyFrom(localCombinedHorizontalAndVerticalAccuracy)
        pass
    if accuracyType == "hav":
        localPosition.horizontal_vertical_accuracy.CopyFrom(localHorizontalAndVerticalAccuracy)
        pass
    if accuracyType == "hcev":
        localPosition.horizontal_confidence_ellipse_vertical_accuracy.CopyFrom(localHorizontalConfidenceEllipseVerticalAccuracy)
        pass

    if accuracyType == "cov":
        localPosition.covariance_matrix.CopyFrom(localCovarianceMatrix)
        pass
    
    if accuracyType == "sd1":
        localPosition.sd1_accuracy.CopyFrom(localSD1)
        pass

    if accuracyType == "sd2":
        localPosition.sd2_accuracy.CopyFrom(localSD2)

    if accuracyType == "hd":
        localPosition.hd_accuracy.CopyFrom(localHD)

    if accuracyType == "ad":
        localPosition.ad_accuracy.CopyFrom(localAD)


    return localPosition

def defineRotation(rotationsystem, accuracy):
    localRotation = spatial_pb2.Rotation()

    # The rotation matrix mainly consists of 2 elements
    # #1 Which Quaternion is used?
    # #2 Accuracy
    # both elements are of type "one of", so there is a clear decision to take here

    # #1
    localEuler = spatial_pb2.Rotation.EulerRotation()
    localEuler.yaw_deg.value = 10
    localEuler.pitch_deg.value = 11
    localEuler.roll_deg.value = 12

    localQuaternion = spatial_pb2.Rotation.QuaternionRotation()
    localQuaternion.x.value = 100
    localQuaternion.y.value = 110
    localQuaternion.z.value = 120

    if rotationsystem == "euler":
        localRotation.euler.CopyFrom(localEuler)
        pass

    if rotationsystem == "quaternion":
        localRotation.quaternion.CopyFrom(localQuaternion)
        pass

    #2
    # there are 6 versions to define the accuracy of rotations
    # #2.1 combined yaw/pitch/roll accuracy
    # #2.2 yaw/pitch/roll accuracy
    # #2.3 covariance matric
    # #2.4 sd accuracy
    # #2.5 hd accuracy
    # #2.6 ad accuracy

    # #2.1
    localCombinedYawPitchRollAccuracy = spatial_pb2.Rotation.CombinedYawPitchRollAccuracy()
    localCombinedYawPitchRollAccuracy.yaw_pitch_roll_deg.value = 10

    # #2.2
    localYawPitchRollAccuracy = spatial_pb2.Rotation.YawPitchRollAccuracy()
    localYawPitchRollAccuracy.yaw_deg.value = 10
    localYawPitchRollAccuracy.pitch_deg.value = 11
    localYawPitchRollAccuracy.roll_deg.value = 12
    
    # #2.3
    localRollCovarianceMatrix = spatial_pb2.Rotation.CovarianceMatrix()
    localRollCovarianceMatrix.covariance_deg2.a11.value = 1
    localRollCovarianceMatrix.covariance_deg2.a12.value = 2
    localRollCovarianceMatrix.covariance_deg2.a13.value = 3
    localRollCovarianceMatrix.covariance_deg2.a21.value = 4
    localRollCovarianceMatrix.covariance_deg2.a22.value = 5
    localRollCovarianceMatrix.covariance_deg2.a23.value = 6
    localRollCovarianceMatrix.covariance_deg2.a31.value = 7
    localRollCovarianceMatrix.covariance_deg2.a32.value = 8
    localRollCovarianceMatrix.covariance_deg2.a33.value = 9

    # #2.4
    # QUESTION: This is a duplicate from #2.1
    localRotationSdAccuracy = spatial_pb2.Rotation.SdAccuracy()
    localRotationSdAccuracy.yaw_pitch_roll_deg.value = 15

    # #2.5
    # QUESTION: This is a dublicate from 2.2
    localRotationHdAccuracy = spatial_pb2.Rotation.HdAccuracy()
    localRotationHdAccuracy.yaw_deg.value = 20
    localRotationHdAccuracy.pitch_deg.value = 21
    localRotationHdAccuracy.roll_deg.value = 22

    # #2.6
    localRotationAdAccuracy = spatial_pb2.Rotation.AdAccuracy()
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a11.value = 1
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a12.value = 2
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a13.value = 3
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a21.value = 4
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a22.value = 5
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a23.value = 6
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a31.value = 7
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a32.value = 8
    localRotationAdAccuracy.inverse_covariance_1_p_deg2.a33.value = 9

    if accuracy == "cypr":
        localRotation.combined_yaw_pitch_roll_accuracy.CopyFrom(localCombinedYawPitchRollAccuracy)
        pass
    if accuracy == "ypr":
        localRotation.yaw_pitch_roll_accuracy.CopyFrom(localYawPitchRollAccuracy)
        pass
    if accuracy == "cov":
        localRotation.covariance_matrix.CopyFrom(localRollCovarianceMatrix)
        pass
    if accuracy == "sd":
        localRotation.sd_accuracy.CopyFrom(localRotationSdAccuracy)
        pass
    if accuracy == "hd":
        localRotation.hd_accuracy.CopyFrom(localRotationHdAccuracy)
        pass
    if accuracy == "ad":
        localRotation.ad_accuracy.CopyFrom(localRotationAdAccuracy)
        pass

    return localRotation