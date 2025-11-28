# Intelligent Scheduling Assistant with n8n, Google Calendar, and Docker

## Executive Summary

### Problem:
Teams and student organizations frequently communicate scheduling changes through informal messages (email, chat, text). These messages must be manually interpreted and translated into calendar updates. When this does not happen reliably, confusion, missed meetings, and coordination breakdowns occur.

### Solution:
This project provides an automated scheduling assistant that interprets natural language instructions and synchronizes them with Google Calendar. The system uses n8n for automation, Google Gemini for intent extraction, Google Sheets for mapping event information, and Docker for reproducible deployment. Users can schedule, update, or remove events simply by sending ordinary English instructions to a webhook endpoint.

---

### Why n8n Instead of Alternatives?
n8n was chosen over a custom Flask API because it provides:
- full workflow visibility,
- built-in AI integration,
- open-source deployability inside Docker.

---

## System Overview

### Course Concepts:

- Workflow automation with n8n, including trigger and action nodes
- Prompt engineering with a large language model (Google Gemini)
- Integration with Google services (Sheets + Calendar REST API)
- Docker containerization for deployment reproducibility
- API-driven validation and monitoring via webhook testing

### Architecture Diagram:

![](assets/architecture.png)


### Data / Models / Services:

- NLP intent model extracts: action, event name, date, start time, end time
- Google Sheets: reference table for matching events to calendars
- Google Calendar: source of truth for event data
- Webhook: request/response pipeline for system interaction

---

## One-Command Launch

Pull, configure, and start the scheduling system in a single command:

```bash
#!/bin/bash
docker compose -f docker/docker-compose.yml up -d
echo "n8n is starting. Visit http://localhost:5678"
```

This does the following:
- Starts the n8n workflow environment in Docker
- Loads environment variables from .env
- Exposes local UI at: http://localhost:5678
- Ensures reproducible deployment regardless of OS

---

## How to Run (Local)

### Import Workflow
Inside the n8n dashboard:

- Open http://localhost:5678
- Import workflows/personal-scheduler.json
- Activate Google credentials (Sheets + Calendar)
- Enable the workflow

---

## How to Test the API
To verify the system is reachable and responding:

```bash
python test_client.py
```

---
### Edge Case Handling (Current & Future)

The system currently handles normal scheduling requests well. The following edge cases are identified for future improvement:

| Edge Case | Desired Response |
|-----------|-------------------|
| “Schedule something later” | Ask: “Please provide a specific date and time.” |
| Conflicting event detected | Suggest alternate time slots. |
| Invalid date format | Respond: “I couldn't understand the date. Try YYYY-MM-DD or ‘next Friday at 4pm’.” |
| No message body | Return HTTP 400 with error JSON. |
| Multiple events in one message | Handle one event at a time (future feature). |

These do not break the workflow, but clarifying responses will improve robustness.

--- 

## Generated Outputs/Event Confirmations
![](assets/proof.png)

---
## Design Decisions

- Google Sheets is leveraged as an editable human oversight layer
- Docker ensures portable, consistent execution for grading and future users
- All system steps are observable and testable through logs and webhook responses

### Limitations / Edge Cases
- Workflow assumes valid date/time expressions (“this Friday at 4 pm”).
- Ambiguous messages (“move it later”) are not resolved — future improvement.
- No authentication / rate limiting on webhook — vulnerable to spam requests.
- AI may hallucinate event IDs if Google Calendar returns empty data.

### Security, Privacy & Ethics

- Secrets are protected via `.env` → **no hardcoded credentials**.
- Calendar modifications always require Google OAuth approval.  
- Google Sheets acts as human oversight to prevent unintended changes.

**Future Security Enhancements:**
- Add webhook authentication token
- Add rate limiting to prevent spam requests
- Reduce OAuth scopes to calendar-only access
- Optional “review-only mode” before applying event changes

### Ops / Monitoring
- n8n logs accessible via container logs.
- No automated uptime check / metrics.
- Future work: health endpoint + alerting.

---
## Source code
GitHub Repository:
[https://github.com/HelenBedsole/Final_Case]


