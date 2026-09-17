"""Data models for the translation API contract (design_app.md)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TranslationRequest:
    text: str
    target_language: str

    @staticmethod
    def from_dict(data: dict) -> "TranslationRequest":
        return TranslationRequest(
            text=data.get("text"),
            target_language=data.get("targetLanguage"),
        )


@dataclass(frozen=True)
class TranslationResponse:
    source_text: str
    detected_language: str
    translated_text: str
    target_language: str

    def to_dict(self) -> dict:
        return {
            "sourceText": self.source_text,
            "detectedLanguage": self.detected_language,
            "translatedText": self.translated_text,
            "targetLanguage": self.target_language,
        }


@dataclass(frozen=True)
class ErrorResponse:
    code: str
    message: str

    def to_dict(self) -> dict:
        return {
            "error": {
                "code": self.code,
                "message": self.message,
            }
        }
