"""Task 3 — Translation Service unit tests (mocked googletrans, no network)."""

from unittest.mock import MagicMock

import pytest

from app.translation_service import TranslationServiceError, detect_and_translate


def test_success_returns_detected_language_and_translated_text():
    translator = MagicMock()
    translator.detect.return_value = MagicMock(lang="en")
    translator.translate.return_value = MagicMock(text="Bonjour")

    result = detect_and_translate("Hello", "fr", translator=translator)

    assert result.detected_language == "en"
    assert result.translated_text == "Bonjour"
    translator.detect.assert_called_once_with("Hello")
    translator.translate.assert_called_once_with("Hello", dest="fr")


def test_detect_failure_raises_translation_service_error_not_raw_exception():
    translator = MagicMock()
    translator.detect.side_effect = RuntimeError("network down")

    with pytest.raises(TranslationServiceError):
        detect_and_translate("Hello", "fr", translator=translator)


def test_translate_failure_raises_translation_service_error_not_raw_exception():
    translator = MagicMock()
    translator.detect.return_value = MagicMock(lang="en")
    translator.translate.side_effect = RuntimeError("network down")

    with pytest.raises(TranslationServiceError):
        detect_and_translate("Hello", "fr", translator=translator)


def test_unexpected_empty_translation_result_raises_translation_service_error():
    translator = MagicMock()
    translator.detect.return_value = MagicMock(lang="en")
    translator.translate.return_value = MagicMock(text=None)

    with pytest.raises(TranslationServiceError):
        detect_and_translate("Hello", "fr", translator=translator)


def test_unexpected_empty_detection_result_raises_translation_service_error():
    translator = MagicMock()
    translator.detect.return_value = MagicMock(lang=None)
    translator.translate.return_value = MagicMock(text="Bonjour")

    with pytest.raises(TranslationServiceError):
        detect_and_translate("Hello", "fr", translator=translator)
