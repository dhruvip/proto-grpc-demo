
import grpc
from hello_pb2 import HelloRequest

from hello_pb2_grpc import HelloServiceStub


def call():
    channel = grpc.insecure_channel('localhost:50051')
    stub = HelloServiceStub(channel)
    name = HelloRequest(name='Testing john Doe')
    try:
        # call the rpc function
        response = stub.SayStrictHello(name)
        print(response)
    except grpc.RpcError as e:
        # ouch!
        # lets print the gRPC error message
        # which is "Length of `Name` cannot be more than 10 characters"
        print(e.details())
        # lets access the error code, which is `INVALID_ARGUMENT`
        # `type` of `status_code` is `grpc.StatusCode`
        status_code = e.code()
        # should print `INVALID_ARGUMENT`
        print(status_code.name)
        # should print `(3, 'invalid argument')`
        print(status_code.value)
        # want to do some specific action based on the error?
        if grpc.StatusCode.INVALID_ARGUMENT == status_code:
            # do your stuff here
            pass
    else:
        print(response.Result)



if __name__ == '__main__':
    call()