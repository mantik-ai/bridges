# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mantik/engine/registry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mantik/engine/registry.proto',
  package='ai.mantik.engine.protos',
  syntax='proto3',
  serialized_options=b'Z\rmantik/engine',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cmantik/engine/registry.proto\x12\x17\x61i.mantik.engine.protos\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd0\x01\n\x0eMantikArtifact\x12\x1a\n\x12mantik_header_json\x18\x01 \x01(\t\x12\x15\n\rartifact_kind\x18\x02 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x03 \x01(\t\x12\x10\n\x08named_id\x18\x04 \x01(\t\x12\x0f\n\x07item_id\x18\x05 \x01(\t\x12@\n\x0f\x64\x65ployment_info\x18\x06 \x01(\x0b\x32\'.ai.mantik.engine.protos.DeploymentInfo\x12\x15\n\rmantik_header\x18\x07 \x01(\t\"\x90\x02\n\x0e\x44\x65ploymentInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cinternal_url\x18\x02 \x01(\t\x12\x14\n\x0c\x65xternal_url\x18\x03 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12=\n\x03sub\x18\x05 \x03(\x0b\x32\x30.ai.mantik.engine.protos.DeploymentInfo.SubEntry\x1aV\n\x08SubEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.ai.mantik.engine.protos.SubDeploymentInfo:\x02\x38\x01\"7\n\x11SubDeploymentInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cinternal_url\x18\x02 \x01(\tB\x0fZ\rmantik/engineb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_MANTIKARTIFACT = _descriptor.Descriptor(
  name='MantikArtifact',
  full_name='ai.mantik.engine.protos.MantikArtifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mantik_header_json', full_name='ai.mantik.engine.protos.MantikArtifact.mantik_header_json', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artifact_kind', full_name='ai.mantik.engine.protos.MantikArtifact.artifact_kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_id', full_name='ai.mantik.engine.protos.MantikArtifact.file_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='named_id', full_name='ai.mantik.engine.protos.MantikArtifact.named_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='ai.mantik.engine.protos.MantikArtifact.item_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deployment_info', full_name='ai.mantik.engine.protos.MantikArtifact.deployment_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mantik_header', full_name='ai.mantik.engine.protos.MantikArtifact.mantik_header', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=299,
)


_DEPLOYMENTINFO_SUBENTRY = _descriptor.Descriptor(
  name='SubEntry',
  full_name='ai.mantik.engine.protos.DeploymentInfo.SubEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ai.mantik.engine.protos.DeploymentInfo.SubEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ai.mantik.engine.protos.DeploymentInfo.SubEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=574,
)

_DEPLOYMENTINFO = _descriptor.Descriptor(
  name='DeploymentInfo',
  full_name='ai.mantik.engine.protos.DeploymentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ai.mantik.engine.protos.DeploymentInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='internal_url', full_name='ai.mantik.engine.protos.DeploymentInfo.internal_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_url', full_name='ai.mantik.engine.protos.DeploymentInfo.external_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ai.mantik.engine.protos.DeploymentInfo.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub', full_name='ai.mantik.engine.protos.DeploymentInfo.sub', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYMENTINFO_SUBENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=574,
)


_SUBDEPLOYMENTINFO = _descriptor.Descriptor(
  name='SubDeploymentInfo',
  full_name='ai.mantik.engine.protos.SubDeploymentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ai.mantik.engine.protos.SubDeploymentInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='internal_url', full_name='ai.mantik.engine.protos.SubDeploymentInfo.internal_url', index=1,
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
  serialized_start=576,
  serialized_end=631,
)

_MANTIKARTIFACT.fields_by_name['deployment_info'].message_type = _DEPLOYMENTINFO
_DEPLOYMENTINFO_SUBENTRY.fields_by_name['value'].message_type = _SUBDEPLOYMENTINFO
_DEPLOYMENTINFO_SUBENTRY.containing_type = _DEPLOYMENTINFO
_DEPLOYMENTINFO.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOYMENTINFO.fields_by_name['sub'].message_type = _DEPLOYMENTINFO_SUBENTRY
DESCRIPTOR.message_types_by_name['MantikArtifact'] = _MANTIKARTIFACT
DESCRIPTOR.message_types_by_name['DeploymentInfo'] = _DEPLOYMENTINFO
DESCRIPTOR.message_types_by_name['SubDeploymentInfo'] = _SUBDEPLOYMENTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MantikArtifact = _reflection.GeneratedProtocolMessageType('MantikArtifact', (_message.Message,), {
  'DESCRIPTOR' : _MANTIKARTIFACT,
  '__module__' : 'mantik.engine.registry_pb2'
  # @@protoc_insertion_point(class_scope:ai.mantik.engine.protos.MantikArtifact)
  })
_sym_db.RegisterMessage(MantikArtifact)

DeploymentInfo = _reflection.GeneratedProtocolMessageType('DeploymentInfo', (_message.Message,), {

  'SubEntry' : _reflection.GeneratedProtocolMessageType('SubEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYMENTINFO_SUBENTRY,
    '__module__' : 'mantik.engine.registry_pb2'
    # @@protoc_insertion_point(class_scope:ai.mantik.engine.protos.DeploymentInfo.SubEntry)
    })
  ,
  'DESCRIPTOR' : _DEPLOYMENTINFO,
  '__module__' : 'mantik.engine.registry_pb2'
  # @@protoc_insertion_point(class_scope:ai.mantik.engine.protos.DeploymentInfo)
  })
_sym_db.RegisterMessage(DeploymentInfo)
_sym_db.RegisterMessage(DeploymentInfo.SubEntry)

SubDeploymentInfo = _reflection.GeneratedProtocolMessageType('SubDeploymentInfo', (_message.Message,), {
  'DESCRIPTOR' : _SUBDEPLOYMENTINFO,
  '__module__' : 'mantik.engine.registry_pb2'
  # @@protoc_insertion_point(class_scope:ai.mantik.engine.protos.SubDeploymentInfo)
  })
_sym_db.RegisterMessage(SubDeploymentInfo)


DESCRIPTOR._options = None
_DEPLOYMENTINFO_SUBENTRY._options = None
# @@protoc_insertion_point(module_scope)