# flask-dockerized-microservice
A minimal Flask REST API containerized with Docker, featuring simple endpoints for demonstration and deployment. Includes a lightweight setup with Python 3.9 and Flask, designed as a starter template for building scalable microservices.
\\# Flask Docker REST API

--- 

## 🚀 Features
- Simple REST API built with [Flask](https://flask.palletsprojects.com/).
- Containerized with Docker for easy deployment.
- Example endpoints:
  - `GET /` → Welcome message
  - `POST /echo` → Returns posted JSON

---

## 📂 Project Structure
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build configuration
└── README.md # Project documentation

---

🛠️ Build & Run Locally

If you want to build the image yourself:
Clone this repo:
git clone https://github.com/shreeharsh-ms/flask-dockerized-microservice

cd flask-dockerized-microservice

Build the Docker image:
docker build -t flask-app .

Run the container:
docker run -p 8000:5000 flask-app


📦 Requirements
Python 3.9+
Flask
Docker (latest)
Dependencies are listed in requirements.txt.

🐳 Docker Hub: user1122sh
