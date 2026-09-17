"""POST /api/translate route (design_app.md API Layer)."""

import logging
import time

from flask import Flask, jsonify, request

from app.models import ErrorResponse, TranslationResponse
from app.translation_service import TranslationServiceError, detect_and_translate
from app.validation import ValidationError, validate_translation_request

logger = logging.getLogger("translator")


def register_routes(app: Flask, translator=None) -> None:
    @app.post("/api/translate")
    def translate():
        start = time.monotonic()
        status_code = 500
        error_code = None

        try:
            payload = request.get_json(silent=True)

            try:
                validated = validate_translation_request(payload)
            except ValidationError as exc:
                status_code = 400
                error_code = "INVALID_INPUT"
                return jsonify(ErrorResponse(code=error_code, message=exc.message).to_dict()), status_code

            try:
                result = detect_and_translate(
                    validated.text, validated.target_language, translator=translator
                )
            except TranslationServiceError as exc:
                status_code = 500
                error_code = "TRANSLATION_FAILED"
                return jsonify(ErrorResponse(code=error_code, message=exc.message).to_dict()), status_code

            response = TranslationResponse(
                source_text=validated.text,
                detected_language=result.detected_language,
                translated_text=result.translated_text,
                target_language=validated.target_language,
            )
            status_code = 200
            return jsonify(response.to_dict()), status_code
        finally:
            duration_ms = (time.monotonic() - start) * 1000
            # Deliberately logs only status/error_code/duration — never text or translatedText.
            logger.info(
                "POST /api/translate status=%s error_code=%s duration_ms=%.2f",
                status_code,
                error_code,
                duration_ms,
            )
