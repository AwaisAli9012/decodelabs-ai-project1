# DecoBot — Rule-Based AI Chatbot

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![Internship](https://img.shields.io/badge/DecodeLabs-AI%20Internship-darkgreen?style=flat-square)
![Batch](https://img.shields.io/badge/Batch-2026-orange?style=flat-square)

> A rule-based conversational AI chatbot built from scratch using pure Python.  
> Developed as Project 1 of the DecodeLabs Artificial Intelligence Industrial Training Program.

---

## Overview

This project demonstrates the foundational architecture of AI systems — decision-making through structured logic. Rather than relying on machine learning models, DecoBot uses explicit if-else control flow to process user input and return intelligent responses.

---

## Features

| Feature | Description |
|--------|-------------|
| Greeting Handling | Responds to greetings in English and Urdu |
| AI Knowledge Base | Answers questions on AI, ML, Deep Learning, and Python |
| Exit Commands | Gracefully ends the session on multiple exit phrases |
| Continuous Loop | Keeps running until the user explicitly exits |
| Fallback Response | Handles unknown input without crashing |
| Fun Responses | Jokes and motivational quotes for engagement |

---

## Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11 | Core language |
| Anaconda | Latest | Environment management |
| Git & GitHub | Latest | Version control |
| VS Code | Latest | Code editor |

```
decodelabs-ai-project1/
│
├── chatbot.py        # Core chatbot logic
├── README.md         # Project documentation
└── .gitignore        # Git ignored files
```

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/AwaisAli9012/decodelabs-ai-project1.git
cd decodelabs-ai-project1

# 2. Create and activate conda environment
conda create -n decodelabs python=3.11
conda activate decodelabs

# 3. Run the chatbot
python chatbot.py
```

```
User Input → Normalize → Match Rule → Return Response → Loop Back
```
## Author

**Awais Ali**
AI Engineering Intern — DecodeLabs | Batch 2026