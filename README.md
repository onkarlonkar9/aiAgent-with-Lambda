# 🤖 aiAgent with AWS Lambda, IAM & API Gateway

> 🚀 A fully **serverless AI Agent** powered by **AWS Lambda**, secured with **IAM**, and accessible via **API Gateway** — easily testable through **Postman**.

![GitHub repo size](https://img.shields.io/github/repo-size/onkarlonkar9/aiAgent-with-Lambda?color=blue&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/onkarlonkar9/aiAgent-with-Lambda?color=brightgreen&style=flat-square)
![License](https://img.shields.io/github/license/onkarlonkar9/aiAgent-with-Lambda?color=orange&style=flat-square)
![Stars](https://img.shields.io/github/stars/onkarlonkar9/aiAgent-with-Lambda?style=social)

---

## 🌟 Overview  

**aiAgent-with-Lambda** is a **cloud-native AI agent** built using **AWS Lambda** for compute, **IAM** for security, and **API Gateway** for API exposure.  
It allows you to build, deploy, and test intelligent AI-powered endpoints using **Postman** — all in a serverless, scalable, and secure environment.

---

## 🧠 Key Features  

✅ **Serverless AI Execution** — Deployed via AWS Lambda, scales automatically.  
✅ **Secure IAM Roles** — Controlled access to AWS services.  
✅ **Public REST API via API Gateway** — Trigger your AI agent using HTTP methods.  
✅ **Postman Ready** — Easily test your deployed API endpoints.  
✅ **Lightweight & Fast** — Built in Python with minimal dependencies.  

---

## 🏗️ Architecture Diagram  

┌────────────┐ ┌──────────────┐ ┌──────────────┐
│ Postman │ ─────▶ │ API Gateway │ ─────▶ │ AWS Lambda │
└────────────┘ └──────────────┘ └──────────────┘
│
▼
┌────────────┐
│ IAM Role │
└────────────┘


---

## ⚙️ Tech Stack  

| Component | Description |
|------------|-------------|
| ☁️ **AWS Lambda** | Serverless compute engine |
| 🔐 **AWS IAM** | Role-based access control |
| 🌐 **API Gateway** | REST API endpoint management |
| 🧠 **Python** | Core language for AI logic |
| 🧩 **OpenAI / LangChain (optional)** | For intelligent responses |
| 🧪 **Postman** | API testing & debugging |

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/onkarlonkar9/aiAgent-with-Lambda.git
cd aiAgent-with-Lambda
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Configure AWS

Make sure your AWS CLI is configured:
```bash
aws configure
```

This will:

Create your Lambda function

Set up API Gateway

Assign IAM roles

After deployment, you’ll receive your API endpoint URL, e.g.:

https://abc123xyz.execute-api.ap-south-1.amazonaws.com/dev/agent

🧪 Testing with Postman
1️⃣ Open Postman

Click + New Tab

Select POST method

2️⃣ Enter API Gateway URL

Example:
```bash
https://abc123xyz.execute-api.ap-south-1.amazonaws.com/dev/agent
```

3️⃣ Add Headers
Key	Value
Content-Type	application/json
4️⃣ Add Body (JSON)
```bash
{
  "message": "Hello AI Agent!"
}
```

5️⃣ Send Request

Click Send → You should receive a response from your Lambda AI agent.

✅ Example Response:
```bash

{
  "statusCode": 200,
  "body": {
    "response": "Hello! I am your AI agent running on AWS Lambda."
  }
}
```

