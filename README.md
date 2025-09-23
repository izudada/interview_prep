# 🤖 AI-Powered Interview Coach

An interactive interview practice app built with Streamlit, Gemini API, and Docker.
The app generates role-specific interview questions and provides real-time AI feedback on your answers.
<br>

## ✨ Features

- 🎯 Role-based interview question generation

- 📈 Adjustable difficulty level (Easy, Medium, Hard)

- 💬 Real-time AI feedback on answers

- 📦 Dockerized for easy deployment

- 🔄 Option to run with Gemini API (cloud) or Ollama (local LLM)
<br>

## 🛠️ Tech Stack

- Frontend/UI → Streamlit

- LLM → Google Gemini API
 (default) or Ollama
 (local option)

- Containerization → Docker + Docker Compose

- Language → Python 3.10+
<br>

## 📦 Installation

Clone the repo:
```
git clone https://github.com/izudada/interview_prep.git
cd interview-coach
```

Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
``` 
pip install -r requirements.txt 
```
<br>


## 🔑 Environment Variables

Create a ```.env``` file in the root directory and add:
```
# For Gemini
GEMINI_API_KEY=your_gemini_api_key_here

# For Ollama (optional local model setup)
OLLAMA_HOST=http://localhost:11434
```
<br>

## 🚀 Running Locally

### Option A: Using Gemini (default)
Run the docker container using:
```
make up
```
App will be live at http://localhost:8502

### Option B: Using Ollama (local LLM)
Check into the containerization_branch:
```
git pull
git checkout containerization_branch
```
Then run the docker container using:
```
make up
```
<br>

## 🖥️ Usage
1. Select difficulty level and role in the sidebar.

2. Click Start Interview.

3. Answer questions in the text box.

4. Get personalized feedback in real-time.

5. Reset anytime to start fresh.
<br>

## 🏗️ Architecture

- Streamlit app (UI + logic)

- Gemini API or Ollama (LLM backend)

- Docker (containerization for deployment consistency)
<br>


## 📊 Performance & Scalability

- Gemini API → Google handles scaling; subject to rate limits.

- Ollama (local) → Performance depends on your machine’s CPU/RAM.

- Load testing → You can use Locust
 or ab to simulate 50+ concurrent users.
<br>

## 🔮 Roadmap

- Add voice input/output

- Save interview history

- Export feedback to PDF/CSV

- Multi-user support with database integration
<br>

## 📚 Resources

- [Streamlit Docs](https://docs.streamlit.io)

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)

- [Ollama Docs](https://docs.ollama.com)

- [Docker Docs](https://docs.docker.com)

- [Locust Load Testing](https://docs.locust.io/en/stable)

- [Dataquest - Prompting Large Language Models in Python](https://app.dataquest.io/learning/course/prompting-large-language-models-in-python)
