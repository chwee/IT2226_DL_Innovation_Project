(function () {
  const form = document.getElementById("translate-form");
  const textInput = document.getElementById("source-text");
  const targetLanguageSelect = document.getElementById("target-language");
  const translateButton = document.getElementById("translate-button");
  const loadingIndicator = document.getElementById("loading-indicator");
  const validationMessage = document.getElementById("validation-message");
  const errorMessage = document.getElementById("error-message");
  const resultSection = document.getElementById("result-section");
  const resultSourceText = document.getElementById("result-source-text");
  const resultDetectedLanguage = document.getElementById("result-detected-language");
  const resultTranslatedText = document.getElementById("result-translated-text");
  const readAloudButton = document.getElementById("read-aloud-button");
  const readAloudError = document.getElementById("read-aloud-error");

  const API_URL = "/api/translate";
  let lastTranslatedText = "";
  let lastTargetLanguage = "";

  function hasText() {
    return textInput.value.trim().length > 0;
  }

  function updateTranslateButtonState() {
    translateButton.disabled = !hasText();
  }

  function showValidationMessage(message) {
    validationMessage.textContent = message;
    validationMessage.hidden = false;
  }

  function hideValidationMessage() {
    validationMessage.hidden = true;
    validationMessage.textContent = "";
  }

  function hideResult() {
    resultSection.hidden = true;
    readAloudButton.hidden = true;
    hideReadAloudError();
  }

  function showReadAloudError(message) {
    readAloudError.textContent = message;
    readAloudError.hidden = false;
  }

  function hideReadAloudError() {
    readAloudError.hidden = true;
    readAloudError.textContent = "";
  }

  function showError(message) {
    hideResult();
    errorMessage.textContent = message;
    errorMessage.hidden = false;
  }

  function hideError() {
    errorMessage.hidden = true;
    errorMessage.textContent = "";
  }

  function showResult(data) {
    hideError();
    resultSourceText.textContent = data.sourceText;
    resultDetectedLanguage.textContent = data.detectedLanguage;
    resultTranslatedText.textContent = data.translatedText;
    lastTranslatedText = data.translatedText;
    lastTargetLanguage = data.targetLanguage;
    resultSection.hidden = false;

    // Read-aloud is a MUST requirement: the control is always offered
    // after a successful translation. Browser support is feature-detected
    // only at activation time, to show a clear error instead of crashing —
    // never to hide the control itself.
    readAloudButton.hidden = false;
    hideReadAloudError();
  }

  function setLoading(isLoading) {
    translateButton.disabled = isLoading || !hasText();
    loadingIndicator.hidden = !isLoading;
  }

  textInput.addEventListener("input", () => {
    updateTranslateButtonState();
    if (hasText()) {
      hideValidationMessage();
    }
  });

  targetLanguageSelect.addEventListener("change", () => {
    if (targetLanguageSelect.value) {
      hideValidationMessage();
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    hideError();
    hideValidationMessage();

    const text = textInput.value.trim();
    const targetLanguage = targetLanguageSelect.value;

    if (!text) {
      showValidationMessage("Please enter some text to translate.");
      return;
    }

    if (!targetLanguage) {
      showValidationMessage("Please select a target language.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text, targetLanguage: targetLanguage }),
      });

      let data = null;
      try {
        data = await response.json();
      } catch (parseError) {
        showError("The server returned an unexpected response. Please try again.");
        return;
      }

      if (!response.ok) {
        showError((data && data.error && data.error.message) || "Translation failed. Please try again.");
        return;
      }

      showResult(data);
    } catch (networkError) {
      showError("Could not reach the translation server. Check your connection and try again.");
    } finally {
      setLoading(false);
    }
  });

  readAloudButton.addEventListener("click", () => {
    if (!lastTranslatedText) {
      return;
    }

    if (typeof window.speechSynthesis === "undefined" || typeof window.SpeechSynthesisUtterance === "undefined") {
      showReadAloudError("Read-aloud isn't supported in this browser. Try a recent version of Chrome, Edge, Firefox, or Safari.");
      return;
    }

    hideReadAloudError();
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(lastTranslatedText);
    if (lastTargetLanguage) {
      utterance.lang = lastTargetLanguage;
    }
    utterance.onerror = () => {
      showReadAloudError("Couldn't play audio for this language. Your browser may not have a voice installed for it.");
    };
    window.speechSynthesis.speak(utterance);
  });

  updateTranslateButtonState();
})();
