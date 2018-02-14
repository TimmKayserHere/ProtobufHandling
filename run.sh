#!/bin/bash
clear
echo Starting Compilation of the local sample files for protobuf.

echo
echo Used Protobuf Version:
protoc --version
echo
echo Compiling proprietary protobuf ...
protoc -I=. --python_out=./ProprietaryProtobuf_out base.proto
echo Done.
echo -------------------------------
echo Compiling SENSORIS protobuf ...
cd ..
cd specification
echo Compile "data.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/messages/data.proto
echo Done.
echo Compile "base.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/types/base.proto
echo Done.
echo Compile "spatial.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/types/spatial.proto
echo Done.
echo Compile "brake.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/brake.proto
echo Done.
echo Compile "driving_behavior.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/driving_behavior.proto
echo Done.
echo Compile "intersection_attribution.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/intersection_attribution.proto
echo Done.
echo Compile "localization.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/localization.proto
echo Done.
echo Compile "map.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/map.proto
echo Done.
echo Compile "object_detection.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/object_detection.proto
echo Done.
echo Compile "powertrain.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/powertrain.proto
echo Done.
echo Compile "road_attribution.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/road_attribution.proto
echo Done.
echo Compile "traffic_events.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/traffic_events.proto
echo Done.
echo Compile "traffic_maneuver.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/traffic_maneuver.proto
echo Done.
echo Compile "traffic_regulation.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/traffic_regulation.proto
echo Done.
echo Compile "weather.proto"
protoc -I=./src/ --python_out=../ProtobufHandling/SensorisProtobuf_out/ ./src/sensoris/protobuf/categories/weather.proto
echo Done.
echo Successfully compiled all SENSORIS protobuf files
echo --------------------------------------------------