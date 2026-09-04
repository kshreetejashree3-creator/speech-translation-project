from models_config import MODEL_NAMES
from transformers import MarianMTModel, MarianTokenizer


class ModelManager:
    def __init__(self):
        self._cache = {}

    def get_model(self, lang_code):
        if lang_code not in MODEL_NAMES:
            raise ValueError(
                f"Invalid language code '{lang_code}'. "
                f"Valid language codes are: {list(MODEL_NAMES.keys())}"
            )

        if lang_code in self._cache:
            return self._cache[lang_code]
        else:
            model_name = MODEL_NAMES[lang_code]
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
            model.eval()

            self._cache[lang_code] = (tokenizer, model)
            return self._cache[lang_code]