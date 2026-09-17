# tasks.md — Web Translator Application

## Document Information

- **Feature Name**: Web Translator Application
- **Version**: 2.0 (revised to explicitly apply the Task Planning Guidelines)
- **Date**: August 11, 2026
- **Author**: Wee Chee Hong
- **Related Documents**:
  - Requirements: `requirements_app.md` (v1.1)
  - Design: `design_app.md` (v1.1)

## Implementation Overview

This plan breaks `design_app.md` into implementation tasks for a stateless, two-tier application (Flask backend + plain HTML/JS frontend, no database). Every task below is written per the template's **Task Planning Guidelines**: each has an action-verb title naming its component, an explicit Scope, testable Acceptance Criteria, Dependencies, a size/risk Estimate, and the Testing types it requires — not just a requirement citation. The standard 6-phase structure is scaled to 4 phases, since database and authentication tasks don't apply (out of scope per `requirements_app.md`).

### Implementation Strategy
- Build backend and frontend against the fixed API contract in `design_app.md` (`POST /api/translate`) so each side can be implemented — or LLM-generated — independently and still integrate correctly.
- Isolate the Translation Service behind its `detect_and_translate()` facade before wiring it into the Flask route, so it can be unit-tested without a live network dependency.
- Validate on both sides: client-side for UX, server-side as the actual source of truth.

### Development Approach
- **Testing Strategy**: Lightweight unit + integration tests (`pytest`), plus manual end-to-end verification — scaled to this project's size, not full TDD ceremony.
- **Integration Strategy**: Backend is built and smoke-tested first via direct HTTP calls, then the frontend is connected against the same contract.
- **Deployment Strategy**: Single local/classroom instance; no CI/CD pipeline.

### Change Log
- **2026-08-11**: Requirement 3's read-aloud capability (3.2, 3.3, 3.5) upgraded from optional/feature-detected to **MUST**, now reflected in `requirements_app.md` (v1.1) and `design_app.md` (v1.1) directly. Previously the read-aloud control was hidden entirely in browsers without `window.speechSynthesis`. Now it is always shown after a successful translation; in an unsupported browser, activating it surfaces a clear inline error instead of being absent. See Task 6.2 for the updated scope and acceptance criteria.

---

## Implementation Plan

### Phase 1: Foundation and Setup

- [x] **1. Set up project structure and development environment**
  - **Scope**: Included — `/backend` and `/frontend` directories, `requirements.txt` with `flask` and `googletrans==4.0.0-rc1`, verified install. Excluded — no build tooling, no linting config (not required by `design_app.md`'s technology stack).
  - **Acceptance Criteria**:
    - `flask` and `googletrans==4.0.0-rc1` install cleanly via `pip install -r requirements.txt`
    - `import googletrans` succeeds without version-mismatch errors after running the uninstall/reinstall fix
  - **Dependencies**: None — this is the first task
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: N/A (environment setup, not application logic)
  - **_Requirements: Technical Constraints (requirements_app.md)_**

- [x] **2. Implement TranslationRequest/Response data models and validation** *(Data Layer pattern)*
  - **Scope**: Included — code representations of `TranslationRequest`, `TranslationResponse`, `ErrorResponse` from `design_app.md`; a validation function for text presence, length (≤5,000 chars), and target-language presence. Excluded — no database schema (no persistence in this design).
  - **Acceptance Criteria**:
    - Validation rejects empty/whitespace-only text
    - Validation rejects text over 5,000 characters
    - Validation rejects a missing `targetLanguage`
    - Valid input passes validation with no side effects
  - **Dependencies**: Task 1 (project structure must exist)
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: Unit tests covering each rejection case and the valid-input case
  - **_Requirements: 1.1, 1.3, 1.4, 2.4, 2.5; Performance NFR_**

### Phase 2: Backend Implementation

- [x] **3. Create Translation Service business logic** *(Service Layer pattern)*
  - **Scope**: Included — a `detect_and_translate(text, target_language)` facade wrapping `googletrans`'s detect and translate calls; a `TranslationServiceError` raised on library failure or unexpected result. Excluded — no retry/circuit-breaker logic (not specified as a requirement at this scale).
  - **Acceptance Criteria**:
    - Given valid text and a supported target language, returns detected source language and translated text
    - Given a `googletrans` failure (simulated via mock), raises `TranslationServiceError` rather than propagating the raw library exception
  - **Dependencies**: Task 1 (library installed)
  - **Estimate**: Small–Medium (1 day); Medium risk (external, unofficial library dependency)
  - **Testing**: Unit tests using a mocked `googletrans` client for both the success path and the failure path (no live network call required for these tests)
  - **_Requirements: 2.1, 2.2, 2.6_**

- [x] **4. Implement Translate API endpoint** *(API Layer pattern)*
- [x] **4.1 Add request validation to the POST /api/translate route**
  - **Scope**: Included — parse JSON body into `TranslationRequest`; run Task 2's validation; return `400` with `ErrorResponse` (`code: "INVALID_INPUT"`) on failure. Excluded — no authentication/authorization (out of scope per `requirements_app.md`).
  - **Acceptance Criteria**: Invalid requests (empty text, missing target language, oversized text) receive `400` and never reach the Translation Service
  - **Dependencies**: Task 2 (validation function)
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: Integration tests sending malformed requests and asserting `400` + correct `ErrorResponse` shape
  - **_Requirements: 2.4, 2.5_**

- [x] **4.2 Wire the route to the Translation Service and map responses**
  - **Scope**: Included — call `detect_and_translate()` on valid input; return `200` with `TranslationResponse` on success; catch `TranslationServiceError` and return `500` with `ErrorResponse` (`code: "TRANSLATION_FAILED"`). Excluded — no partial/streaming responses.
  - **Acceptance Criteria**: A valid request returns `200` with all four `TranslationResponse` fields populated; a simulated service failure returns `500` with a human-readable message and no raw stack trace exposed
  - **Dependencies**: Task 3 (Translation Service), Task 4.1 (validation in place)
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: Integration tests for both the success path and the simulated-failure path
  - **_Requirements: 2.1, 2.2, 2.3, 2.6_**

- [x] **4.3 Add backend logging per the design's logging strategy**
  - **Scope**: Included — log HTTP status, error code (if any), and request duration. Excluded — logging of `text` or `translatedText` content, which is explicitly prohibited.
  - **Acceptance Criteria**: Log output never contains request or response body text content, across both success and error paths
  - **Dependencies**: Task 4.2
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: Manual inspection of log output during integration testing to confirm no content leakage
  - **_Requirements: Security NFR_**

- [x] **4.4 Write backend integration tests for the full endpoint**
  - **Scope**: Included — HTTP-level tests against the running Flask app covering all response codes (`200`, `400`, `500`). Excluded — load/performance testing (see Task 7.3 for the project's stance on this).
  - **Acceptance Criteria**: Automated tests pass for: valid request → `200`; empty text → `400`; missing target language → `400`; oversized text → `400`; simulated service failure → `500`
  - **Dependencies**: Tasks 4.1–4.3
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: Integration tests (this task's entire scope); any test relying on a live `googletrans` call is marked tolerant of network flakiness per `design_app.md`
  - **_Requirements: 2.1–2.6; Performance NFR_**

### Phase 3: Frontend Implementation

- [x] **5. Build the translator input form UI** *(UI Layer pattern)*
- [x] **5.1 Create the input form components**
  - **Scope**: Included — text input box, target-language dropdown (fixed list), translate button. Excluded — dynamic language-list fetching (assumption in `requirements_app.md` is a fixed frontend-configured list).
  - **Acceptance Criteria**: Dropdown displays the full supported-language list; input box accepts typed and pasted text
  - **Dependencies**: None (can proceed in parallel with backend work once the API contract is fixed)
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: Component-level manual verification (rendering, dropdown population)
  - **_Requirements: 1.1, 1.2_**

- [x] **5.2 Implement client-side validation and request lifecycle state**
  - **Scope**: Included — enable translate only when text is non-empty; show validation messages for empty text or missing target language without calling the backend; disable the button and show a loading indicator while a request is pending. Excluded — server-side validation logic (that lives in Task 4.1; this is a UX convenience only).
  - **Acceptance Criteria**: Clicking translate with empty text or no target language shows a message and produces zero network calls; the button is disabled and a loading indicator is visible for the duration of a request
  - **Dependencies**: Task 5.1
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: End-to-end manual testing of each validation and loading-state scenario
  - **_Requirements: 1.1, 1.3, 1.4, 1.5_**

- [x] **5.3 Implement the API client call to the backend**
  - **Scope**: Included — `fetch()` call to `POST /api/translate` with a body matching `TranslationRequest` exactly; parsing of `TranslationResponse` or `ErrorResponse`; a distinct handling path for network-level failure (backend unreachable). Excluded — retry logic (not specified as a requirement).
  - **Acceptance Criteria**: A successful call correctly parses all four response fields; an error response is distinguished from a network failure in how it's handled downstream
  - **Dependencies**: Task 5.2; Task 4.4 (backend must be functioning to integrate against)
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: Integration testing against the running backend (both success and induced-error cases)
  - **_Requirements: 2.1, 2.3; Reliability NFR_**

- [x] **6. Build result display and read-aloud UI** *(UI Layer pattern)*
- [x] **6.1 Render translation results and error states**
  - **Scope**: Included — display `sourceText`, `detectedLanguage`, `translatedText` on success; display a clear error message on `ErrorResponse` or network failure, in place of a result. Excluded — persisting or exporting results (out of scope).
  - **Acceptance Criteria**: A successful response renders all three fields correctly; any error condition renders a message and never a stale or partial result
  - **Dependencies**: Task 5.3
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: End-to-end manual testing of the success-display and error-display paths
  - **_Requirements: 3.1, 3.4; Reliability NFR_**

- [x] **6.2 Implement read-aloud via the Web Speech API** *(MUST — upgraded from optional, see Change Log)*
  - **Scope**: Included — read-aloud control is always rendered alongside every successful result (no longer feature-detect-and-hide); `window.speechSynthesis` is still feature-detected internally so the app never crashes, but the control's visibility no longer depends on it; speak `translatedText` via `SpeechSynthesisUtterance` on activation; if the API is unsupported, activation shows a clear inline error message in place of speech. Excluded — server-generated audio (explicitly ruled out in `design_app.md`) — this remains a client-only feature, so "must" means *must always be offered to the user*, not *must work in every browser regardless of API support*.
  - **Acceptance Criteria**: The read-aloud control is present after every successful translation, in every browser, without exception; in a browser supporting the API, activating it produces audible speech of the translated text; in a browser without support, activating it shows a clear, specific error message (never silent failure, never a JS exception, never a hidden/absent control)
  - **Dependencies**: Task 6.1
  - **Estimate**: Small–Medium (1 day); Medium risk (browser API support varies)
  - **Testing**: Manual end-to-end testing in at least one supporting and one non-supporting (or simulated non-supporting) browser environment
  - **_Requirements: 3.2, 3.3, 3.5 (now MUST, not optional — see Change Log); Usability NFR_**

- [x] **6.3 Verify responsive/mobile usability**
  - **Scope**: Included — confirm the input box, dropdown, and buttons remain usable without horizontal scrolling on a mobile-sized viewport. Excluded — a dedicated mobile-first redesign (not required by the NFR wording).
  - **Acceptance Criteria**: All controls are visible and operable at a mobile viewport width without horizontal scroll
  - **Dependencies**: Task 6.1
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: Manual testing at a mobile viewport size (browser dev tools or a physical device)
  - **_Requirements: Usability NFR_**

### Phase 4: Integration and Testing

- [x] **7. Integrate frontend and backend, and validate against requirements** *(Integration pattern)*
- [x] **7.1 Run the frontend against the live backend**
  - **Scope**: Included — start the Flask server, open the frontend, confirm the request payload sent by the frontend matches the `TranslationRequest` shape the backend expects, byte for byte on field names. Excluded — automated contract testing tooling (manual verification is sufficient at this scale).
  - **Acceptance Criteria**: A translation request round-trips successfully with no field-name or type mismatches
  - **Dependencies**: Task 4.4 (backend complete), Task 5.3 (frontend API client complete)
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: Integration (manual, cross-component)
  - **_Requirements: 2.1_**

- [x] **7.2 Execute end-to-end user scenarios**
  - **Scope**: Included — the four scenarios: successful translate + read-aloud; empty-text validation; missing-target-language validation; backend-unreachable error display. Excluded — multi-user concurrent load scenarios (out of scope per `requirements_app.md`).
  - **Acceptance Criteria**: All four scenarios behave exactly as specified in their respective acceptance criteria in `requirements_app.md`
  - **Dependencies**: Task 7.1
  - **Estimate**: Small (< 1 day); Low risk
  - **Testing**: End-to-end manual testing
  - **_Requirements: 1.3, 1.4, 3.1–3.5; Reliability NFR_**

- [x] **7.3 Run the full automated test suite and confirm performance target**
  - **Scope**: Included — run all unit tests (Tasks 2, 3) and integration tests (Tasks 4.4, 5.3); time a handful of sample requests to sanity-check the 3-second response target. Excluded — formal load/stress testing, per `design_app.md`'s Performance Considerations (explicitly scoped out at classroom scale, not silently skipped).
  - **Acceptance Criteria**: All automated tests pass; sampled request/response times are comfortably under 3 seconds under normal conditions
  - **Dependencies**: Task 7.2
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: Full regression run of unit + integration tests; ad hoc performance sampling (not formal load testing)
  - **_Requirements: Performance NFR_**

- [x] **7.4 Traceability check against requirements_app.md**
  - **Scope**: Included — go through every acceptance criterion for Requirements 1–3 and all four NFR categories, and confirm each is demonstrably satisfied by the running application. Excluded — none; this task must cover everything.
  - **Acceptance Criteria**: A completed checklist showing every acceptance criterion in `requirements_app.md` mapped to a passing test or a manually verified behavior; any gap is documented rather than left implicit
  - **Dependencies**: Task 7.3
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: N/A — this task is itself the traceability verification step
  - **_Requirements: All (Requirements 1–3, all NFRs)_**

- [x] **7.5 Final cleanup**
  - **Scope**: Included — remove temporary debug code and any console logging of request/response body content. Excluded — broader refactoring not motivated by a specific defect found in testing.
  - **Acceptance Criteria**: No debug output remains; no log statement anywhere prints `text` or `translatedText` content
  - **Dependencies**: Task 7.4
  - **Estimate**: Small (< half a day); Low risk
  - **Testing**: Manual code review pass
  - **_Requirements: Security NFR_**

---

## Requirements Traceability Summary

| Requirement / NFR | Covered by Task(s) |
|---|---|
| Requirement 1 (Input & Language Selection) | 2, 5.1, 5.2, 7.2 |
| Requirement 2 (Detection & Translation) | 2, 3, 4.1, 4.2, 4.4, 5.3, 7.1 |
| Requirement 3 (Display & Read-Aloud) | 6.1, 6.2, 7.2 |
| Performance NFR | 2, 4.4, 7.3 |
| Security NFR | 4.3, 7.5 |
| Usability NFR | 6.2, 6.3 |
| Reliability NFR | 5.3, 6.1, 7.2 |

Every requirement and NFR from `requirements_app.md` maps to at least one task, and every task maps back to at least one requirement or NFR — satisfying the Requirements Traceability guideline's "ensure all requirements are covered by tasks" and "validate task completion against requirements."

## Testing Integration Summary

| Test Type | Applied In |
|---|---|
| Unit Tests | Tasks 2, 3 |
| Integration Tests | Tasks 4.1, 4.2, 4.4, 5.3, 7.1 |
| End-to-End Tests | Tasks 5.2, 6.1, 6.2, 6.3, 7.2 |
| Performance Tests | Task 7.3 (sampling only — formal load testing intentionally excluded, see Task 7.3 scope) |

---

## Estimation Summary

| Task | Size | Risk |
|------|------|------|
| 1. Project setup | Small | Low |
| 2. Data models & validation | Small | Low |
| 3. Translation Service | Small–Medium | Medium (external library) |
| 4.1–4.4 Backend API | Small each | Low |
| 5.1–5.3 Frontend input & API client | Small each | Low |
| 6.1 Result display | Small | Low |
| 6.2 Read-aloud | Small–Medium | Medium (browser API variance) |
| 6.3 Responsive check | Small | Low |
| 7.1–7.5 Integration & testing | Small each | Low |

No task is classified "Large" or "High risk," consistent with the intentionally small, two-tier, no-database scope defined in `requirements_app.md` and `design_app.md`. The two "Medium" risk items (Translation Service, read-aloud) are both driven by dependency on external/browser behavior outside this project's control, not by internal complexity.

---

This task list is ready for **Phase 4 of the practical: Implementation via LLM Code Generation** — Tasks 3, 4, 5, and 6 should be used directly as source material for backend and frontend code-generation prompts, since each now specifies exact scope, acceptance criteria, and dependencies in addition to the requirement it must satisfy.
