# 🛰️ LLM-Powered Military Intelligence Summarizer with Ethical AI

A secure, cross-platform summarization system built for defense and intelligence operations. This application enables ethical, model-driven summarization of military reports via a web interface and mobile apps, backed by a FastAPI server and PostgreSQL database.

## 🚀 Features

- 📄 Upload military reports (PDF/TXT)
- 🤖 Choose from multiple LLM models to summarize content
- 🧠 Backend filters summaries for ethical concerns (bias, misinformation)
- 📥 Download result as PDF or 📎 generate a shareable link
- 🔒 User history capped at 15 saved summaries
- 🔧 Admin dashboard to approve users and manage model access
- 📲 Cross-platform support (React Web + React Native Mobile Apps)

---

## 👤 User Roles

### Standard Users
- Request access and await approval
- Use approved models to summarize reports
- Request more model access with usage limits
- View and manage summary history (up to 15)

### Admin Users
- Approve/deny user signups
- Assign and revoke model access per user
- Manage model usage limits
- View system logs and user activity

---

## 🧱 Tech Stack

| Layer        | Tech                        |
|--------------|-----------------------------|
| Frontend     | React (Vite) + Tailwind CSS |
| Mobile App   | React Native + Expo         |
| Backend API  | FastAPI (Python)            |
| Database     | PostgreSQL (Supabase/Railway) |
| Auth         | JWT-based                   |
| Storage      | Cloud file storage (TBD)    |
| LLMs         | OpenAI API / HuggingFace    |
| PDF Export   | WeasyPrint / pdfkit         |

---

## 🛠️ Project Structure

```bash
project-root/
├── frontend/            # React web app
├── mobile/              # React Native app (Expo)
├── backend/             # FastAPI server
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── auth/
│   └── main.py
├── docs/                # Architecture, ethics guide, API docs
├── database/            # SQL schema, seed scripts
└── README.md
