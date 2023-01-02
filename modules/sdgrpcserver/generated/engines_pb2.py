# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engines.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import generation_pb2 as generation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rengines.proto\x12\x07gooseai\x1a\x10generation.proto\"\xdf\x01\n\rEngineSampler\x12*\n\x07sampler\x18\x01 \x01(\x0e\x32\x19.gooseai.DiffusionSampler\x12\x14\n\x0csupports_eta\x18\n \x01(\x08\x12\x16\n\x0esupports_churn\x18\x0b \x01(\x08\x12\x1d\n\x15supports_sigma_limits\x18\x0c \x01(\x08\x12\x1b\n\x13supports_karras_rho\x18\r \x01(\x08\x12\x38\n\x15supported_noise_types\x18\x14 \x03(\x0e\x32\x19.gooseai.SamplerNoiseType\"\xde\x01\n\nEngineInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\r\n\x05ready\x18\x03 \x01(\x08\x12!\n\x04type\x18\x04 \x01(\x0e\x32\x13.gooseai.EngineType\x12+\n\ttokenizer\x18\x05 \x01(\x0e\x32\x18.gooseai.EngineTokenizer\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x33\n\x12supported_samplers\x18\xf4\x03 \x03(\x0b\x32\x16.gooseai.EngineSampler\"\x14\n\x12ListEnginesRequest\".\n\x07\x45ngines\x12#\n\x06\x65ngine\x18\x01 \x03(\x0b\x32\x13.gooseai.EngineInfo*Z\n\nEngineType\x12\x08\n\x04TEXT\x10\x00\x12\x0b\n\x07PICTURE\x10\x01\x12\t\n\x05\x41UDIO\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\x12\n\x0e\x43LASSIFICATION\x10\x04\x12\x0b\n\x07STORAGE\x10\x05*%\n\x0f\x45ngineTokenizer\x12\x08\n\x04GPT2\x10\x00\x12\x08\n\x04PILE\x10\x01\x32P\n\x0e\x45nginesService\x12>\n\x0bListEngines\x12\x1b.gooseai.ListEnginesRequest\x1a\x10.gooseai.Engines\"\x00\x42\x38Z6github.com/stability-ai/api-interfaces/gooseai/enginesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'engines_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/stability-ai/api-interfaces/gooseai/engines'
  _ENGINETYPE._serialized_start=565
  _ENGINETYPE._serialized_end=655
  _ENGINETOKENIZER._serialized_start=657
  _ENGINETOKENIZER._serialized_end=694
  _ENGINESAMPLER._serialized_start=45
  _ENGINESAMPLER._serialized_end=268
  _ENGINEINFO._serialized_start=271
  _ENGINEINFO._serialized_end=493
  _LISTENGINESREQUEST._serialized_start=495
  _LISTENGINESREQUEST._serialized_end=515
  _ENGINES._serialized_start=517
  _ENGINES._serialized_end=563
  _ENGINESSERVICE._serialized_start=696
  _ENGINESSERVICE._serialized_end=776
# @@protoc_insertion_point(module_scope)
