# requirements.md — Web Translator Application

## Document Information

- **Feature Name**: Web Translator Application
- **Version**: 1.1 (Requirement 3's read-aloud capability upgraded from optional to MUST — see Change Log)
- **Date**: August 11, 2026
- **Author**: Wee Chee Hong
- **Stakeholders**: End users (translator app users), Course instructor (ITI122), Learners implementing the feature

### Change Log
- **2026-08-11 (v1.1)**: Requirement 3's read-aloud capability (AC 3.2, 3.3, 3.5) upgraded from optional/feature-detected to **MUST**. The read-aloud control is now always shown after a successful translation, in every browser; a browser without Web Speech API support must show a clear error on activation rather than hiding or disabling the control. See Requirement 3 below and the corresponding update in `design_app.md`.

## Introduction

Users who need to communicate across languages often don't know what language a piece of text is written in, let alone how to translate it. This feature provides a simple web-based translator: a user pastes or types text, picks the language they want it translated into, and the system automatically figures out what language the text is in and returns the translation — with an option to hear it spoken aloud.

The feature is intentionally scoped as a single-session, stateless tool. There is no user account, no translation history, and no persistence — every request is self-contained: text and target language in, translated result out.

### Feature Summary
A web application that detects the source language of user-entered text and translates it into a user-selected target language, displaying both the original and translated text and offering read-aloud playback of the translation.

### Business Value
Lowers the barrier to cross-language communication for users who don't know the source language of a piece of text (e.g., a message, a label, a snippet from a document) — they can get a usable translation without first identifying the language themselves. As a teaching artifact, it also gives learners a small, complete, two-tier (frontend/backend) system to practice full-stack integration end to end.

### Scope
**In scope:** single text-entry translation, automatic source-language detection, target-language selection, displaying source + translated text, read-aloud of the translated text (required — the control is always offered, not conditional on browser support).

**Out of scope:** user accounts/authentication, translation history or saved translations, file/document upload translation, batch translation of multiple texts, offline translation, editing/correcting translations, support for languages not offered by the translation library.

## Requirements

### Requirement 1: Text Input and Target Language Selection

**User Story:** As a user, I want to enter text and select a target language, so that I can request a translation into the language I need.

#### Acceptance Criteria

1. WHEN the user types or pastes text into the input box THEN the Frontend SHALL enable the translate action only if the input is non-empty.
2. WHEN the user opens the target-language dropdown THEN the Frontend SHALL display the list of supported target languages.
3. IF the user activates translate without having entered any text THEN the Frontend SHALL display a validation message and SHALL NOT send a request to the backend.
4. IF the user activates translate without selecting a target language THEN the Frontend SHALL display a validation message and SHALL NOT send a request to the backend.
5. WHILE a translation request is in progress THEN the Frontend SHALL disable the translate action and SHALL display a loading indicator.

#### Additional Details
- **Priority**: High
- **Complexity**: Low
- **Dependencies**: None
- **Assumptions**: The list of target languages is a fixed set configured in the frontend rather than fetched dynamically.

### Requirement 2: Source Language Detection and Translation

**User Story:** As a user, I want the system to automatically detect the language my text is written in and translate it, so that I don't need to know or specify the source language myself.

#### Acceptance Criteria

1. WHEN the Backend receives a POST request containing text and a target language THEN the Backend SHALL detect the source language of the text.
2. WHEN the source language has been detected THEN the Backend SHALL translate the text into the requested target language.
3. WHEN translation completes successfully THEN the Backend SHALL return the source text, the detected source language, the translated text, and the target language as a single JSON response.
4. IF the request body is missing the text field or the text field is empty THEN the Backend SHALL respond with a 400 error and SHALL NOT attempt translation.
5. IF the request body is missing the target language THEN the Backend SHALL respond with a 400 error and SHALL NOT attempt translation.
6. IF the translation service fails or raises an error THEN the Backend SHALL respond with a 500 error containing a human-readable error message.

#### Additional Details
- **Priority**: High
- **Complexity**: Medium
- **Dependencies**: Requirement 1 (backend receives what the frontend collects)
- **Assumptions**: The translation library used (googletrans) can reliably detect the source language for all text the system is expected to receive; a live internet connection is available to the backend.

### Requirement 3: Displaying Results and Read-Aloud

**User Story:** As a user, I want to see both my original text and the translation, and hear the translation read aloud, so that I can verify and use the result.

#### Acceptance Criteria

1. WHEN the Backend returns a successful translation response THEN the Frontend SHALL display the source text, the detected source language, and the translated text.
2. WHEN a translated result is displayed THEN the Frontend SHALL always show a read-aloud control alongside it, regardless of browser capability (MUST — not conditional on feature detection).
3. WHEN the user activates the read-aloud control in a browser that supports it THEN the Frontend SHALL play back the translated text as speech.
4. IF the Backend returns an error response THEN the Frontend SHALL display an error message to the user instead of a translation result.
5. WHERE the read-aloud feature is unavailable in the user's browser THEN the Frontend SHALL keep the read-aloud control visible and, WHEN the user activates it, SHALL display a clear inline error message explaining that read-aloud is unsupported — rather than hiding the control, disabling it, or failing silently.

#### Additional Details
- **Priority**: High *(upgraded from Medium — read-aloud is now a MUST requirement, see Change Log)*
- **Complexity**: Low
- **Dependencies**: Requirement 2 (results must exist before they can be displayed or read aloud)
- **Assumptions**: Read-aloud is implemented using the browser's built-in speech synthesis capability rather than a server-generated audio file. Because there is no server-side fallback, a browser lacking Web Speech API support cannot actually produce speech — "must" therefore means the control must always be *offered* and any unavailability must be *clearly communicated*, not that speech is guaranteed to play in every browser.

## Non-Functional Requirements

### Performance Requirements
- WHEN a user submits a translation request under normal conditions THEN the Backend SHALL return a response within 3 seconds.
- IF the text input exceeds a reasonable length (e.g., 5,000 characters) THEN the Backend SHALL reject the request with a 400 error rather than attempt a slow or unbounded translation.

### Security Requirements
- WHEN the Backend receives request input THEN the Backend SHALL validate and sanitize the input before processing it.
- WHEN handling requests THEN the Backend SHALL NOT log or persist the content of translated text, to avoid retaining user data unnecessarily.

### Usability Requirements
- WHEN the application is viewed on a mobile-sized screen THEN the Frontend SHALL remain usable (input box, dropdown, and buttons remain accessible without horizontal scrolling).
- IF the read-aloud feature is not supported by the browser THEN the Frontend SHALL keep the control visible and clearly indicate, on activation, that the feature is unavailable — rather than hiding the control or leaving it present-but-broken.

### Reliability Requirements
- IF the Backend is unreachable THEN the Frontend SHALL display a clear connection-error message rather than hanging indefinitely.
- IF the translation library returns an unexpected or malformed result THEN the Backend SHALL catch the failure and respond with a 500 error rather than crashing the server process.

## Constraints and Assumptions

### Technical Constraints
- The backend must use the `googletrans` library, pinned to version `4.0.0-rc1`, due to known breaking issues in other versions.
- The backend is implemented in Python using Flask; the frontend is implemented in plain HTML/JavaScript (no build tooling assumed).
- No database is used — the system is stateless per request.

### Business Constraints
- This is a classroom/teaching exercise with no budget for paid translation APIs; the free `googletrans` library is used instead of a commercial service.
- No timeline constraints beyond the practical session schedule.

### Assumptions
- Users have a working internet connection, since both the translation library and (if browser-based) read-aloud may depend on it.
- Users will primarily submit short-to-medium length text (sentences or short paragraphs), not entire documents.
- The set of target languages offered is limited to those supported by `googletrans`.
- Only one translation request is handled at a time per user session; concurrent multi-user load is out of scope for performance tuning.

## Success Criteria

### Definition of Done
- [ ] All acceptance criteria for Requirements 1–3 are met
- [ ] Non-functional requirements (performance, security, usability, reliability) are satisfied
- [ ] Frontend and backend integrate correctly end to end (request/response contract matches)
- [ ] Manual testing confirms translation, language detection, and read-aloud all work as specified

### Acceptance Metrics
- A submitted translation request returns a result (or a clear error) within 3 seconds under normal conditions.
- Source language is correctly detected for text in at least the languages demonstrated during testing.
- 100% of invalid requests (empty text, missing target language) are rejected with a 400 error rather than silently failing or crashing.

## Glossary

| Term | Definition |
|------|------------|
| Source language | The language the user's original input text is written in, determined automatically by the system. |
| Target language | The language the user selects for the text to be translated into. |
| Detected language | The source language as identified by the translation library's language-detection function. |
| Translation API | The backend's `POST` endpoint that accepts text and a target language and returns a translation. |
| Read-aloud | A feature that converts the translated text to speech so the user can listen to it. |
| googletrans | The Python library used by the backend to perform language detection and translation. |

---

## Requirements Review Checklist (self-check)

- [x] All user stories have clear roles, features, and benefits
- [x] Each requirement has specific acceptance criteria using EARS format
- [x] Non-functional requirements are addressed
- [x] Success criteria are defined and measurable
- [x] Requirements avoid implementation detail where possible (implementation constraints are separated into Constraints section)
- [x] Terminology is consistent and defined in the Glossary
- [x] Requirements are numbered and traceable for use in design.md and tasks.md

---

This document is ready to feed into **Phase 2: Design** — each design decision in `design.md` should be traceable back to a requirement number above (e.g., the API contract for `POST /api/translate` should satisfy Requirement 2's acceptance criteria).
