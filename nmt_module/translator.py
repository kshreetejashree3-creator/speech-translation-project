import logging
from transformers import MarianMTModel, MarianTokenizer

# Configure logging once, at the top of the file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class Translator:
    def __init__(self, model_name: str):
        logger.info(f"Loading model: {model_name}")
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)
        self.model.eval()
        logger.info("Model loaded successfully.")

    def _validate(self, text: str) -> str:
        if text is None:
            logger.error("Validation failed: input was None.")
            raise ValueError("Input text cannot be None.")
        if not isinstance(text, str):
            logger.error(f"Validation failed: got type {type(text).__name__}.")
            raise TypeError(f"Expected a string, got {type(text).__name__}.")
        cleaned = text.strip()
        if cleaned == "":
            logger.error("Validation failed: empty or whitespace-only string.")
            raise ValueError("Input text cannot be empty or whitespace-only.")
        if len(cleaned) > 500:
            logger.warning("Input text exceeds 500 characters.")
            raise ValueError("Input text is too long (max 500 characters).")
        return cleaned

    def translate(self, text):
        if isinstance(text, str):
            cleaned = [self._validate(text)]
            logger.debug(f"Translating single sentence: {cleaned[0]}")
            inputs = self.tokenizer(cleaned, return_tensors="pt", padding=True)
            translated_tokens = self.model.generate(**inputs)
            translated = self.tokenizer.batch_decode(
                translated_tokens, skip_special_tokens=True
            )
            logger.info("Translated 1 sentence.")
            return translated[0]

        elif isinstance(text, list):
            if len(text) == 0:
                logger.error("Translation failed: empty list given.")
                raise ValueError("Input list cannot be empty.")
            cleaned = [self._validate(sentence) for sentence in text]
            logger.debug(f"Translating batch of {len(cleaned)} sentences.")
            inputs = self.tokenizer(cleaned, return_tensors="pt", padding=True)
            translated_tokens = self.model.generate(**inputs)
            translated = self.tokenizer.batch_decode(
                translated_tokens, skip_special_tokens=True
            )
            logger.info(f"Translated {len(translated)} sentences.")
            return translated

        else:
            logger.error(f"Translation failed: invalid type {type(text).__name__}.")
            raise TypeError(
                f"Expected a string or list of strings, got {type(text).__name__}."
            )


if __name__ == "__main__":
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    translator = Translator(model_name)

    sentence = "Hi."
    print(sentence, "→", translator.translate(sentence))

    sentences = [
        "Hi.",
        "I love learning about machine translation.",
        "This is my final year project.",
        "i would like to order 500 orages for ₹60 ",
        " OOPs!!!"
    ]
    for original, translated in zip(sentences, translator.translate(sentences)):
        print(original, "→", translated)