# Exercise: gRPC Demo

**Objective**: Understand Proto files.

## 📝 Steps

1. Install `grpcio-tools`.
2. Create `service.proto`.
3. Define a `Greeter` service with a `SayHello` method.
4. Generate Python code from proto.

```protobuf
syntax = "proto3";

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```
