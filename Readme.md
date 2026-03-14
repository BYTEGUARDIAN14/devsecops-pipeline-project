# DevSecOps CI/CD Pipeline Project

A beginner-to-intermediate **DevSecOps project** demonstrating how to build a secure CI/CD pipeline using modern DevOps tools.

This project shows how code changes automatically trigger testing, container builds, and vulnerability scanning using GitHub Actions.

---

## Project Overview

This repository demonstrates a **secure CI pipeline** for a simple Flask application.

The pipeline automatically performs:

• Automated testing
• Docker image build
• Container vulnerability scanning

This simulates a **real-world DevSecOps workflow used in modern software teams.**

---

## Architecture

Developer pushes code → GitHub Actions pipeline starts → Tests run → Docker image builds → Security scan runs using Trivy.

Pipeline Flow:

Push Code
↓
Install Dependencies
↓
Run Tests
↓
Build Docker Image
↓
Security Scan (Trivy)

---

## Tech Stack

| Tool           | Purpose                          |
| -------------- | -------------------------------- |
| Python Flask   | Sample web application           |
| Docker         | Containerization                 |
| GitHub Actions | CI/CD pipeline automation        |
| Trivy          | Container vulnerability scanning |
| Pytest         | Automated testing                |

---

## Project Structure

```
devsecops-pipeline-project
│
├── app
│   ├── app.py
│   └── requirements.txt
│
├── tests
│   └── test_app.py
│
├── Dockerfile
│
└── .github
    └── workflows
        └── pipeline.yml
```

---

## Application

The application is a minimal Flask web server.

Endpoint:

```
GET /
```

Response:

```
DevSecOps Pipeline Working!
```

---

## Running the Application Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/devsecops-pipeline-project.git
cd devsecops-pipeline-project
```

### 2. Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r app/requirements.txt
```

### 4. Run the application

```
python app/app.py
```

Open in browser:

```
http://localhost:5000
```

---

## Running with Docker

Build the container image:

```
docker build -t devsecops-demo .
```

Run the container:

```
docker run -p 5000:5000 devsecops-demo
```

Open:

```
http://localhost:5000
```

---

## CI/CD Pipeline

The CI pipeline is implemented using **GitHub Actions**.

Pipeline triggers automatically when code is pushed to the `main` branch.

Pipeline stages:

1. Checkout repository
2. Setup Python environment
3. Install dependencies
4. Run automated tests
5. Build Docker container
6. Scan container vulnerabilities using Trivy

---

## Security Scanning

Container images are scanned using **Trivy**.

The scan checks for:

• OS vulnerabilities
• vulnerable dependencies
• outdated packages

This demonstrates **DevSecOps security integration in CI pipelines.**

---

## Key DevOps Concepts Demonstrated

• Continuous Integration (CI)
• Containerization with Docker
• Automated testing in pipelines
• Security scanning in CI/CD
• Infrastructure automation using GitHub Actions

---

## Future Improvements

Possible improvements for this project:

• Push Docker images to Docker Hub automatically
• Deploy containers to Kubernetes
• Add SonarQube for code quality scanning
• Add dependency vulnerability scanning
• Add monitoring using Prometheus and Grafana

---

## Author

Mohamed Adhnaan J M

GitHub: https://github.com/BYTEGUARDIAN14
