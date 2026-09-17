import pytest

from app.models import TranslationRequest
from app.validation import MAX_TEXT_LENGTH, ValidationError, validate_translation_request


def test_rejects_empty_text():
    with pytest.raises(ValidationError):
        validate_translation_request({"text": "", "targetLanguage": "fr"})


def test_rejects_whitespace_only_text():
    with pytest.raises(ValidationError):
        validate_translation_request({"text": "   \t\n  ", "targetLanguage": "fr"})


def test_rejects_missing_text():
    with pytest.raises(ValidationError):
        validate_translation_request({"targetLanguage": "fr"})


def test_rejects_text_over_max_length():
    oversized_text = "a" * (MAX_TEXT_LENGTH + 1)
    with pytest.raises(ValidationError):
        validate_translation_request({"text": oversized_text, "targetLanguage": "fr"})


def test_accepts_text_at_max_length():
    boundary_text = "a" * MAX_TEXT_LENGTH
    result = validate_translation_request({"text": boundary_text, "targetLanguage": "fr"})
    assert result.text == boundary_text


def test_rejects_missing_target_language():
    with pytest.raises(ValidationError):
        validate_translation_request({"text": "hello"})


def test_rejects_blank_target_language():
    with pytest.raises(ValidationError):
        validate_translation_request({"text": "hello", "targetLanguage": "  "})


def test_valid_input_passes_and_returns_translation_request():
    result = validate_translation_request({"text": "hello world", "targetLanguage": "fr"})
    assert result == TranslationRequest(text="hello world", target_language="fr")


def test_valid_input_has_no_side_effects():
    payload = {"text": "hello world", "targetLanguage": "fr"}
    payload_copy = dict(payload)
    validate_translation_request(payload)
    assert payload == payload_copy
