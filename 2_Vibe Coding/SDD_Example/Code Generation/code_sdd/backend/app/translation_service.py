"""Translation Service business logic wrapping googletrans (design_app.md)."""

from dataclasses import dataclass

from googletrans import Translator


class TranslationServiceError(Exception):
    """Raised when the underlying translation library fails or returns
    an unusable result. Never exposes the raw library exception/traceback."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


@dataclass(frozen=True)
class TranslationResult:
    detected_language: str
    translated_text: str


def detect_and_translate(text: str, target_language: str, translator: Translator = None) -> TranslationResult:
    """Detect the source language of `text` and translate it to `target_language`.

    Accepts an injectable `translator` (any object exposing `.detect()` and
    `.translate()` like googletrans.Translator) so callers can mock it in tests
    without a live network dependency.
    """
    client = translator if translator is not None else Translator()

    try:
        detection = client.detect(text)
        translation = client.translate(text, dest=target_language)
    except Exception as exc:
        raise TranslationServiceError("Translation service is currently unavailable") from exc

    detected_language = getattr(detection, "lang", None)
    translated_text = getattr(translation, "text", None)

    if not detected_language or not translated_text:
        raise TranslationServiceError("Translation service returned an unexpected result")

    return TranslationResult(detected_language=detected_language, translated_text=translated_text)
