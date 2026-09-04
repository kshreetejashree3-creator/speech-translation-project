from pipeline import translate, translate_batch
from stt_adapter import handle_stt_output
from channels import CHANNELS

print(translate("Good morning", "fr"))

print(translate("Good morning", "de"))

print(translate("Good morning", "es"))

print(handle_stt_output("Good morning", "fr"))

try:
    translate("Good morning", "xyz")
except ValueError as e:
    print("Caught expected error:", e)

def print_channel(translated_text):
    print(translated_text)

stt_chunks = [("Hello", "fr"), ("How are you?", "de"), ("Good bye", "es")]

for text, lang in stt_chunks:
    result = handle_stt_output(text, lang)
    CHANNELS[lang](result)
