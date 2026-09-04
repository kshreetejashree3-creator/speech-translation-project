from translator import Translator
from model_manager import ModelManager


manager = ModelManager()


def translate(text, target_language):
    tokenizer, model = manager.get_model(target_language)

    translator = Translator(tokenizer, model)

    return translator.translate(text)


def translate_batch(texts, target_language):
    tokenizer, model = manager.get_model(target_language)

    translator = Translator(tokenizer, model)

    return translator.translate(texts)