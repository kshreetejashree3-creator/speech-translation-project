# stt_adapter.py
#A demo for me to work ard it
# PLACEHOLDER: we don't yet know the real format the STT module sends.
# Assumption for now: STT sends one plain string per recognized chunk of speech.
# If the real format turns out different (e.g. a dict with a "text" key),
# only this function needs to change — nothing in pipeline.py or translator.py.

from pipeline import translate


def handle_stt_output(stt_text, target_language):
    return translate(stt_text, target_language)