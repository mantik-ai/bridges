# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import graph_builder_pb2 as mantik_dot_engine_dot_graph__builder__pb2


class GraphBuilderServiceStub(object):
    """Responsible for building up computation graphs. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Get',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.GetRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.AlgorithmApply = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/AlgorithmApply',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.ApplyRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.Train = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Train',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.TrainRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.TrainResponse.FromString,
                )
        self.Literal = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Literal',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.LiteralRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.Cached = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Cached',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.CacheRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.Select = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Select',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.SelectRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.AutoUnion = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/AutoUnion',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.AutoUnionRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.SqlQuery = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/SqlQuery',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.QueryRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.Split = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Split',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.SplitRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.MultiNodeResponse.FromString,
                )
        self.BuildPipeline = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/BuildPipeline',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.BuildPipelineRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.Tag = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/Tag',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.TagRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )
        self.SetMetaVariables = channel.unary_unary(
                '/ai.mantik.engine.protos.GraphBuilderService/SetMetaVariables',
                request_serializer=mantik_dot_engine_dot_graph__builder__pb2.SetMetaVariableRequest.SerializeToString,
                response_deserializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
                )


class GraphBuilderServiceServicer(object):
    """Responsible for building up computation graphs. 
    """

    def Get(self, request, context):
        """* Loads a new node from the repository. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AlgorithmApply(self, request, context):
        """* Applies an algorithm (or pipeline) to a dataset. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Train(self, request, context):
        """* Trains an algorithm with a dataset. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Literal(self, request, context):
        """* Generates a node from a literal. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cached(self, request, context):
        """* Generates a cached copy of an item. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Select(self, request, context):
        """* Run a select query on the dataset item. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AutoUnion(self, request, context):
        """* Run a auto union query on two datasets. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SqlQuery(self, request, context):
        """* Run a SQL Query on datasets. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Split(self, request, context):
        """* Split a DataSet into multiple fractions. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuildPipeline(self, request, context):
        """* Build a pipeline from Algorithms. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Tag(self, request, context):
        """Returns the item using a new name. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMetaVariables(self, request, context):
        """Set Meta Variables of an Item. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GraphBuilderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.GetRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'AlgorithmApply': grpc.unary_unary_rpc_method_handler(
                    servicer.AlgorithmApply,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.ApplyRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'Train': grpc.unary_unary_rpc_method_handler(
                    servicer.Train,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.TrainRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.TrainResponse.SerializeToString,
            ),
            'Literal': grpc.unary_unary_rpc_method_handler(
                    servicer.Literal,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.LiteralRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'Cached': grpc.unary_unary_rpc_method_handler(
                    servicer.Cached,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.CacheRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'Select': grpc.unary_unary_rpc_method_handler(
                    servicer.Select,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.SelectRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'AutoUnion': grpc.unary_unary_rpc_method_handler(
                    servicer.AutoUnion,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.AutoUnionRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'SqlQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.SqlQuery,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.QueryRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'Split': grpc.unary_unary_rpc_method_handler(
                    servicer.Split,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.SplitRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.MultiNodeResponse.SerializeToString,
            ),
            'BuildPipeline': grpc.unary_unary_rpc_method_handler(
                    servicer.BuildPipeline,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.BuildPipelineRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'Tag': grpc.unary_unary_rpc_method_handler(
                    servicer.Tag,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.TagRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
            'SetMetaVariables': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMetaVariables,
                    request_deserializer=mantik_dot_engine_dot_graph__builder__pb2.SetMetaVariableRequest.FromString,
                    response_serializer=mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ai.mantik.engine.protos.GraphBuilderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GraphBuilderService(object):
    """Responsible for building up computation graphs. 
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Get',
            mantik_dot_engine_dot_graph__builder__pb2.GetRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AlgorithmApply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/AlgorithmApply',
            mantik_dot_engine_dot_graph__builder__pb2.ApplyRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Train(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Train',
            mantik_dot_engine_dot_graph__builder__pb2.TrainRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.TrainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Literal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Literal',
            mantik_dot_engine_dot_graph__builder__pb2.LiteralRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cached(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Cached',
            mantik_dot_engine_dot_graph__builder__pb2.CacheRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Select(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Select',
            mantik_dot_engine_dot_graph__builder__pb2.SelectRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AutoUnion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/AutoUnion',
            mantik_dot_engine_dot_graph__builder__pb2.AutoUnionRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SqlQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/SqlQuery',
            mantik_dot_engine_dot_graph__builder__pb2.QueryRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Split(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Split',
            mantik_dot_engine_dot_graph__builder__pb2.SplitRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.MultiNodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuildPipeline(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/BuildPipeline',
            mantik_dot_engine_dot_graph__builder__pb2.BuildPipelineRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Tag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/Tag',
            mantik_dot_engine_dot_graph__builder__pb2.TagRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMetaVariables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.mantik.engine.protos.GraphBuilderService/SetMetaVariables',
            mantik_dot_engine_dot_graph__builder__pb2.SetMetaVariableRequest.SerializeToString,
            mantik_dot_engine_dot_graph__builder__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
