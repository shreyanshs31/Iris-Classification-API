# Iris Classification API
 A FastAPI-based microservice for real-time Iris flower classification using a trained scikit-learn model. Dockerized for easy deployment.

This project is a **FastAPI-based microservice** for real-time **Iris flower classification** using a trained scikit-learn model. The app is Dockerized for easy deployment and exposes a clean REST API with automatic documentation.

---

## 🚀 Features

- ✅ Real-time prediction for Iris flower species
- ✅ FastAPI-powered REST API with Swagger docs
- ✅ Dockerized for portable and local deployment
- ✅ Model versioning with `joblib`
- ✅ Input validation using Pydantic

---

## 📂 Project Structure
IRIS-CLASSIFICATION-API/
├── main.py # FastAPI application
├── model.py # Model loading and prediction
├── schema.py # Input/output validation with Pydantic
├── iris_model.pkl # Trained scikit-learn model
├── requirements.txt # Dependencies for pip
├── Dockerfile # Build the Docker image
├── .dockerignore # Ignore unnecessary files in Docker
└── README.md # You're reading it

---

## 🧠 Prerequisites

- Python 3.10+ (if running without Docker)
- Docker (for containerized deployment)

---

## 🐳 Run with Docker
🔨 1. Clone this repo
📦 2. Build the Docker image
🚀 3. Run the container
🌐 4. Access the API

---

## 🛠️ Development (Without Docker)

Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies
pip install -r requirements.txt

Run FastAPI server
uvicorn main:app --reload

---

## 🧠 Model Details
Dataset: [Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Model: scikit-learn (e.g. RandomForest, LogisticRegression, etc.)

Serialized with joblib to iris_model.pkl

📝 License
MIT License

