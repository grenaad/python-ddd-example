# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import pos_pb2 as pos__pb2


class POSStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUser = channel.unary_unary(
        '/grpc_pos.POS/CreateUser',
        request_serializer=pos__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=pos__pb2.OKResponse.FromString,
        )
    self.CreateCustomer = channel.unary_unary(
        '/grpc_pos.POS/CreateCustomer',
        request_serializer=pos__pb2.CreateCustomerRequest.SerializeToString,
        response_deserializer=pos__pb2.OKResponse.FromString,
        )
    self.GetCustomer = channel.unary_unary(
        '/grpc_pos.POS/GetCustomer',
        request_serializer=pos__pb2.GetCustomerRequest.SerializeToString,
        response_deserializer=pos__pb2.GetCustomerResponse.FromString,
        )
    self.GetStore = channel.unary_unary(
        '/grpc_pos.POS/GetStore',
        request_serializer=pos__pb2.GetStoreRequest.SerializeToString,
        response_deserializer=pos__pb2.GetStoreResponse.FromString,
        )
    self.GetStores = channel.unary_unary(
        '/grpc_pos.POS/GetStores',
        request_serializer=pos__pb2.GetStoresRequest.SerializeToString,
        response_deserializer=pos__pb2.GetStoresResponse.FromString,
        )
    self.GetCategory = channel.unary_unary(
        '/grpc_pos.POS/GetCategory',
        request_serializer=pos__pb2.GetCategoryRequest.SerializeToString,
        response_deserializer=pos__pb2.GetCategoryResponse.FromString,
        )
    self.CreateOrder = channel.unary_unary(
        '/grpc_pos.POS/CreateOrder',
        request_serializer=pos__pb2.CreateOrderRequest.SerializeToString,
        response_deserializer=pos__pb2.OKResponse.FromString,
        )
    self.CreateCustomerPayment = channel.unary_unary(
        '/grpc_pos.POS/CreateCustomerPayment',
        request_serializer=pos__pb2.CreateCustomerPaymentRequest.SerializeToString,
        response_deserializer=pos__pb2.OKResponse.FromString,
        )


class POSServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateCustomer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCustomer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStores(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCategory(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateCustomerPayment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_POSServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=pos__pb2.CreateUserRequest.FromString,
          response_serializer=pos__pb2.OKResponse.SerializeToString,
      ),
      'CreateCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCustomer,
          request_deserializer=pos__pb2.CreateCustomerRequest.FromString,
          response_serializer=pos__pb2.OKResponse.SerializeToString,
      ),
      'GetCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomer,
          request_deserializer=pos__pb2.GetCustomerRequest.FromString,
          response_serializer=pos__pb2.GetCustomerResponse.SerializeToString,
      ),
      'GetStore': grpc.unary_unary_rpc_method_handler(
          servicer.GetStore,
          request_deserializer=pos__pb2.GetStoreRequest.FromString,
          response_serializer=pos__pb2.GetStoreResponse.SerializeToString,
      ),
      'GetStores': grpc.unary_unary_rpc_method_handler(
          servicer.GetStores,
          request_deserializer=pos__pb2.GetStoresRequest.FromString,
          response_serializer=pos__pb2.GetStoresResponse.SerializeToString,
      ),
      'GetCategory': grpc.unary_unary_rpc_method_handler(
          servicer.GetCategory,
          request_deserializer=pos__pb2.GetCategoryRequest.FromString,
          response_serializer=pos__pb2.GetCategoryResponse.SerializeToString,
      ),
      'CreateOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CreateOrder,
          request_deserializer=pos__pb2.CreateOrderRequest.FromString,
          response_serializer=pos__pb2.OKResponse.SerializeToString,
      ),
      'CreateCustomerPayment': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCustomerPayment,
          request_deserializer=pos__pb2.CreateCustomerPaymentRequest.FromString,
          response_serializer=pos__pb2.OKResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc_pos.POS', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
