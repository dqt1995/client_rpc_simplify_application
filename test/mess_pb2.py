# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test/mess.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test/mess.proto',
  package='mess',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0ftest/mess.proto\x12\x04mess\"W\n\x07\x41uthReq\x12\x18\n\x10workspace_domain\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x11\n\tauth_type\x18\x04 \x01(\x03\x62\x06proto3'
)




_AUTHREQ = _descriptor.Descriptor(
  name='AuthReq',
  full_name='mess.AuthReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspace_domain', full_name='mess.AuthReq.workspace_domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='mess.AuthReq.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='mess.AuthReq.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth_type', full_name='mess.AuthReq.auth_type', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=25,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['AuthReq'] = _AUTHREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthReq = _reflection.GeneratedProtocolMessageType('AuthReq', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQ,
  '__module__' : 'test.mess_pb2'
  # @@protoc_insertion_point(class_scope:mess.AuthReq)
  })
_sym_db.RegisterMessage(AuthReq)


# @@protoc_insertion_point(module_scope)
