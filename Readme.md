# 🏥 HealthHive AI

An AI-powered personalized healthcare assistant built using **Streamlit**, **Google Gemini**, **Supabase**, **ChromaDB**, and a **Multi-Agent + RAG Architecture**.

HealthHive AI provides personalized recommendations for nutrition, workouts, sleep, and general wellness by combining user health profiles with evidence-based knowledge retrieval.

---

## 🚀 Features

- 🔐 Username & Password Authentication
- 👤 Personalized User Profiles
- 🤖 AI Health Chat Assistant
- 🥗 Nutrition Recommendations
- 💪 Workout Guidance
- 😴 Sleep Recommendations
- 📈 Health Progress Assistance
- 🧠 Daily AI Health Brief
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Chat History
- ☁️ Supabase Database Integration
- 📊 BMI, Calories, Protein & Water Calculations

---

## 🏗️ Architecture

```
                User
                  │
                  ▼
          Manager Agent
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
Nutrition     Workout      Sleep
   Agent         Agent       Agent
     │            │            │
     └────────────┼────────────┘
                  │
                  ▼
             RAG Agent
                  │
          ChromaDB Vector DB
                  │
                  ▼
            Google Gemini
                  │
                  ▼
             Final Response
```

---

## 🧠 AI Agents

### 🥗 Nutrition Agent
Provides diet plans, calorie guidance, protein intake, and healthy eating recommendations.

### 💪 Workout Agent
Generates workout plans based on fitness goals and activity level.

### 😴 Sleep Agent
Offers sleep improvement tips and recovery recommendations.

### 📈 Progress Agent
Tracks user health goals and provides motivational guidance.

### 📚 RAG Agent
Retrieves trusted medical knowledge from a ChromaDB vector database before generating responses.

### 🎯 Manager Agent
Routes user queries to the appropriate specialized agent.

---

## 📚 Retrieval-Augmented Generation (RAG)

HealthHive AI uses RAG to improve response accuracy.

### Workflow

```
User Question
      │
      ▼
ChromaDB Retrieval
      │
      ▼
Relevant Medical Context
      │
      ▼
Google Gemini
      │
      ▼
Evidence-based Answer
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI

- Google Gemini
- LangChain

### Vector Database

- ChromaDB

### Database

- Supabase

### Authentication

- Custom Username & Password Authentication
- bcrypt Password Hashing

### Embeddings

- Sentence Transformers

---

## 📂 Project Structure

```
HealthHiveAI/
│
├── agents/
├── config/
├── data/
│   ├── embeddings/
│   └── pdfs/
├── pages/
├── rag/
├── services/
├── utils/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/HealthHiveAI.git
```

```bash
cd HealthHiveAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

> Add screenshots of:
- Home Page
- Dashboard
- AI Chat
- User Profile
- Daily AI Brief

---

## 🎯 Future Enhancements

- AI Memory
- Personalized Health Recommendations
- Health Score
- Dashboard Analytics
- PDF Health Report
- Voice Assistant
- Mobile Application

---

## 👨‍💻 Developer

**Vikas**

Computer Science & Engineering (AI & ML)

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

## 📄 License

This project is developed for educational and portfolio purposes.