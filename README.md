InsurPredict: FastAPI Insurance Premium Prediction API
A high-performance, containerized API for predicting insurance premiums using a machine learning model, built with FastAPI and Docker.

📖 Table of Contents
About The Project

✨ Features

🛠️ Technology Stack

🚀 Getting Started

Prerequisites

Installation & Setup

🐳 Running with Docker

🔌 API Endpoints

🤝 Contributing

📄 License

🧐 About The Project
InsurPredict provides a fast and reliable way to serve a machine learning model that predicts insurance premiums. It exposes a simple RESTful API that takes applicant data as input and returns an estimated insurance premium.

This project leverages the speed of FastAPI to handle web requests and the portability of Docker for containerization, making it incredibly easy to deploy and scale in any environment.

✨ Features
High Performance: Built on FastAPI, one of the fastest Python web frameworks available.

Asynchronous: Takes full advantage of async/await syntax for non-blocking I/O.

Containerized: Dockerized for easy deployment, scaling, and environment consistency.

Interactive Docs: Automatic, interactive API documentation (Swagger UI & ReDoc) for easy testing.

Easy to Extend: Simple structure to integrate and update your insurance prediction model.

Type Hinting: Modern Python with type hints for robust and maintainable code.

🛠️ Technology Stack
This project is built with the following technologies:

FastAPI: The web framework for building the API.

Uvicorn: The lightning-fast ASGI server.

Docker: For containerization and deployment.

Scikit-learn / Pandas: (or your ML library of choice) For the machine learning model.

Python 3.9+: The programming language used.

🚀 Getting Started
Follow these instructions to get the project running on your local machine.

Prerequisites
Make sure you have the following installed:

Python 3.9 or higher

Docker and Docker Compose

Installation & Setup
Clone the repository:

git clone https://github.com/your-username/insurpredict.git
cd insurpredict

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the dependencies:

pip install -r requirements.txt

Run the application locally:

uvicorn main:app --reload

The application will be available at http://127.0.0.1:8000. You can access the interactive API docs at http://127.0.0.1:8000/docs.

🐳 Running with Docker
The easiest way to run the application is by using Docker.

Build the Docker image:

docker build -t insurpredict .

Run the Docker container:

docker run -p 8000:8000 insurpredict

The application will be running and accessible at http://localhost:8000.

🔌 API Endpoints
The following API endpoints are available:

GET /
Description: A simple health check endpoint to verify that the server is running.

Response:

{
  "message": "Welcome to the Insurance Premium Prediction API!"
}

POST /predict
Description: Endpoint to get an insurance premium prediction based on applicant data.

Request Body: The request body should be a JSON object containing the applicant's features.

{
  "age": 35,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southwest"
}

Response: The response will be a JSON object containing the model's predicted premium.

{
  "predicted_premium": 5420.75
}

Test with curl:

curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "age": 35,
    "sex": "male",
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "southwest"
  }'

🤝 Contributing
Contributions are welcome! Please fork the repository and open a pull request to add features or fix bugs.

Fork the Project

Create your Feature Branch (git checkout -b feature/NewPredictionModel)

Commit your Changes (git commit -m 'Add NewPredictionModel')

Push to the Branch (git push origin feature/NewPredictionModel)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.
