# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import tensors_pb2 as tensors__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10generation.proto\x12\x07gooseai\x1a\rtensors.proto\"/\n\x05Token\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\n\n\x02id\x18\x02 \x01(\rB\x07\n\x05_text\"T\n\x06Tokens\x12\x1e\n\x06tokens\x18\x01 \x03(\x0b\x32\x0e.gooseai.Token\x12\x19\n\x0ctokenizer_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_tokenizer_id\"X\n\x18ImageAdjustment_Gaussian\x12\r\n\x05sigma\x18\x01 \x01(\x02\x12-\n\tdirection\x18\x02 \x01(\x0e\x32\x1a.gooseai.GaussianDirection\"\x18\n\x16ImageAdjustment_Invert\"h\n\x16ImageAdjustment_Levels\x12\x11\n\tinput_low\x18\x01 \x01(\x02\x12\x12\n\ninput_high\x18\x02 \x01(\x02\x12\x12\n\noutput_low\x18\x03 \x01(\x02\x12\x13\n\x0boutput_high\x18\x04 \x01(\x02\"\xd2\x01\n\x18ImageAdjustment_Channels\x12&\n\x01r\x18\x01 \x01(\x0e\x32\x16.gooseai.ChannelSourceH\x00\x88\x01\x01\x12&\n\x01g\x18\x02 \x01(\x0e\x32\x16.gooseai.ChannelSourceH\x01\x88\x01\x01\x12&\n\x01\x62\x18\x03 \x01(\x0e\x32\x16.gooseai.ChannelSourceH\x02\x88\x01\x01\x12&\n\x01\x61\x18\x04 \x01(\x0e\x32\x16.gooseai.ChannelSourceH\x03\x88\x01\x01\x42\x04\n\x02_rB\x04\n\x02_gB\x04\n\x02_bB\x04\n\x02_a\"t\n\x17ImageAdjustment_Rescale\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\r\n\x05width\x18\x02 \x01(\x04\x12\"\n\x04mode\x18\x03 \x01(\x0e\x32\x14.gooseai.RescaleMode\x12\x16\n\x0e\x61lgorithm_hint\x18\x04 \x03(\t\"P\n\x14ImageAdjustment_Crop\x12\x0b\n\x03top\x18\x01 \x01(\x04\x12\x0c\n\x04left\x18\x02 \x01(\x04\x12\r\n\x05width\x18\x03 \x01(\x04\x12\x0e\n\x06height\x18\x04 \x01(\x04\"\xd3\x02\n\x0fImageAdjustment\x12\x31\n\x04\x62lur\x18\x01 \x01(\x0b\x32!.gooseai.ImageAdjustment_GaussianH\x00\x12\x31\n\x06invert\x18\x02 \x01(\x0b\x32\x1f.gooseai.ImageAdjustment_InvertH\x00\x12\x31\n\x06levels\x18\x03 \x01(\x0b\x32\x1f.gooseai.ImageAdjustment_LevelsH\x00\x12\x35\n\x08\x63hannels\x18\x04 \x01(\x0b\x32!.gooseai.ImageAdjustment_ChannelsH\x00\x12\x33\n\x07rescale\x18\x05 \x01(\x0b\x32 .gooseai.ImageAdjustment_RescaleH\x00\x12-\n\x04\x63rop\x18\x06 \x01(\x0b\x32\x1d.gooseai.ImageAdjustment_CropH\x00\x42\x0c\n\nadjustment\"\xd7\x03\n\x08\x41rtifact\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x0c\n\x04mime\x18\x03 \x01(\t\x12\x12\n\x05magic\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x06\x62inary\x18\x05 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x06 \x01(\tH\x00\x12!\n\x06tokens\x18\x07 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12\x33\n\nclassifier\x18\x0b \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12!\n\x06tensor\x18\x0e \x01(\x0b\x32\x0f.tensors.TensorH\x00\x12\r\n\x05index\x18\x08 \x01(\r\x12,\n\rfinish_reason\x18\t \x01(\x0e\x32\x15.gooseai.FinishReason\x12\x0c\n\x04seed\x18\n \x01(\r\x12\x0c\n\x04uuid\x18\x0c \x01(\t\x12\x0c\n\x04size\x18\r \x01(\x04\x12.\n\x0b\x61\x64justments\x18\xf4\x03 \x03(\x0b\x32\x18.gooseai.ImageAdjustment\x12\x32\n\x0fpostAdjustments\x18\xf5\x03 \x03(\x0b\x32\x18.gooseai.ImageAdjustmentB\x06\n\x04\x64\x61taB\x08\n\x06_magic\"N\n\x10PromptParameters\x12\x11\n\x04init\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x06weight\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\x07\n\x05_initB\t\n\x07_weight\"\xaf\x01\n\x06Prompt\x12\x32\n\nparameters\x18\x01 \x01(\x0b\x32\x19.gooseai.PromptParametersH\x01\x88\x01\x01\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12!\n\x06tokens\x18\x03 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12%\n\x08\x61rtifact\x18\x04 \x01(\x0b\x32\x11.gooseai.ArtifactH\x00\x42\x08\n\x06promptB\r\n\x0b_parameters\"\xef\x01\n\x11SamplerParameters\x12\x10\n\x03\x65ta\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x0esampling_steps\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x1c\n\x0flatent_channels\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12 \n\x13\x64ownsampling_factor\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x16\n\tcfg_scale\x18\x05 \x01(\x02H\x04\x88\x01\x01\x42\x06\n\x04_etaB\x11\n\x0f_sampling_stepsB\x12\n\x10_latent_channelsB\x16\n\x14_downsampling_factorB\x0c\n\n_cfg_scale\"\x8b\x01\n\x15\x43onditionerParameters\x12 \n\x13vector_adjust_prior\x18\x01 \x01(\tH\x00\x88\x01\x01\x12(\n\x0b\x63onditioner\x18\x02 \x01(\x0b\x32\x0e.gooseai.ModelH\x01\x88\x01\x01\x42\x16\n\x14_vector_adjust_priorB\x0e\n\x0c_conditioner\"j\n\x12ScheduleParameters\x12\x12\n\x05start\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x10\n\x03\x65nd\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05value\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\x08\n\x06_startB\x06\n\x04_endB\x08\n\x06_value\"\xe4\x01\n\rStepParameter\x12\x13\n\x0bscaled_step\x18\x01 \x01(\x02\x12\x30\n\x07sampler\x18\x02 \x01(\x0b\x32\x1a.gooseai.SamplerParametersH\x00\x88\x01\x01\x12\x32\n\x08schedule\x18\x03 \x01(\x0b\x32\x1b.gooseai.ScheduleParametersH\x01\x88\x01\x01\x12\x32\n\x08guidance\x18\x04 \x01(\x0b\x32\x1b.gooseai.GuidanceParametersH\x02\x88\x01\x01\x42\n\n\x08_samplerB\x0b\n\t_scheduleB\x0b\n\t_guidance\"\x97\x01\n\x05Model\x12\x30\n\x0c\x61rchitecture\x18\x01 \x01(\x0e\x32\x1a.gooseai.ModelArchitecture\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x02\x12\x18\n\x10semantic_version\x18\x05 \x01(\t\x12\r\n\x05\x61lias\x18\x06 \x01(\t\"\xbc\x01\n\x10\x43utoutParameters\x12*\n\x07\x63utouts\x18\x01 \x03(\x0b\x32\x19.gooseai.CutoutParameters\x12\x12\n\x05\x63ount\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04gray\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04\x62lur\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\nsize_power\x18\x05 \x01(\x02H\x03\x88\x01\x01\x42\x08\n\x06_countB\x07\n\x05_grayB\x07\n\x05_blurB\r\n\x0b_size_power\"=\n\x1aGuidanceScheduleParameters\x12\x10\n\x08\x64uration\x18\x01 \x01(\x02\x12\r\n\x05value\x18\x02 \x01(\x02\"\x97\x02\n\x1aGuidanceInstanceParameters\x12\x1e\n\x06models\x18\x02 \x03(\x0b\x32\x0e.gooseai.Model\x12\x1e\n\x11guidance_strength\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12\x35\n\x08schedule\x18\x04 \x03(\x0b\x32#.gooseai.GuidanceScheduleParameters\x12/\n\x07\x63utouts\x18\x05 \x01(\x0b\x32\x19.gooseai.CutoutParametersH\x01\x88\x01\x01\x12$\n\x06prompt\x18\x06 \x01(\x0b\x32\x0f.gooseai.PromptH\x02\x88\x01\x01\x42\x14\n\x12_guidance_strengthB\n\n\x08_cutoutsB\t\n\x07_prompt\"~\n\x12GuidanceParameters\x12\x30\n\x0fguidance_preset\x18\x01 \x01(\x0e\x32\x17.gooseai.GuidancePreset\x12\x36\n\tinstances\x18\x02 \x03(\x0b\x32#.gooseai.GuidanceInstanceParameters\"n\n\rTransformType\x12.\n\tdiffusion\x18\x01 \x01(\x0e\x32\x19.gooseai.DiffusionSamplerH\x00\x12%\n\x08upscaler\x18\x02 \x01(\x0e\x32\x11.gooseai.UpscalerH\x00\x42\x06\n\x04type\"Y\n\x11\x45xtendedParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x05\x66loat\x18\x02 \x01(\x02H\x00\x12\r\n\x03int\x18\x03 \x01(\x04H\x00\x12\r\n\x03str\x18\x04 \x01(\tH\x00\x42\x07\n\x05value\"D\n\x12\x45xtendedParameters\x12.\n\nparameters\x18\x01 \x03(\x0b\x32\x1a.gooseai.ExtendedParameter\"\xcb\x02\n\x0fImageParameters\x12\x13\n\x06height\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x12\n\x05width\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x0c\n\x04seed\x18\x03 \x03(\r\x12\x14\n\x07samples\x18\x04 \x01(\x04H\x02\x88\x01\x01\x12\x12\n\x05steps\x18\x05 \x01(\x04H\x03\x88\x01\x01\x12.\n\ttransform\x18\x06 \x01(\x0b\x32\x16.gooseai.TransformTypeH\x04\x88\x01\x01\x12*\n\nparameters\x18\x07 \x03(\x0b\x32\x16.gooseai.StepParameter\x12\x34\n\textension\x18\xf4\x03 \x01(\x0b\x32\x1b.gooseai.ExtendedParametersH\x05\x88\x01\x01\x42\t\n\x07_heightB\x08\n\x06_widthB\n\n\x08_samplesB\x08\n\x06_stepsB\x0c\n\n_transformB\x0c\n\n_extension\"J\n\x11\x43lassifierConcept\x12\x0f\n\x07\x63oncept\x18\x01 \x01(\t\x12\x16\n\tthreshold\x18\x02 \x01(\x02H\x00\x88\x01\x01\x42\x0c\n\n_threshold\"\xf4\x01\n\x12\x43lassifierCategory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x1a.gooseai.ClassifierConcept\x12\x17\n\nadjustment\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x0f.gooseai.ActionH\x01\x88\x01\x01\x12\x35\n\x0f\x63lassifier_mode\x18\x05 \x01(\x0e\x32\x17.gooseai.ClassifierModeH\x02\x88\x01\x01\x42\r\n\x0b_adjustmentB\t\n\x07_actionB\x12\n\x10_classifier_mode\"\xb8\x01\n\x14\x43lassifierParameters\x12/\n\ncategories\x18\x01 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12,\n\x07\x65xceeds\x18\x02 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12-\n\x0frealized_action\x18\x03 \x01(\x0e\x32\x0f.gooseai.ActionH\x00\x88\x01\x01\x42\x12\n\x10_realized_action\"k\n\x0f\x41ssetParameters\x12$\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x14.gooseai.AssetAction\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x1e\n\x03use\x18\x03 \x01(\x0e\x32\x11.gooseai.AssetUse\"\x94\x01\n\nAnswerMeta\x12\x13\n\x06gpu_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x63pu_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07node_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tengine_id\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\t\n\x07_gpu_idB\t\n\x07_cpu_idB\n\n\x08_node_idB\x0c\n\n_engine_id\"\xa9\x01\n\x06\x41nswer\x12\x11\n\tanswer_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x10\n\x08received\x18\x03 \x01(\x04\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x04\x12&\n\x04meta\x18\x06 \x01(\x0b\x32\x13.gooseai.AnswerMetaH\x00\x88\x01\x01\x12$\n\tartifacts\x18\x07 \x03(\x0b\x32\x11.gooseai.ArtifactB\x07\n\x05_meta\"\xdf\x02\n\x07Request\x12\x11\n\tengine_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12-\n\x0erequested_type\x18\x03 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x1f\n\x06prompt\x18\x04 \x03(\x0b\x32\x0f.gooseai.Prompt\x12)\n\x05image\x18\x05 \x01(\x0b\x32\x18.gooseai.ImageParametersH\x00\x12\x33\n\nclassifier\x18\x07 \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12)\n\x05\x61sset\x18\x08 \x01(\x0b\x32\x18.gooseai.AssetParametersH\x00\x12\x38\n\x0b\x63onditioner\x18\x06 \x01(\x0b\x32\x1e.gooseai.ConditionerParametersH\x01\x88\x01\x01\x42\x08\n\x06paramsB\x0e\n\x0c_conditioner\"w\n\x08OnStatus\x12%\n\x06reason\x18\x01 \x03(\x0e\x32\x15.gooseai.FinishReason\x12\x13\n\x06target\x18\x02 \x01(\tH\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x03 \x03(\x0e\x32\x14.gooseai.StageActionB\t\n\x07_target\"\\\n\x05Stage\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x07request\x18\x02 \x01(\x0b\x32\x10.gooseai.Request\x12$\n\ton_status\x18\x03 \x03(\x0b\x32\x11.gooseai.OnStatus\"A\n\x0c\x43hainRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\x05stage\x18\x02 \x03(\x0b\x32\x0e.gooseai.Stage*E\n\x0c\x46inishReason\x12\x08\n\x04NULL\x10\x00\x12\n\n\x06LENGTH\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\n\n\x06\x46ILTER\x10\x04*\xe4\x01\n\x0c\x41rtifactType\x12\x11\n\rARTIFACT_NONE\x10\x00\x12\x12\n\x0e\x41RTIFACT_IMAGE\x10\x01\x12\x12\n\x0e\x41RTIFACT_VIDEO\x10\x02\x12\x11\n\rARTIFACT_TEXT\x10\x03\x12\x13\n\x0f\x41RTIFACT_TOKENS\x10\x04\x12\x16\n\x12\x41RTIFACT_EMBEDDING\x10\x05\x12\x1c\n\x18\x41RTIFACT_CLASSIFICATIONS\x10\x06\x12\x11\n\rARTIFACT_MASK\x10\x07\x12\x13\n\x0f\x41RTIFACT_LATENT\x10\x08\x12\x13\n\x0f\x41RTIFACT_TENSOR\x10\t*M\n\x11GaussianDirection\x12\x12\n\x0e\x44IRECTION_NONE\x10\x00\x12\x10\n\x0c\x44IRECTION_UP\x10\x01\x12\x12\n\x0e\x44IRECTION_DOWN\x10\x02*\x83\x01\n\rChannelSource\x12\r\n\tCHANNEL_R\x10\x00\x12\r\n\tCHANNEL_G\x10\x01\x12\r\n\tCHANNEL_B\x10\x02\x12\r\n\tCHANNEL_A\x10\x03\x12\x10\n\x0c\x43HANNEL_ZERO\x10\x04\x12\x0f\n\x0b\x43HANNEL_ONE\x10\x05\x12\x13\n\x0f\x43HANNEL_DISCARD\x10\x06*D\n\x0bRescaleMode\x12\x12\n\x0eRESCALE_STRICT\x10\x00\x12\x10\n\x0cRESCALE_CROP\x10\x02\x12\x0f\n\x0bRESCALE_FIT\x10\x03*\xa8\x02\n\x10\x44iffusionSampler\x12\x10\n\x0cSAMPLER_DDIM\x10\x00\x12\x10\n\x0cSAMPLER_DDPM\x10\x01\x12\x13\n\x0fSAMPLER_K_EULER\x10\x02\x12\x1d\n\x19SAMPLER_K_EULER_ANCESTRAL\x10\x03\x12\x12\n\x0eSAMPLER_K_HEUN\x10\x04\x12\x13\n\x0fSAMPLER_K_DPM_2\x10\x05\x12\x1d\n\x19SAMPLER_K_DPM_2_ANCESTRAL\x10\x06\x12\x11\n\rSAMPLER_K_LMS\x10\x07\x12\x1f\n\x1aSAMPLER_DPMSOLVERPP_1ORDER\x10\xf4\x03\x12\x1f\n\x1aSAMPLER_DPMSOLVERPP_2ORDER\x10\xf5\x03\x12\x1f\n\x1aSAMPLER_DPMSOLVERPP_3ORDER\x10\xf6\x03*F\n\x08Upscaler\x12\x10\n\x0cUPSCALER_RGB\x10\x00\x12\x13\n\x0fUPSCALER_GFPGAN\x10\x01\x12\x13\n\x0fUPSCALER_ESRGAN\x10\x02*\xd8\x01\n\x0eGuidancePreset\x12\x18\n\x14GUIDANCE_PRESET_NONE\x10\x00\x12\x1a\n\x16GUIDANCE_PRESET_SIMPLE\x10\x01\x12\x1d\n\x19GUIDANCE_PRESET_FAST_BLUE\x10\x02\x12\x1e\n\x1aGUIDANCE_PRESET_FAST_GREEN\x10\x03\x12\x18\n\x14GUIDANCE_PRESET_SLOW\x10\x04\x12\x1a\n\x16GUIDANCE_PRESET_SLOWER\x10\x05\x12\x1b\n\x17GUIDANCE_PRESET_SLOWEST\x10\x06*\x91\x01\n\x11ModelArchitecture\x12\x1b\n\x17MODEL_ARCHITECTURE_NONE\x10\x00\x12\x1f\n\x1bMODEL_ARCHITECTURE_CLIP_VIT\x10\x01\x12\"\n\x1eMODEL_ARCHITECTURE_CLIP_RESNET\x10\x02\x12\x1a\n\x16MODEL_ARCHITECTURE_LDM\x10\x03*\xa2\x01\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_PASSTHROUGH\x10\x00\x12\x1f\n\x1b\x41\x43TION_REGENERATE_DUPLICATE\x10\x01\x12\x15\n\x11\x41\x43TION_REGENERATE\x10\x02\x12\x1e\n\x1a\x41\x43TION_OBFUSCATE_DUPLICATE\x10\x03\x12\x14\n\x10\x41\x43TION_OBFUSCATE\x10\x04\x12\x12\n\x0e\x41\x43TION_DISCARD\x10\x05*D\n\x0e\x43lassifierMode\x12\x17\n\x13\x43LSFR_MODE_ZEROSHOT\x10\x00\x12\x19\n\x15\x43LSFR_MODE_MULTICLASS\x10\x01*=\n\x0b\x41ssetAction\x12\r\n\tASSET_PUT\x10\x00\x12\r\n\tASSET_GET\x10\x01\x12\x10\n\x0c\x41SSET_DELETE\x10\x02*\x81\x01\n\x08\x41ssetUse\x12\x17\n\x13\x41SSET_USE_UNDEFINED\x10\x00\x12\x13\n\x0f\x41SSET_USE_INPUT\x10\x01\x12\x14\n\x10\x41SSET_USE_OUTPUT\x10\x02\x12\x1a\n\x16\x41SSET_USE_INTERMEDIATE\x10\x03\x12\x15\n\x11\x41SSET_USE_PROJECT\x10\x04*W\n\x0bStageAction\x12\x15\n\x11STAGE_ACTION_PASS\x10\x00\x12\x18\n\x14STAGE_ACTION_DISCARD\x10\x01\x12\x17\n\x13STAGE_ACTION_RETURN\x10\x02\x32\x83\x01\n\x11GenerationService\x12\x31\n\x08Generate\x12\x10.gooseai.Request\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x12;\n\rChainGenerate\x12\x15.gooseai.ChainRequest\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x42\x0fZ\r./;generationb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\r./;generation'
  _FINISHREASON._serialized_start=5614
  _FINISHREASON._serialized_end=5683
  _ARTIFACTTYPE._serialized_start=5686
  _ARTIFACTTYPE._serialized_end=5914
  _GAUSSIANDIRECTION._serialized_start=5916
  _GAUSSIANDIRECTION._serialized_end=5993
  _CHANNELSOURCE._serialized_start=5996
  _CHANNELSOURCE._serialized_end=6127
  _RESCALEMODE._serialized_start=6129
  _RESCALEMODE._serialized_end=6197
  _DIFFUSIONSAMPLER._serialized_start=6200
  _DIFFUSIONSAMPLER._serialized_end=6496
  _UPSCALER._serialized_start=6498
  _UPSCALER._serialized_end=6568
  _GUIDANCEPRESET._serialized_start=6571
  _GUIDANCEPRESET._serialized_end=6787
  _MODELARCHITECTURE._serialized_start=6790
  _MODELARCHITECTURE._serialized_end=6935
  _ACTION._serialized_start=6938
  _ACTION._serialized_end=7100
  _CLASSIFIERMODE._serialized_start=7102
  _CLASSIFIERMODE._serialized_end=7170
  _ASSETACTION._serialized_start=7172
  _ASSETACTION._serialized_end=7233
  _ASSETUSE._serialized_start=7236
  _ASSETUSE._serialized_end=7365
  _STAGEACTION._serialized_start=7367
  _STAGEACTION._serialized_end=7454
  _TOKEN._serialized_start=44
  _TOKEN._serialized_end=91
  _TOKENS._serialized_start=93
  _TOKENS._serialized_end=177
  _IMAGEADJUSTMENT_GAUSSIAN._serialized_start=179
  _IMAGEADJUSTMENT_GAUSSIAN._serialized_end=267
  _IMAGEADJUSTMENT_INVERT._serialized_start=269
  _IMAGEADJUSTMENT_INVERT._serialized_end=293
  _IMAGEADJUSTMENT_LEVELS._serialized_start=295
  _IMAGEADJUSTMENT_LEVELS._serialized_end=399
  _IMAGEADJUSTMENT_CHANNELS._serialized_start=402
  _IMAGEADJUSTMENT_CHANNELS._serialized_end=612
  _IMAGEADJUSTMENT_RESCALE._serialized_start=614
  _IMAGEADJUSTMENT_RESCALE._serialized_end=730
  _IMAGEADJUSTMENT_CROP._serialized_start=732
  _IMAGEADJUSTMENT_CROP._serialized_end=812
  _IMAGEADJUSTMENT._serialized_start=815
  _IMAGEADJUSTMENT._serialized_end=1154
  _ARTIFACT._serialized_start=1157
  _ARTIFACT._serialized_end=1628
  _PROMPTPARAMETERS._serialized_start=1630
  _PROMPTPARAMETERS._serialized_end=1708
  _PROMPT._serialized_start=1711
  _PROMPT._serialized_end=1886
  _SAMPLERPARAMETERS._serialized_start=1889
  _SAMPLERPARAMETERS._serialized_end=2128
  _CONDITIONERPARAMETERS._serialized_start=2131
  _CONDITIONERPARAMETERS._serialized_end=2270
  _SCHEDULEPARAMETERS._serialized_start=2272
  _SCHEDULEPARAMETERS._serialized_end=2378
  _STEPPARAMETER._serialized_start=2381
  _STEPPARAMETER._serialized_end=2609
  _MODEL._serialized_start=2612
  _MODEL._serialized_end=2763
  _CUTOUTPARAMETERS._serialized_start=2766
  _CUTOUTPARAMETERS._serialized_end=2954
  _GUIDANCESCHEDULEPARAMETERS._serialized_start=2956
  _GUIDANCESCHEDULEPARAMETERS._serialized_end=3017
  _GUIDANCEINSTANCEPARAMETERS._serialized_start=3020
  _GUIDANCEINSTANCEPARAMETERS._serialized_end=3299
  _GUIDANCEPARAMETERS._serialized_start=3301
  _GUIDANCEPARAMETERS._serialized_end=3427
  _TRANSFORMTYPE._serialized_start=3429
  _TRANSFORMTYPE._serialized_end=3539
  _EXTENDEDPARAMETER._serialized_start=3541
  _EXTENDEDPARAMETER._serialized_end=3630
  _EXTENDEDPARAMETERS._serialized_start=3632
  _EXTENDEDPARAMETERS._serialized_end=3700
  _IMAGEPARAMETERS._serialized_start=3703
  _IMAGEPARAMETERS._serialized_end=4034
  _CLASSIFIERCONCEPT._serialized_start=4036
  _CLASSIFIERCONCEPT._serialized_end=4110
  _CLASSIFIERCATEGORY._serialized_start=4113
  _CLASSIFIERCATEGORY._serialized_end=4357
  _CLASSIFIERPARAMETERS._serialized_start=4360
  _CLASSIFIERPARAMETERS._serialized_end=4544
  _ASSETPARAMETERS._serialized_start=4546
  _ASSETPARAMETERS._serialized_end=4653
  _ANSWERMETA._serialized_start=4656
  _ANSWERMETA._serialized_end=4804
  _ANSWER._serialized_start=4807
  _ANSWER._serialized_end=4976
  _REQUEST._serialized_start=4979
  _REQUEST._serialized_end=5330
  _ONSTATUS._serialized_start=5332
  _ONSTATUS._serialized_end=5451
  _STAGE._serialized_start=5453
  _STAGE._serialized_end=5545
  _CHAINREQUEST._serialized_start=5547
  _CHAINREQUEST._serialized_end=5612
  _GENERATIONSERVICE._serialized_start=7457
  _GENERATIONSERVICE._serialized_end=7588
# @@protoc_insertion_point(module_scope)