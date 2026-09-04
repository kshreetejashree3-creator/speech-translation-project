# models_config.py
#
# Maps a target language code to the Hugging Face model name
# responsible for translating English -> that language.
MODEL_NAMES = {
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "es": "Helsinki-NLP/opus-mt-en-es",
}