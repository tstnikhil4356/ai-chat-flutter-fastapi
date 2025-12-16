# 🤖 AI Chat Application (Flutter + FastAPI + Gemini)

A full-stack AI-powered mobile chat application built using **Flutter**, **FastAPI**, and **Google Gemini LLM**.  
The app allows users to ask questions in natural language and receive intelligent, real-time responses from a Large Language Model.

---

## 📱 Project Overview

This project demonstrates how a real-world AI application is built end-to-end:
- A **Flutter mobile app** for user interaction
- A **FastAPI backend** for handling requests
- Integration with **Google Gemini LLM** for AI-generated responses

The application has been tested on an **Android emulator** as well as a **physical Android device**.

---

## 🧱 Tech Stack

### Frontend
- Flutter  
- Dart  
- HTTP package  

### Backend
- FastAPI  
- Uvicorn  
- Pydantic  

### AI / ML
- Google Gemini LLM  
- Gemini API (Free Tier)  

---

## 🔄 How It Works

1. User enters a message in the Flutter app  
2. Flutter sends a POST request to the FastAPI backend  
3. Backend forwards the prompt to Google Gemini  
4. Gemini generates a response  
5. Backend returns the response as JSON  
6. Flutter displays the response in a chat-style UI  

### Architecture

## 🔄 Application Architecture

- **Flutter Mobile App**
  - Collects user input
  - Sends HTTP requests to backend
  - Displays AI responses in chat UI

- **FastAPI Backend**
  - Receives requests from Flutter
  - Validates input using Pydantic
  - Communicates with Gemini LLM

- **Google Gemini LLM**
  - Processes user prompts
  - Generates intelligent responses
  - Sends output back to backend


---

## 🧪 Features

- Modern chat-style user interface  
- Real-time AI responses  
- Loading indicator while AI is processing  
- REST API-based communication  
- Works on emulator and real Android device  

---

## 🖥️ Project Structure

```text
llm_chat_app/
├── backend/                 # FastAPI backend
│   ├── main.py              # API logic
│   └── requirements.txt     # Backend dependencies
│
├── flutter_app/             # Flutter mobile app
│   ├── lib/
│   │   └── main.dart        # App UI and logic
│   ├── pubspec.yaml         # Flutter dependencies
│   └── android/             # Android platform files
│
└── README.md                # Project documentation

## 🚀 Running the Project Locally

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000

cd flutter_app
flutter pub get
flutter run
