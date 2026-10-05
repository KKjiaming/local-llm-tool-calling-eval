"""Local model registration; official BFCL tool conversion and decoding unchanged."""
from bfcl_eval.constants.enums import ModelStyle
from bfcl_eval.constants.model_config import MODEL_CONFIG_MAPPING, ModelConfig
from bfcl_eval.model_handler.api_inference.openai_completion import OpenAICompletionsHandler
from bfcl_eval.model_handler.base_handler import BaseHandler

class LocalHandler(OpenAICompletionsHandler):
    def __init__(self, model_name, temperature=0, registry_name=None, is_fc_model=True, **kwargs):
        # Scoring / preparation only: no client initialization or credential lookup.
        BaseHandler.__init__(self, model_name, temperature, registry_name or model_name, is_fc_model, **kwargs)
        self.model_style = ModelStyle.OPENAI_COMPLETIONS

def register(model_id):
    name = model_id + "-local-FC"
    MODEL_CONFIG_MAPPING[name] = ModelConfig(model_name=model_id, display_name=name,
        url="https://huggingface.co/" + model_id, org=model_id.split("/")[0],
        license="See pinned model card", model_handler=LocalHandler,
        is_fc_model=True, underscore_to_dot=True)
    return name
