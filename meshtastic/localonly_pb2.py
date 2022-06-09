# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: localonly.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import config_pb2 as config__pb2
import module_config_pb2 as module__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='localonly.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\017LocalOnlyProtosH\003Z!github.com/meshtastic/gomeshproto',
  serialized_pb=b'\n\x0flocalonly.proto\x1a\x0c\x63onfig.proto\x1a\x13module_config.proto\"\xed\x01\n\x0bLocalConfig\x12$\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x14.Config.DeviceConfig\x12(\n\x08position\x18\x02 \x01(\x0b\x32\x16.Config.PositionConfig\x12\"\n\x05power\x18\x03 \x01(\x0b\x32\x13.Config.PowerConfig\x12 \n\x04wifi\x18\x04 \x01(\x0b\x32\x12.Config.WiFiConfig\x12&\n\x07\x64isplay\x18\x05 \x01(\x0b\x32\x15.Config.DisplayConfig\x12 \n\x04lora\x18\x06 \x01(\x0b\x32\x12.Config.LoRaConfig\"\x89\x03\n\x11LocalModuleConfig\x12&\n\x04mqtt\x18\x01 \x01(\x0b\x32\x18.ModuleConfig.MQTTConfig\x12*\n\x06serial\x18\x02 \x01(\x0b\x32\x1a.ModuleConfig.SerialConfig\x12G\n\x15\x65xternal_notification\x18\x03 \x01(\x0b\x32(.ModuleConfig.ExternalNotificationConfig\x12\x37\n\rstore_forward\x18\x04 \x01(\x0b\x32 .ModuleConfig.StoreForwardConfig\x12\x31\n\nrange_test\x18\x05 \x01(\x0b\x32\x1d.ModuleConfig.RangeTestConfig\x12\x30\n\ttelemetry\x18\x06 \x01(\x0b\x32\x1d.ModuleConfig.TelemetryConfig\x12\x39\n\x0e\x63\x61nned_message\x18\x07 \x01(\x0b\x32!.ModuleConfig.CannedMessageConfigBK\n\x13\x63om.geeksville.meshB\x0fLocalOnlyProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
  ,
  dependencies=[config__pb2.DESCRIPTOR,module__config__pb2.DESCRIPTOR,])




_LOCALCONFIG = _descriptor.Descriptor(
  name='LocalConfig',
  full_name='LocalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='LocalConfig.device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='LocalConfig.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power', full_name='LocalConfig.power', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wifi', full_name='LocalConfig.wifi', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display', full_name='LocalConfig.display', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lora', full_name='LocalConfig.lora', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=55,
  serialized_end=292,
)


_LOCALMODULECONFIG = _descriptor.Descriptor(
  name='LocalModuleConfig',
  full_name='LocalModuleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mqtt', full_name='LocalModuleConfig.mqtt', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial', full_name='LocalModuleConfig.serial', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_notification', full_name='LocalModuleConfig.external_notification', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_forward', full_name='LocalModuleConfig.store_forward', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_test', full_name='LocalModuleConfig.range_test', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry', full_name='LocalModuleConfig.telemetry', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='canned_message', full_name='LocalModuleConfig.canned_message', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=295,
  serialized_end=688,
)

_LOCALCONFIG.fields_by_name['device'].message_type = config__pb2._CONFIG_DEVICECONFIG
_LOCALCONFIG.fields_by_name['position'].message_type = config__pb2._CONFIG_POSITIONCONFIG
_LOCALCONFIG.fields_by_name['power'].message_type = config__pb2._CONFIG_POWERCONFIG
_LOCALCONFIG.fields_by_name['wifi'].message_type = config__pb2._CONFIG_WIFICONFIG
_LOCALCONFIG.fields_by_name['display'].message_type = config__pb2._CONFIG_DISPLAYCONFIG
_LOCALCONFIG.fields_by_name['lora'].message_type = config__pb2._CONFIG_LORACONFIG
_LOCALMODULECONFIG.fields_by_name['mqtt'].message_type = module__config__pb2._MODULECONFIG_MQTTCONFIG
_LOCALMODULECONFIG.fields_by_name['serial'].message_type = module__config__pb2._MODULECONFIG_SERIALCONFIG
_LOCALMODULECONFIG.fields_by_name['external_notification'].message_type = module__config__pb2._MODULECONFIG_EXTERNALNOTIFICATIONCONFIG
_LOCALMODULECONFIG.fields_by_name['store_forward'].message_type = module__config__pb2._MODULECONFIG_STOREFORWARDCONFIG
_LOCALMODULECONFIG.fields_by_name['range_test'].message_type = module__config__pb2._MODULECONFIG_RANGETESTCONFIG
_LOCALMODULECONFIG.fields_by_name['telemetry'].message_type = module__config__pb2._MODULECONFIG_TELEMETRYCONFIG
_LOCALMODULECONFIG.fields_by_name['canned_message'].message_type = module__config__pb2._MODULECONFIG_CANNEDMESSAGECONFIG
DESCRIPTOR.message_types_by_name['LocalConfig'] = _LOCALCONFIG
DESCRIPTOR.message_types_by_name['LocalModuleConfig'] = _LOCALMODULECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocalConfig = _reflection.GeneratedProtocolMessageType('LocalConfig', (_message.Message,), {
  'DESCRIPTOR' : _LOCALCONFIG,
  '__module__' : 'localonly_pb2'
  # @@protoc_insertion_point(class_scope:LocalConfig)
  })
_sym_db.RegisterMessage(LocalConfig)

LocalModuleConfig = _reflection.GeneratedProtocolMessageType('LocalModuleConfig', (_message.Message,), {
  'DESCRIPTOR' : _LOCALMODULECONFIG,
  '__module__' : 'localonly_pb2'
  # @@protoc_insertion_point(class_scope:LocalModuleConfig)
  })
_sym_db.RegisterMessage(LocalModuleConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
