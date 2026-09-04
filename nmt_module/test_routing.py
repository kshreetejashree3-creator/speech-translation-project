from model_manager import ModelManager


def test_fr_loads_correct_model():
    manager = ModelManager()
    tokenizer, model = manager.get_model("fr")
    assert "fr" in tokenizer.name_or_path
    print("test_fr_loads_correct_model passed")


def test_invalid_language_raises_error():
    manager = ModelManager()
    try:
        manager.get_model("xyz")
        assert False, "Expected a ValueError but none was raised"
    except ValueError:
        print("test_invalid_language_raises_error passed")


def test_translation_produces_output():
    manager = ModelManager()
    tokenizer, model = manager.get_model("fr")
    from translator import Translator
    translator = Translator(tokenizer, model)
    result = translator.translate("Hello")
    assert isinstance(result, str) and len(result) > 0
    print("test_translation_produces_output passed")


def test_batch_translation_matches_input_length():
    from pipeline import translate_batch
    input_texts = ["Hello", "How are you?"]
    output_texts = translate_batch(input_texts, "fr")
    assert len(input_texts) == len(output_texts)
    print("test_batch_translation_matches_input_length passed")


test_fr_loads_correct_model()
test_invalid_language_raises_error()
test_translation_produces_output()
test_batch_translation_matches_input_length()