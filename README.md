# 🚀 LangChain Azure OpenAI Chat Example

This project demonstrates how to connect **LangChain** with **Azure OpenAI** to create a simple interactive command-line chatbot.
Users can type any question, and the model responds using Azure OpenAI’s deployed model.

---

## 📁 Project Structure

```
LangChain/
│
├── connection.py        # Main Python script
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (not committed)
└── README.md            # Project documentation
```

---

## 🧠 Features

- 🔗 LangChain + Azure OpenAI integration
- 💬 Interactive user input via terminal
- 🔐 Secure API key handling using `.env`
- ⚡ Lightweight & beginner-friendly
- ☁️ Azure OpenAI compatible

---

## 🛠️ Prerequisites

- Python 3.9+
- Azure OpenAI resource
- Azure OpenAI deployed model (e.g., gpt-4o, gpt-35-turbo)

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/langchain-azure-chat.git
cd langchain-azure-chat
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
OPENAI_API_KEY=your_api_key_here
OPENAI_API_VERSION=2024-02-15-preview
OPENAI_DEPLOYMENT_NAME=your_deployment_name
```

---

## ▶️ Run the Application

```bash
python connection.py
```

### Example Output
```
Enter your question: What is CrewAI?

Query: What is CrewAI?
Response: CrewAI is an open-source framework for orchestrating collaborative AI agents...
```

---

## 📄 requirements.txt

```txt
langchain
langchain-openai
python-dotenv
```

---

## 🧩 How It Works

1. Loads environment variables
2. Initializes AzureChatOpenAI via LangChain
3. Accepts user input
4. Sends query to Azure OpenAI
5. Prints response

---

## 📜 License

Open-source for learning and development.

---

## 👨‍💻 Author

**Guruprasath Sridhar**
