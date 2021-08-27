# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mantik/mnp/mnp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mantik/mnp/mnp.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\026ai.mantik.mnp.protocolZ\nmantik/mnp',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14mantik/mnp/mnp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19google/protobuf/any.proto\"\x0e\n\x0c\x41\x62outRequest\"B\n\rAboutResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05\x65xtra\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\x9a\x01\n\x0bInitRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12+\n\rconfiguration\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12#\n\x06inputs\x18\x03 \x03(\x0b\x32\x13.ConfigureInputPort\x12%\n\x07outputs\x18\x04 \x03(\x0b\x32\x14.ConfigureOutputPort\"*\n\x12\x43onfigureInputPort\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\"D\n\x13\x43onfigureOutputPort\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65stination_url\x18\x02 \x01(\t\";\n\x0cInitResponse\x12\x1c\n\x05state\x18\x01 \x01(\x0e\x32\r.SessionState\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\r\n\x0bQuitRequest\"\x0e\n\x0cQuitResponse\"(\n\x12QuitSessionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\x15\n\x13QuitSessionResponse\"o\n\x0bPushRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x11\n\tdata_size\x18\x04 \x01(\x03\x12\x0c\n\x04\x64one\x18\x05 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\"\x0e\n\x0cPushResponse\"@\n\x0bPullRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"8\n\x0cPullResponse\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"G\n\x10QueryTaskRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0e\n\x06\x65nsure\x18\x03 \x01(\x08\"N\n\x0eTaskPortStatus\x12\x11\n\tmsg_count\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x03\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0c\n\x04\x64one\x18\x04 \x01(\x08\"\x80\x01\n\x11QueryTaskResponse\x12\x19\n\x05state\x18\x01 \x01(\x0e\x32\n.TaskState\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x1f\n\x06inputs\x18\x03 \x03(\x0b\x32\x0f.TaskPortStatus\x12 \n\x07outputs\x18\x04 \x03(\x0b\x32\x0f.TaskPortStatus*h\n\x0cSessionState\x12\x13\n\x0fSS_INITIALIZING\x10\x00\x12\x12\n\x0eSS_DOWNLOADING\x10\x01\x12\x12\n\x0eSS_STARTING_UP\x10\x02\x12\x0c\n\x08SS_READY\x10\x03\x12\r\n\tSS_FAILED\x10\x04*J\n\tTaskState\x12\x0e\n\nTS_UNKNOWN\x10\x00\x12\r\n\tTS_EXISTS\x10\x01\x12\x0f\n\x0bTS_FINISHED\x10\x02\x12\r\n\tTS_FAILED\x10\x03\x32\xd1\x02\n\nMnpService\x12\x31\n\x05\x41\x62out\x12\x16.google.protobuf.Empty\x1a\x0e.AboutResponse\"\x00\x12\'\n\x04Init\x12\x0c.InitRequest\x1a\r.InitResponse\"\x00\x30\x01\x12%\n\x04Quit\x12\x0c.QuitRequest\x1a\r.QuitResponse\"\x00\x12\x38\n\x0bQuitSession\x12\x13.QuitSessionRequest\x1a\x14.QuitSessionResponse\x12\'\n\x04Push\x12\x0c.PushRequest\x1a\r.PushResponse\"\x00(\x01\x12\'\n\x04Pull\x12\x0c.PullRequest\x1a\r.PullResponse\"\x00\x30\x01\x12\x34\n\tQueryTask\x12\x11.QueryTaskRequest\x1a\x12.QueryTaskResponse\"\x00\x42$\n\x16\x61i.mantik.mnp.protocolZ\nmantik/mnpb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_SESSIONSTATE = _descriptor.EnumDescriptor(
  name='SessionState',
  full_name='SessionState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SS_INITIALIZING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SS_DOWNLOADING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SS_STARTING_UP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SS_READY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SS_FAILED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1129,
  serialized_end=1233,
)
_sym_db.RegisterEnumDescriptor(_SESSIONSTATE)

SessionState = enum_type_wrapper.EnumTypeWrapper(_SESSIONSTATE)
_TASKSTATE = _descriptor.EnumDescriptor(
  name='TaskState',
  full_name='TaskState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TS_EXISTS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TS_FINISHED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TS_FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1235,
  serialized_end=1309,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE)

TaskState = enum_type_wrapper.EnumTypeWrapper(_TASKSTATE)
SS_INITIALIZING = 0
SS_DOWNLOADING = 1
SS_STARTING_UP = 2
SS_READY = 3
SS_FAILED = 4
TS_UNKNOWN = 0
TS_EXISTS = 1
TS_FINISHED = 2
TS_FAILED = 3



_ABOUTREQUEST = _descriptor.Descriptor(
  name='AboutRequest',
  full_name='AboutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=94,
)


_ABOUTRESPONSE = _descriptor.Descriptor(
  name='AboutResponse',
  full_name='AboutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='AboutResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra', full_name='AboutResponse.extra', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=162,
)


_INITREQUEST = _descriptor.Descriptor(
  name='InitRequest',
  full_name='InitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='InitRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='InitRequest.configuration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='InitRequest.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='InitRequest.outputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=319,
)


_CONFIGUREINPUTPORT = _descriptor.Descriptor(
  name='ConfigureInputPort',
  full_name='ConfigureInputPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='ConfigureInputPort.content_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=363,
)


_CONFIGUREOUTPUTPORT = _descriptor.Descriptor(
  name='ConfigureOutputPort',
  full_name='ConfigureOutputPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='ConfigureOutputPort.content_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_url', full_name='ConfigureOutputPort.destination_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=433,
)


_INITRESPONSE = _descriptor.Descriptor(
  name='InitResponse',
  full_name='InitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='InitResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='InitResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=494,
)


_QUITREQUEST = _descriptor.Descriptor(
  name='QuitRequest',
  full_name='QuitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=509,
)


_QUITRESPONSE = _descriptor.Descriptor(
  name='QuitResponse',
  full_name='QuitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=525,
)


_QUITSESSIONREQUEST = _descriptor.Descriptor(
  name='QuitSessionRequest',
  full_name='QuitSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='QuitSessionRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=567,
)


_QUITSESSIONRESPONSE = _descriptor.Descriptor(
  name='QuitSessionResponse',
  full_name='QuitSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=590,
)


_PUSHREQUEST = _descriptor.Descriptor(
  name='PushRequest',
  full_name='PushRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PushRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='PushRequest.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='PushRequest.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_size', full_name='PushRequest.data_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done', full_name='PushRequest.done', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='PushRequest.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=703,
)


_PUSHRESPONSE = _descriptor.Descriptor(
  name='PushResponse',
  full_name='PushResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=719,
)


_PULLREQUEST = _descriptor.Descriptor(
  name='PullRequest',
  full_name='PullRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PullRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='PullRequest.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='PullRequest.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=785,
)


_PULLRESPONSE = _descriptor.Descriptor(
  name='PullResponse',
  full_name='PullResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='PullResponse.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done', full_name='PullResponse.done', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='PullResponse.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=843,
)


_QUERYTASKREQUEST = _descriptor.Descriptor(
  name='QueryTaskRequest',
  full_name='QueryTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='QueryTaskRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='QueryTaskRequest.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ensure', full_name='QueryTaskRequest.ensure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=916,
)


_TASKPORTSTATUS = _descriptor.Descriptor(
  name='TaskPortStatus',
  full_name='TaskPortStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_count', full_name='TaskPortStatus.msg_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='TaskPortStatus.data', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='TaskPortStatus.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done', full_name='TaskPortStatus.done', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=918,
  serialized_end=996,
)


_QUERYTASKRESPONSE = _descriptor.Descriptor(
  name='QueryTaskResponse',
  full_name='QueryTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='QueryTaskResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='QueryTaskResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='QueryTaskResponse.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='QueryTaskResponse.outputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=999,
  serialized_end=1127,
)

_ABOUTRESPONSE.fields_by_name['extra'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_INITREQUEST.fields_by_name['configuration'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_INITREQUEST.fields_by_name['inputs'].message_type = _CONFIGUREINPUTPORT
_INITREQUEST.fields_by_name['outputs'].message_type = _CONFIGUREOUTPUTPORT
_INITRESPONSE.fields_by_name['state'].enum_type = _SESSIONSTATE
_QUERYTASKRESPONSE.fields_by_name['state'].enum_type = _TASKSTATE
_QUERYTASKRESPONSE.fields_by_name['inputs'].message_type = _TASKPORTSTATUS
_QUERYTASKRESPONSE.fields_by_name['outputs'].message_type = _TASKPORTSTATUS
DESCRIPTOR.message_types_by_name['AboutRequest'] = _ABOUTREQUEST
DESCRIPTOR.message_types_by_name['AboutResponse'] = _ABOUTRESPONSE
DESCRIPTOR.message_types_by_name['InitRequest'] = _INITREQUEST
DESCRIPTOR.message_types_by_name['ConfigureInputPort'] = _CONFIGUREINPUTPORT
DESCRIPTOR.message_types_by_name['ConfigureOutputPort'] = _CONFIGUREOUTPUTPORT
DESCRIPTOR.message_types_by_name['InitResponse'] = _INITRESPONSE
DESCRIPTOR.message_types_by_name['QuitRequest'] = _QUITREQUEST
DESCRIPTOR.message_types_by_name['QuitResponse'] = _QUITRESPONSE
DESCRIPTOR.message_types_by_name['QuitSessionRequest'] = _QUITSESSIONREQUEST
DESCRIPTOR.message_types_by_name['QuitSessionResponse'] = _QUITSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['PushRequest'] = _PUSHREQUEST
DESCRIPTOR.message_types_by_name['PushResponse'] = _PUSHRESPONSE
DESCRIPTOR.message_types_by_name['PullRequest'] = _PULLREQUEST
DESCRIPTOR.message_types_by_name['PullResponse'] = _PULLRESPONSE
DESCRIPTOR.message_types_by_name['QueryTaskRequest'] = _QUERYTASKREQUEST
DESCRIPTOR.message_types_by_name['TaskPortStatus'] = _TASKPORTSTATUS
DESCRIPTOR.message_types_by_name['QueryTaskResponse'] = _QUERYTASKRESPONSE
DESCRIPTOR.enum_types_by_name['SessionState'] = _SESSIONSTATE
DESCRIPTOR.enum_types_by_name['TaskState'] = _TASKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AboutRequest = _reflection.GeneratedProtocolMessageType('AboutRequest', (_message.Message,), {
  'DESCRIPTOR' : _ABOUTREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:AboutRequest)
  })
_sym_db.RegisterMessage(AboutRequest)

AboutResponse = _reflection.GeneratedProtocolMessageType('AboutResponse', (_message.Message,), {
  'DESCRIPTOR' : _ABOUTRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:AboutResponse)
  })
_sym_db.RegisterMessage(AboutResponse)

InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:InitRequest)
  })
_sym_db.RegisterMessage(InitRequest)

ConfigureInputPort = _reflection.GeneratedProtocolMessageType('ConfigureInputPort', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGUREINPUTPORT,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:ConfigureInputPort)
  })
_sym_db.RegisterMessage(ConfigureInputPort)

ConfigureOutputPort = _reflection.GeneratedProtocolMessageType('ConfigureOutputPort', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGUREOUTPUTPORT,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:ConfigureOutputPort)
  })
_sym_db.RegisterMessage(ConfigureOutputPort)

InitResponse = _reflection.GeneratedProtocolMessageType('InitResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:InitResponse)
  })
_sym_db.RegisterMessage(InitResponse)

QuitRequest = _reflection.GeneratedProtocolMessageType('QuitRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUITREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:QuitRequest)
  })
_sym_db.RegisterMessage(QuitRequest)

QuitResponse = _reflection.GeneratedProtocolMessageType('QuitResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUITRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:QuitResponse)
  })
_sym_db.RegisterMessage(QuitResponse)

QuitSessionRequest = _reflection.GeneratedProtocolMessageType('QuitSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUITSESSIONREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:QuitSessionRequest)
  })
_sym_db.RegisterMessage(QuitSessionRequest)

QuitSessionResponse = _reflection.GeneratedProtocolMessageType('QuitSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUITSESSIONRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:QuitSessionResponse)
  })
_sym_db.RegisterMessage(QuitSessionResponse)

PushRequest = _reflection.GeneratedProtocolMessageType('PushRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUSHREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:PushRequest)
  })
_sym_db.RegisterMessage(PushRequest)

PushResponse = _reflection.GeneratedProtocolMessageType('PushResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUSHRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:PushResponse)
  })
_sym_db.RegisterMessage(PushResponse)

PullRequest = _reflection.GeneratedProtocolMessageType('PullRequest', (_message.Message,), {
  'DESCRIPTOR' : _PULLREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:PullRequest)
  })
_sym_db.RegisterMessage(PullRequest)

PullResponse = _reflection.GeneratedProtocolMessageType('PullResponse', (_message.Message,), {
  'DESCRIPTOR' : _PULLRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:PullResponse)
  })
_sym_db.RegisterMessage(PullResponse)

QueryTaskRequest = _reflection.GeneratedProtocolMessageType('QueryTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTASKREQUEST,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:QueryTaskRequest)
  })
_sym_db.RegisterMessage(QueryTaskRequest)

TaskPortStatus = _reflection.GeneratedProtocolMessageType('TaskPortStatus', (_message.Message,), {
  'DESCRIPTOR' : _TASKPORTSTATUS,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:TaskPortStatus)
  })
_sym_db.RegisterMessage(TaskPortStatus)

QueryTaskResponse = _reflection.GeneratedProtocolMessageType('QueryTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTASKRESPONSE,
  '__module__' : 'mantik.mnp.mnp_pb2'
  # @@protoc_insertion_point(class_scope:QueryTaskResponse)
  })
_sym_db.RegisterMessage(QueryTaskResponse)


DESCRIPTOR._options = None

_MNPSERVICE = _descriptor.ServiceDescriptor(
  name='MnpService',
  full_name='MnpService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1312,
  serialized_end=1649,
  methods=[
  _descriptor.MethodDescriptor(
    name='About',
    full_name='MnpService.About',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ABOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Init',
    full_name='MnpService.Init',
    index=1,
    containing_service=None,
    input_type=_INITREQUEST,
    output_type=_INITRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Quit',
    full_name='MnpService.Quit',
    index=2,
    containing_service=None,
    input_type=_QUITREQUEST,
    output_type=_QUITRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QuitSession',
    full_name='MnpService.QuitSession',
    index=3,
    containing_service=None,
    input_type=_QUITSESSIONREQUEST,
    output_type=_QUITSESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Push',
    full_name='MnpService.Push',
    index=4,
    containing_service=None,
    input_type=_PUSHREQUEST,
    output_type=_PUSHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Pull',
    full_name='MnpService.Pull',
    index=5,
    containing_service=None,
    input_type=_PULLREQUEST,
    output_type=_PULLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryTask',
    full_name='MnpService.QueryTask',
    index=6,
    containing_service=None,
    input_type=_QUERYTASKREQUEST,
    output_type=_QUERYTASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MNPSERVICE)

DESCRIPTOR.services_by_name['MnpService'] = _MNPSERVICE

# @@protoc_insertion_point(module_scope)