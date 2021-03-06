# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/int.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/int.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1aproto/lib/python/int.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"6\n\x03Int\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x03\x12!\n\x02id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_INT = _descriptor.Descriptor(
    name="Int",
    full_name="syft.lib.python.Int",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="syft.lib.python.Int.data",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.Int.id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=86,
    serialized_end=140,
)

_INT.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["Int"] = _INT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Int = _reflection.GeneratedProtocolMessageType(
    "Int",
    (_message.Message,),
    {
        "DESCRIPTOR": _INT,
        "__module__": "proto.lib.python.int_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.Int)
    },
)
_sym_db.RegisterMessage(Int)


# @@protoc_insertion_point(module_scope)
