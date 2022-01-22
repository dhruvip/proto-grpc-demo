from concurrent import futures
import grpc
from hello_pb2_grpc import HelloServiceServicer, add_HelloServiceServicer_to_server
from hello_pb2 import HelloResponse 
import google.protobuf.empty_pb2 as empty_pb2
class handler(HelloServiceServicer):
    def SayHello(self, request, context):
        return HelloResponse(resp_message=f"Helllos {request.name}")
    
    def SayStrictHello(self, request, context):
        if len(request.name) > 10:
            err_msg = 'Name cannot be more than 10 characters'
            context.set_details(err_msg)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return HelloResponse()
        else:
            return HelloResponse(resp_message=f"Helllos {request.name}")

    def Ping(self, request,context):
        print('Hellow therer; yes we are active')
        return empty_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_HelloServiceServicer_to_server(handler(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            pass
    except KeyboardInterrupt as k:
        print('server stopped')
        server.stop(0)

if __name__ == "__main__":
    serve()