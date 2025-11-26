# Personal Scheduler Agent (n8n + Gemini + Google Calendar)

## 1) Executive Summary
**Problem:** People send natural language messages about scheduling (create, update, delete). Manually handling these is time-consuming.

**Solution:** A containerized n8n workflow that exposes an HTTP Webhook. It uses Google Gemini to parse intent, checks a Google Sheets event table, and performs calendar operations (create/update/delete) on Google Calendar. The system returns structured JSON confirmations and logs actions.

---

## 2) System Overview

**Course concepts / tools used**
- n8n workflow automation (visual orchestration)
- Large Language Model (Google Gemini) for intent extraction
- Google Sheets as an editable knowledge store (events)
- Google Calendar API for persisting events
- Docker + docker-compose for containerization and reproducible runs

**Architecture diagram**
(Place `assets/architecture.png` here — include screenshot of n8n canvas and a small system diagram)

**Data & services**
- Google Sheets `EventsDB` (sheet: `events`) — contains `event_name,start_time,end_time,location,calendar_id,notes,internal_id`
- Google Calendar account: `primary` calendar used for demonstration
- Gemini API key (stored in `.env`)

---

## 3) How to Run (Local)

1. Copy `.env.example` to `.env` and fill in keys.
2. Start the app (from repo root):
```bash
cd docker
chmod +x run.sh
./run.sh up
# open http://localhost:5678

```

---

## Demonstration Screenshots

### Node Structure
![Node Structure](assets/architecture.png)

### Example Webhook Response
![Webhook Response](assets/output.png)

### Calendar Event Confirmation
![Calendar Event Created](assets/proof.png)


