

# 🚀 Customer Churn Prediction – End-to-End Machine Learning Project

## 📌 Project Overview

This project builds an **end-to-end machine learning pipeline** to predict customer churn. The system analyzes customer transaction behavior and predicts whether a customer is likely to leave the service.

The trained model is deployed as a **REST API using FastAPI**, containerized using **Docker**, and hosted on **AWS EC2** for real-time predictions.

This repository demonstrates a **production-style machine learning workflow**, combining **data science, backend development, and cloud deployment**.

---

# 🎯 Business Problem

Customer churn is a critical problem for many businesses such as telecom, SaaS, and subscription-based platforms.

Losing customers directly impacts revenue. By predicting churn early, businesses can:

* Identify customers at risk
* Offer retention strategies
* Improve customer experience
* Reduce revenue loss

This project predicts churn probability based on customer transaction patterns.

---

# 📊 Dataset Description

**Dataset Source:** Public dataset / Kaggle

### Key Features

| Feature   | Description                            |
| --------- | -------------------------------------- |
| Frequency | Number of purchases made by a customer |
| Monetary  | Total amount spent by the customer     |
| AOV       | Average Order Value                    |

### Target Variable

| Value | Meaning             |
| ----- | ------------------- |
| 0     | Customer will stay  |
| 1     | Customer will churn |

---

# 🛠 Technology Stack

### Programming Language

* Python

### Data Science

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

### Backend

* FastAPI

### Deployment

* Docker
* AWS EC2

---

# 🔄 Project Workflow

## 1️⃣ Data Collection

The dataset was obtained from a publicly available source and loaded using Pandas.

---

## 2️⃣ Data Cleaning

* Removed invalid transactions
* Handled missing values
* Ensured correct data types

---

## 3️⃣ Exploratory Data Analysis

EDA was performed to understand customer behavior.

Key insights included:

* Customer purchase frequency distribution
* Spending patterns
* Correlation between features

Visualization tools:

* Matplotlib
* Seaborn

---

## 4️⃣ Feature Engineering

Important customer behavior features were created:

* Frequency
* Monetary
* Average Order Value (AOV)

These help measure **customer engagement and purchasing behavior**.

---

## 5️⃣ Model Training

Models tested:

* Logistic Regression
* Random Forest

The best model was selected based on evaluation metrics.

---

## 6️⃣ Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

## 7️⃣ Model Deployment

The trained model was deployed using:

```
Machine Learning Model
        ↓
FastAPI REST API
        ↓
Docker Container
        ↓
AWS EC2 Instance
```

This allows real-time prediction through an API.

---

# 🌐 API Deployment

The model is exposed through a REST endpoint.

### Endpoint

```
POST /predict
```

### API Documentation

FastAPI automatically generates Swagger documentation.

Example:

```
http://<EC2_PUBLIC_IP>:8000/docs
```

---

# 📬 Example API Request

```
POST /predict
```

```json
{
 "Frequency": 10,
 "Monetary": 5000,
 "AOV": 50
}
```

---

# 📤 Example API Response

```json
{
 "churn_probability": 0.23,
 "prediction": 0
}
```

### Interpretation

| Prediction | Meaning             |
| ---------- | ------------------- |
| 0          | Customer will stay  |
| 1          | Customer will churn |

---

# 📂 Project Directory Structure

```
churn-api-deployment
│
├── app
│   ├── main.py
│   ├── schema.py
│   └── model_loader.py
│
├── artifacts
│   ├── final_churn_model.joblib
│   ├── scaler.joblib
│   └── threshold.joblib
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository:

```
git clone https://github.com/Rohan1-tech/churn-api-deployment.git
```

Move into project directory:

```
cd churn-api-deployment
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶ Running the Project Locally

Start FastAPI server:

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Running with Docker

Build Docker image:

```
docker build -t churn-api .
```

Run container:

```
docker run -d -p 8000:8000 churn-api
```

Open API documentation:

```
http://localhost:8000/docs
```

---

# ☁ AWS Deployment

The Docker container is deployed on **AWS EC2**.

To start the API again:

1️⃣ Start EC2 instance

2️⃣ Connect to server

3️⃣ Run container

```
sudo docker run -d -p 8000:8000 churn-api
```

4️⃣ Open:

```
http://<EC2_PUBLIC_IP>:8000/docs
```

---

# 📸 Project Screenshots

*(Add screenshots here)*

Example:

* FastAPI Swagger UI
* Prediction request
* Prediction response
* AWS EC2 instance running

---


#  Author

**Rohan Pagare**

📧 Email: [rohanpagare6616@gmail.com](mailto:rohanpagare6616@gmail.com)




💼 LinkedIn: [https://linkedin.com/in/rohan-pagare-1bab0a2a9](https://linkedin.com/in/rohan-pagare-1bab0a2a9)



💻 GitHub: [https://github.com/Rohan1-tech](https://github.com/Rohan1-tech)

