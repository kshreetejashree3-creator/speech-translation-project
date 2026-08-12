from translator import Translator


# Create NMT Translator
nmt = Translator("Helsinki-NLP/opus-mt-en-fr")


# --------------------------------------------------
# Test 1: Single sentence
# --------------------------------------------------

# Simulate STT producing a single transcribed sentence
stt_output = "The weather is nice today."

translated = nmt.translate(stt_output)

print("STT gave:", stt_output)
print("NMT returns:", translated)

# Check that NMT returns a string
assert isinstance(translated, str), "NMT should return a string."

# Check that translation is not empty
assert translated.strip() != "", "Translation should not be empty."


# --------------------------------------------------
# Test 2: Batch of sentences
# --------------------------------------------------

# Simulate STT producing a burst of sentences
stt_batch_output = [
    "Hello.",
    "How is your project going?",
    "Good luck with the demo."
]

translated_batch = nmt.translate(stt_batch_output)

print("\nSTT gave batch:", stt_batch_output)
print("NMT returns batch:", translated_batch)


# Check that the number of translations matches
# the number of input sentences
assert len(stt_batch_output) == len(
    translated_batch
), "Mismatch! Something went wrong."

print("Counts match ✅")


# Check every translation
for translation in translated_batch:
    assert isinstance(
        translation, str
    ), "Each translation should be a string."

    assert translation.strip() != "", \
        "Translation should not be empty."


# --------------------------------------------------
# Test 3: Invalid input
# --------------------------------------------------

# Simulate a bug upstream: STT accidentally sends None
try:
    nmt.translate(None)

except (ValueError, TypeError) as e:
    print("\nHandled bad input gracefully:", e)

else:
    assert False, "Translator should reject None input."


print("\nAll tests passed! ✅")