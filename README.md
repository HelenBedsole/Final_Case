# Intelligent Scheduling Assistant with n8n, Google Calendar, and Docker

## Executive Summary

### Problem:
Teams and student organizations frequently communicate scheduling changes through informal messages (email, chat, text). These messages must be manually interpreted and translated into calendar updates. When this does not happen reliably, confusion, missed meetings, and coordination breakdowns occur.

### Solution:
This project provides an automated scheduling assistant that interprets natural language instructions and synchronizes them with Google Calendar. The system uses n8n for automation, Google Gemini for intent extraction, Google Sheets for mapping event information, and Docker for reproducible deployment. Users can schedule, update, or remove events simply by sending ordinary English instructions to a webhook endpoint.

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
cd docker
chmod +x run.sh
./run.sh up
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

Webhook Request Example:
```
curl -X POST "http://localhost:5678/webhook-test/schedule" \
     -H "Content-Type: application/json" \
     -d '{"message": "Move the project meeting to 7 pm tomorrow"}'
```
Sample Output:
```
{
  "output": "OK. I have updated the Project meeting to be from 6 PM to 7 PM tomorrow."
}
```


## Generated Outputs/Event Confirmations
![](assets/proof.png)

---
## Design Decisions

- Google Sheets is leveraged as an editable human oversight layer
- Docker ensures portable, consistent execution for grading and future users
- All system steps are observable and testable through logs and webhook responses

---
## Source code
GitHub Repository:
[https://github.com/HelenBedsole/Final_Case]


