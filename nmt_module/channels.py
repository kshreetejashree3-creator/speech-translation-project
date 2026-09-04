def french_channel(text):
    print(f"[FR] {text}")


def german_channel(text):
    print(f"[DE] {text}")


def spanish_channel(text):
    print(f"[ES] {text}")


CHANNELS = {
    "fr": french_channel,
    "de": german_channel,
    "es": spanish_channel
}