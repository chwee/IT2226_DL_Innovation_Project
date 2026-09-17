# Worked Example: Applying the Design Thinking Workshop
### Scenario → Empathise → Define → Ideate → Prototype → Test → Solution

This walks through the exact workshop structure from the previous guide, using one realistic scenario from start to finish, so you can see how each phase's deliverable becomes the next phase's starting material.

---

## Starting Scenario (given to the team)

> "Students at a polytechnic frequently miss submission deadlines for practical assignments, even when deadlines are posted on the LMS well in advance."

**Stakeholder to investigate:** Year 2 IT diploma students
**Constraint:** Any solution must work within the existing LMS (no new institutional software purchase)
**Success measure:** Late-submission rate for practical assignments drops measurably next semester

---

## PHASE 1 — EMPATHISE

**Activity carried out:** The team interviews 5 students (mix of consistently on-time and habitually late submitters) and pulls 1 month of LMS access-log data.

### Empathy Map (composite, for "habitually late" student persona — "Wei Jie")

| Says | Thinks |
|---|---|
| "I know the deadline, I just forget to actually start." | "There's always more time — I'll do it this weekend." |
| "The LMS has too many announcements, I stop reading them." | "If it's not on WhatsApp, it doesn't feel real." |

| Does | Feels |
|---|---|
| Opens the LMS mostly to check grades, not announcements | Mild guilt, then panic near the deadline |
| Relies on classmates' group chat to find out deadlines are close | Overwhelmed by juggling 5 modules' separate deadlines |

**Contradiction spotted:** Students say they "know the deadline" but LMS log data shows most late-submitters don't open the assignment page until less than 24 hours before it's due — the deadline is *known* but not *tracked*.

### ✅ Empathy Synthesis Sheet (Deliverable → feeds Phase 2)

- **Verbatim quotes:**
  1. "If it's not on WhatsApp, it doesn't feel real."
  2. "I only open the LMS to check grades."
  3. "I've got five different modules with five different deadline formats — I lose track."
- **Observed behaviors:**
  1. LMS assignment pages are opened <24 hrs before deadline by 68% of late submitters (from log data)
  2. Students cross-check deadlines via peer group chats, not the LMS itself
  3. On-time submitters had personal calendar reminders set up manually
- **Aha contradiction:** Students believe they "know" deadlines, but their LMS behavior shows no active tracking — the failure is in **reminder visibility**, not awareness of the deadline's existence.

---

## PHASE 2 — DEFINE

**Activity:** The team converts the synthesis sheet into needs, then a POV statement.

**Needs extraction:**
- Needs a way to be *reminded through a channel they actually check* (not the LMS itself)
- Needs deadlines *consolidated* across modules instead of scattered

### ✅ Problem Statement Card (Deliverable → feeds Phase 3)

**POV statement:**
> "Year 2 IT diploma students need a way to be reminded of upcoming deadlines through channels they already check daily, because they treat the LMS as a grades-checking tool, not a planning tool — so deadlines they technically 'know about' don't translate into timely action."

**HMW question (selected, 1 of 3 drafted):**
> "How might we get deadline reminders in front of students where they're already paying attention, without requiring new institutional software?"

*(Two runner-up HMWs — "How might we make the LMS itself feel worth checking daily" and "How might we help students plan backward from a deadline" — were parked as secondary, since they required either institutional redesign or heavier behavior change than the constraint allowed.)*

---

## PHASE 3 — IDEATE

**Activity:** Crazy 8s round against the chosen HMW, followed by dot-voting on an Impact/Feasibility grid.

**Ideas generated (sample of the 8):** LMS-to-WhatsApp bot forwarding deadlines; a browser extension nagging on login; peer "deadline buddy" pairing; a shared class calendar; gamified streak-tracking app; SMS reminders; a Telegram bot with countdown pins; printed weekly deadline sheet.

**Shortlist after Impact/Feasibility voting:**

| Concept | One-liner | Impact | Feasibility |
|---|---|---|---|
| **LMS-to-Telegram/WhatsApp bot** | Auto-forwards LMS deadline data into a class group chat students already use daily | High | High (LMS has an export/API; no new software needed) |
| Shared class calendar (Google Calendar feed) | Subscribable calendar auto-populated from LMS deadlines | Medium | High |
| Gamified streak app | Rewards on-time submission with visible streaks | High | Low (requires new app — violates constraint) |

### ✅ Ranked Concept Shortlist (Deliverable → feeds Phase 4)

**Selected concept:** LMS-to-Telegram bot
**Why it beat the runner-up:** The calendar feed still requires students to *check* a calendar (a planning tool), which is the exact behavior the empathy data showed they don't do. The Telegram bot pushes into a channel they already open constantly — it matches the observed behavior rather than asking students to adopt a new one.

---

## PHASE 4 — PROTOTYPE

**Activity:** Since building a real bot integration would take weeks, the team builds a **low-fidelity "Wizard of Oz" prototype**: a real Telegram group where a team member manually posts messages formatted exactly as the bot would, pulling from real upcoming deadlines for one class over one week.

**Riskiest assumption being tested:**
> "Students will actually read and act on a deadline reminder that appears in Telegram, more than they do with the current LMS announcement."

### ✅ Prototype Package (Deliverable → feeds Phase 5)

- **Prototype:** 1-week simulated Telegram bot feed, e.g.:
  > 🔔 *Reminder: ITG202 Practical 1 due in 48 hours (Fri, 11:59 PM). Submit via LMS → [link]*
- **Test Script:**
  1. Add 15 students from one class to the test group
  2. Send reminders at 72h, 24h, and 3h before two real deadlines
  3. Track: Do students react (emoji/reply) to the message? Does the class's late-submission rate for those two deadlines change vs. the module's historical average?
  4. **Pass criteria (set in advance):** Late-submission rate drops by at least 15 percentage points vs. historical average, AND at least 60% of students engage with (react to or click) at least one reminder.
  5. **Fail criteria:** No measurable change in submission timing, or reminders are muted/ignored by most students within 3 days.

---

## PHASE 5 — TEST

**Activity:** Run the 1-week pilot as scripted.

**Results observed:**
- 13 of 15 students reacted to at least one reminder (87% engagement) — exceeds the 60% pass bar
- Late submissions for the two tracked assignments dropped from a historical average of 34% to 11% (a 23-point drop) — exceeds the 15-point pass bar
- Qualitative feedback: "This is the first time I actually saw the deadline before it was too late." / One student muted the group after the first two days but still submitted on time (suggests reminder worked before being muted)
- Unexpected signal: 2 students asked if reminders could also include *what* the practical required, not just the date — a scope insight for a future iteration, not this cycle

**Verdict:** **Validated.** Evidence clearly supports the concept within the tested constraint.

---

## Final Deliverable: Solution Brief

| Section | Content |
|---|---|
| **Scenario** | Students miss practical assignment deadlines despite LMS postings |
| **POV / Problem Statement** | Students treat LMS as a grades tool, not a planning tool; deadlines don't reach them in a channel they actively monitor |
| **Solution** | Automated LMS-to-Telegram bot pushing deadline reminders at 72h/24h/3h intervals into existing class group chats |
| **Evidence** | 87% engagement rate; late-submission rate fell from 34% → 11% over the pilot week |
| **Verdict** | Validated — recommend scaling to full cohort next semester |
| **Next step** | Build the real LMS→Telegram integration (not the manual Wizard-of-Oz version); re-test at full scale; consider a light iteration adding assignment-content summaries per student feedback |

---

## What This Example Demonstrates

Notice how nothing in the final solution was decided upfront — it was *earned* through the chain:

- The **quote-level evidence** in Empathise ("if it's not on WhatsApp it doesn't feel real") directly justified the **POV** in Define.
- The **POV's constraint** (channel they already check) is what eliminated the gamified-app idea in Ideate, despite it scoring high on impact.
- The **prototype's pass/fail bar** was locked in *before* testing, so the team couldn't retroactively spin an ambiguous result as a win.
- The final brief can be read top-to-bottom and traced back to the very first quote — that traceability is the actual point of the methodology, not just "having 5 stages."
