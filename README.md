# NMT Module — Speech Translation Project

## Overview
This module translates English text into French, German, or Spanish. It receives text
from the STT (Speech-to-Text) teammate's module, selects the correct translation model
based on the requested target language, translates the text, and sends the result to
the appropriate output channel.

## Supported Languages
| Code | Language | Model                          |
|------|----------|---------------------------------|
| fr   | French   | Helsinki-NLP/opus-mt-en-fr      |
| de   | German   | Helsinki-NLP/opus-mt-en-de      |
| es   | Spanish  | Helsinki-NLP/opus-mt-en-es      |

## Architecture
STT
↓
stt_adapter.handle_stt_output()
↓
pipeline.translate() / translate_batch()
↓
model_manager.ModelManager (loads + caches models)
↓
translator.Translator (tokenize → generate → decode)
↓
channels.CHANNELS (routes output by language)


## File Structure
- `models_config.py` — maps language code → Hugging Face model name
- `model_manager.py` — loads and caches models per language, raises a clear error for unsupported codes
- `translator.py` — validates input, tokenizes, translates, decodes (single or batch)
- `pipeline.py` — reusable `translate(text, lang)` and `translate_batch(texts, lang)` interface
- `stt_adapter.py` — entry point for STT output (placeholder until real STT format is confirmed)
- `channels.py` — routes translated output to a destination based on language
- `test_routing.py` — automated tests
- `experiment.py` — manual scratch/testing file

## How to Run
```bash
python experiment.py
```

## Example
```python
from pipeline import translate, translate_batch

translate("Good morning", "fr")
# "Bonjour"

translate_batch(["Hello", "How are you?"], "de")
# ["Hallo", "Wie geht es dir?"]
```

## Batch vs Streaming
Translation can run in two modes:
- **Batch** — translate a list of sentences all at once (`translate_batch`)
- **Streaming (simple form)** — translate each sentence as soon as it arrives, one at a
  time in a loop, without waiting for others. This matches how live speech actually
  works, since STT produces text in small chunks rather than all at once.

Currently, streaming is implemented as a simple `for` loop over incoming chunks — no
async or threading is used yet, since it isn't needed at this stage.

## Testing
Run:
```bash
python test_routing.py
```
Tests cover: correct model routing, invalid language handling, translation output
validity, and batch output length matching input length.

## Future Work
- Confirm real STT output format and update `stt_adapter.py` accordingly
- Add more languages by adding an entry to `models_config.py` — no other file needs
  to change
- Replace placeholder channels with real destinations (e.g. text-to-speech module)
- Add async/streaming only if performance requires it, after profiling