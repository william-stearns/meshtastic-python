# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deviceonly.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2
from . import mesh_pb2 as mesh__pb2
from . import radioconfig_pb2 as radioconfig__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deviceonly.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\nDeviceOnlyH\003Z!github.com/meshtastic/gomeshproto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x64\x65viceonly.proto\x1a\rchannel.proto\x1a\nmesh.proto\x1a\x11radioconfig.proto\"\x80\x01\n\x11LegacyRadioConfig\x12\x39\n\x0bpreferences\x18\x01 \x01(\x0b\x32$.LegacyRadioConfig.LegacyPreferences\x1a\x30\n\x11LegacyPreferences\x12\x1b\n\x06region\x18\x0f \x01(\x0e\x32\x0b.RegionCode\"\xf0\x03\n\x0b\x44\x65viceState\x12\'\n\x0blegacyRadio\x18\x01 \x01(\x0b\x32\x12.LegacyRadioConfig\x12\x1c\n\x07my_node\x18\x02 \x01(\x0b\x32\x0b.MyNodeInfo\x12\x14\n\x05owner\x18\x03 \x01(\x0b\x32\x05.User\x12\x1a\n\x07node_db\x18\x04 \x03(\x0b\x32\t.NodeInfo\x12\"\n\rreceive_queue\x18\x05 \x03(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07version\x18\x08 \x01(\r\x12$\n\x0frx_text_message\x18\x07 \x01(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07no_save\x18\t \x01(\x08\x12\x15\n\rdid_gps_reset\x18\x0b \x01(\x08\x12+\n#canned_message_plugin_message_part1\x18\r \x01(\t\x12+\n#canned_message_plugin_message_part2\x18\x0e \x01(\t\x12+\n#canned_message_plugin_message_part3\x18\x0f \x01(\t\x12+\n#canned_message_plugin_message_part4\x18\x10 \x01(\t\x12+\n#canned_message_plugin_message_part5\x18\x11 \x01(\tJ\x04\x08\x0c\x10\r\")\n\x0b\x43hannelFile\x12\x1a\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x08.ChannelBF\n\x13\x63om.geeksville.meshB\nDeviceOnlyH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
  ,
  dependencies=[channel__pb2.DESCRIPTOR,mesh__pb2.DESCRIPTOR,radioconfig__pb2.DESCRIPTOR,])




_LEGACYRADIOCONFIG_LEGACYPREFERENCES = _descriptor.Descriptor(
  name='LegacyPreferences',
  full_name='LegacyRadioConfig.LegacyPreferences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='region', full_name='LegacyRadioConfig.LegacyPreferences.region', index=0,
      number=15, type=14, cpp_type=8, label=1,
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
  serialized_start=147,
  serialized_end=195,
)

_LEGACYRADIOCONFIG = _descriptor.Descriptor(
  name='LegacyRadioConfig',
  full_name='LegacyRadioConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='preferences', full_name='LegacyRadioConfig.preferences', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LEGACYRADIOCONFIG_LEGACYPREFERENCES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=195,
)


_DEVICESTATE = _descriptor.Descriptor(
  name='DeviceState',
  full_name='DeviceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacyRadio', full_name='DeviceState.legacyRadio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='my_node', full_name='DeviceState.my_node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='DeviceState.owner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_db', full_name='DeviceState.node_db', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receive_queue', full_name='DeviceState.receive_queue', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='DeviceState.version', index=5,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_text_message', full_name='DeviceState.rx_text_message', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='no_save', full_name='DeviceState.no_save', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='did_gps_reset', full_name='DeviceState.did_gps_reset', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canned_message_plugin_message_part1', full_name='DeviceState.canned_message_plugin_message_part1', index=9,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canned_message_plugin_message_part2', full_name='DeviceState.canned_message_plugin_message_part2', index=10,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canned_message_plugin_message_part3', full_name='DeviceState.canned_message_plugin_message_part3', index=11,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canned_message_plugin_message_part4', full_name='DeviceState.canned_message_plugin_message_part4', index=12,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canned_message_plugin_message_part5', full_name='DeviceState.canned_message_plugin_message_part5', index=13,
      number=17, type=9, cpp_type=9, label=1,
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
  serialized_start=198,
  serialized_end=694,
)


_CHANNELFILE = _descriptor.Descriptor(
  name='ChannelFile',
  full_name='ChannelFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='ChannelFile.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=696,
  serialized_end=737,
)

_LEGACYRADIOCONFIG_LEGACYPREFERENCES.fields_by_name['region'].enum_type = radioconfig__pb2._REGIONCODE
_LEGACYRADIOCONFIG_LEGACYPREFERENCES.containing_type = _LEGACYRADIOCONFIG
_LEGACYRADIOCONFIG.fields_by_name['preferences'].message_type = _LEGACYRADIOCONFIG_LEGACYPREFERENCES
_DEVICESTATE.fields_by_name['legacyRadio'].message_type = _LEGACYRADIOCONFIG
_DEVICESTATE.fields_by_name['my_node'].message_type = mesh__pb2._MYNODEINFO
_DEVICESTATE.fields_by_name['owner'].message_type = mesh__pb2._USER
_DEVICESTATE.fields_by_name['node_db'].message_type = mesh__pb2._NODEINFO
_DEVICESTATE.fields_by_name['receive_queue'].message_type = mesh__pb2._MESHPACKET
_DEVICESTATE.fields_by_name['rx_text_message'].message_type = mesh__pb2._MESHPACKET
_CHANNELFILE.fields_by_name['channels'].message_type = channel__pb2._CHANNEL
DESCRIPTOR.message_types_by_name['LegacyRadioConfig'] = _LEGACYRADIOCONFIG
DESCRIPTOR.message_types_by_name['DeviceState'] = _DEVICESTATE
DESCRIPTOR.message_types_by_name['ChannelFile'] = _CHANNELFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LegacyRadioConfig = _reflection.GeneratedProtocolMessageType('LegacyRadioConfig', (_message.Message,), {

  'LegacyPreferences' : _reflection.GeneratedProtocolMessageType('LegacyPreferences', (_message.Message,), {
    'DESCRIPTOR' : _LEGACYRADIOCONFIG_LEGACYPREFERENCES,
    '__module__' : 'deviceonly_pb2'
    # @@protoc_insertion_point(class_scope:LegacyRadioConfig.LegacyPreferences)
    })
  ,
  'DESCRIPTOR' : _LEGACYRADIOCONFIG,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:LegacyRadioConfig)
  })
_sym_db.RegisterMessage(LegacyRadioConfig)
_sym_db.RegisterMessage(LegacyRadioConfig.LegacyPreferences)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

ChannelFile = _reflection.GeneratedProtocolMessageType('ChannelFile', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELFILE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:ChannelFile)
  })
_sym_db.RegisterMessage(ChannelFile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
