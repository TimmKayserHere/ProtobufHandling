# ProtobufHandling


from base.proto
protoc -I=. --python_out=../../../../../ProtobufHandling/SensorisProtobuf_out base.proto

from this directory
protoc -I=../specification/src/sensoris/protobuf/types --python_out=./SensorisProtobuf_out base.proto

with absolute paths
protoc -I=/Users/kayser/Documents/SENSORIS/specification/src/sensoris/protobuf/types --python_out=/Users/kayser/Documents/SENSORIS/ProtobufHandling/SensorisProtobuf_out base.proto
