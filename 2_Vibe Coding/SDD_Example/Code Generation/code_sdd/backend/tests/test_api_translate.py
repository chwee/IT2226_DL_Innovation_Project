"""Task 4.1-4.4 — POST /api/translate integration tests (Flask test client).

Uses an injected mock translator so these tests never depend on a live
network call to googletrans.
"""

from unittest.mock import MagicMock

import pytest

from app import create_app


@pytest.fixture
def mock_translator():
    translator = MagicMock()
    translator.detect.return_value = MagicMock(lang="en")
    translator.translate.return_value = MagicMock(text="Bonjour le monde")
    return translator


@pytest.fixture
def client(mock_translator):
    app = create_app(translator=mock_translator)
    app.testing = True
    return app.test_client()


# --- Task 4.1: request validation -------------------------------------------------

def test_task_4_1_empty_text_returns_400_and_never_calls_service(client, mock_translator):
    response = client.post("/api/translate", json={"text": "", "targetLanguage": "fr"})

    assert response.status_code == 400
    body = response.get_json()
    assert body["code"] == "INVALID_INPUT"
    mock_translator.translate.assert_not_called()


def test_task_4_1_missing_target_language_returns_400_and_never_calls_service(client, mock_translator):
    response = client.post("/api/translate", json={"text": "Hello"})

    assert response.status_code == 400
    body = response.get_json()
    assert body["code"] == "INVALID_INPUT"
    mock_translator.translate.assert_not_called()


def test_task_4_1_oversized_text_returns_400_and_never_calls_service(client, mock_translator):
    response = client.post("/api/translate", json={"text": "a" * 5001, "targetLanguage": "fr"})

    assert response.status_code == 400
    body = response.get_json()
    assert body["code"] == "INVALID_INPUT"
    mock_translator.translate.assert_not_called()


def test_task_4_1_malformed_json_body_returns_400(client, mock_translator):
    response = client.post(
        "/api/translate", data="not json", content_type="application/json"
    )

    assert response.status_code == 400
    assert response.get_json()["code"] == "INVALID_INPUT"
    mock_translator.translate.assert_not_called()


# --- Task 4.2: route wired to Translation Service, responses mapped ---------------

def test_task_4_2_valid_request_returns_200_with_all_four_fields(client):
    response = client.post("/api/translate", json={"text": "Hello world", "targetLanguage": "fr"})

    assert response.status_code == 200
    body = response.get_json()
    assert body["sourceText"] == "Hello world"
    assert body["detectedLanguage"] == "en"
    assert body["translatedText"] == "Bonjour le monde"
    assert body["targetLanguage"] == "fr"


def test_task_4_2_simulated_service_failure_returns_500_with_no_raw_traceback(mock_translator):
    mock_translator.translate.side_effect = RuntimeError("googletrans exploded")
    app = create_app(translator=mock_translator)
    app.testing = True
    client = app.test_client()

    response = client.post("/api/translate", json={"text": "Hello", "targetLanguage": "fr"})

    assert response.status_code == 500
    body = response.get_json()
    assert body["code"] == "TRANSLATION_FAILED"
    assert "Traceback" not in body["message"]
    assert "googletrans exploded" not in body["message"]


# --- Task 4.3: logging never contains request/response text content --------------

def test_task_4_3_success_log_never_contains_text_content(client, caplog):
    with caplog.at_level("INFO", logger="translator"):
        client.post("/api/translate", json={"text": "Hello world", "targetLanguage": "fr"})

    log_output = "\n".join(record.getMessage() for record in caplog.records)
    assert "Hello world" not in log_output
    assert "Bonjour le monde" not in log_output
    assert "status=200" in log_output


def test_task_4_3_error_log_never_contains_text_content(client, caplog):
    with caplog.at_level("INFO", logger="translator"):
        client.post("/api/translate", json={"text": "Secret text", "targetLanguage": ""})

    log_output = "\n".join(record.getMessage() for record in caplog.records)
    assert "Secret text" not in log_output
    assert "status=400" in log_output
    assert "error_code=INVALID_INPUT" in log_output


# --- Task 4.4: full endpoint coverage across all response codes ------------------

def test_task_4_4_full_response_code_matrix(client, mock_translator):
    valid = client.post("/api/translate", json={"text": "Hello", "targetLanguage": "fr"})
    assert valid.status_code == 200

    empty_text = client.post("/api/translate", json={"text": "", "targetLanguage": "fr"})
    assert empty_text.status_code == 400

    missing_target = client.post("/api/translate", json={"text": "Hello"})
    assert missing_target.status_code == 400

    oversized = client.post("/api/translate", json={"text": "a" * 5001, "targetLanguage": "fr"})
    assert oversized.status_code == 400

    mock_translator.translate.side_effect = RuntimeError("boom")
    service_failure = client.post("/api/translate", json={"text": "Hello", "targetLanguage": "fr"})
    assert service_failure.status_code == 500
