# Delivery App

This project is a delivery time prediction application that utilizes a machine learning model to estimate delivery times based on various input features. The application is structured into a backend and a frontend.

## Project Structure

```
delivery-app
├── backend
│   ├── main.py                # FastAPI application for handling predictions
│   ├── gbr_pipeline.pkl       # Serialized machine learning model
│   └── requirements.txt       # Backend dependencies
├── frontend
│   ├── app.py                 # Entry point for the Dash application
│   ├── assets                 # Static assets (CSS, JS, images)
│   └── requirements.txt       # Frontend dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

## Backend

The backend is built using FastAPI and serves as the API for the application. It includes:

- **main.py**: Contains the FastAPI application, loads the machine learning model, defines the data model using Pydantic, and implements the `/predict/` endpoint.
- **gbr_pipeline.pkl**: The serialized model used for making predictions.
- **requirements.txt**: Lists the required libraries for the backend, including FastAPI, joblib, and pandas.

## Frontend

The frontend is developed using Dash and provides a web interface for users to interact with the backend API. It includes:

- **app.py**: The main file that sets up the layout and callbacks for the Dash application.
- **assets**: A directory for static files such as CSS and JavaScript.
- **requirements.txt**: Lists the required libraries for the frontend, including Dash.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd delivery-app
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```
     uvicorn main:app --reload
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the Dash application:
     ```
     python app.py
     ```

## Usage

Once both the backend and frontend are running, you can access the Dash application in your web browser. Use the provided interface to input delivery features and receive predicted delivery times.

## License

This project is licensed under the MIT License.