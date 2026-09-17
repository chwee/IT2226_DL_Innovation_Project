"""Validation for incoming TranslationRequest payloads (design_app.md)."""

from app.models import TranslationRequest

MAX_TEXT_LENGTH = 5000


class ValidationError(Exception):
    """Raised when a translation request payload fails validation."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


def validate_translation_request(data: dict) -> TranslationRequest:
    """Validate a raw request payload and return a TranslationRequest.

    Raises ValidationError, and has no side effects, on invalid input.
    """
    if not isinstance(data, dict):
        raise ValidationError("Request body must be a JSON object")

    text = data.get("text")
    target_language = data.get("targetLanguage")

    if not isinstance(text, str) or not text.strip():
        raise ValidationError("Text must not be empty")

    if len(text) > MAX_TEXT_LENGTH:
        raise ValidationError(f"Text must not exceed {MAX_TEXT_LENGTH} characters")

    if not isinstance(target_language, str) or not target_language.strip():
        raise ValidationError("Target language is required")

    return TranslationRequest(text=text, target_language=target_language)
