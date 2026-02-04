# Full CI/CD Pipeline Project

This project simulates a real-world ML application lifecycle. You will build a complete Continuous Integration and Continuous Deployment pipeline using GitHub Actions.

## 📂 Project Structure

```
full_cicd_pipeline/
├── src/
│   ├── app.py              # FastAPI application (Model Serving)
│   └── model.py            # Mock model inference
├── tests/
│   ├── test_app.py         # Functional tests for API
│   └── test_model.py       # Unit tests for Model
├── .github/
│   └── workflows/
│       ├── ci.yaml         # Continuous Integration (Tests, Linting)
│       └── cd.yaml         # Continuous Deployment (Docker Build, Push)
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Tasks to Complete

1. **Local Setup**:
   - Install dependencies: `pip install -r requirements.txt`
   - Run the app: `uvicorn src.app:app --reload`
   - Run tests: `pytest tests/`

2. **Dockerization**:
   - Build the image: `docker build -t ml-cicd-app .`
   - Run container: `docker run -p 8000:8000 ml-cicd-app`

3. **CI Pipeline (GitHub Actions)**:
   - Create `.github/workflows/ci.yaml`
   - Configure it to run PyTest and Black on every push.

4. **CD Pipeline**:
   - Create `.github/workflows/cd.yaml`
   - Configure it to build and push Docker image on new tags (e.g., `v1.0`).

## 🧪 Testing

The project uses `pytest`. Run all tests with:

```bash
pytest
```
