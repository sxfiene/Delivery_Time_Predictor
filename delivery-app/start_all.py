import subprocess
import os
import time

def start_mlflow():
    mlflow_command = [
        "mlflow", "server",
        "--backend-store-uri", "sqlite:///mlflow.db",
        "--default-artifact-root", "./mlruns",
        "--host", "0.0.0.0",
        "--port", "5000"
    ]
    return subprocess.Popen(mlflow_command)

def start_backend():
    backend_command = ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    return subprocess.Popen(backend_command, cwd="./delivery-app/backend")

def start_frontend():
    frontend_command = ["python", "app.py"]
    return subprocess.Popen(frontend_command, cwd="./delivery-app/frontend")

if __name__ == "__main__":
    # Start MLflow server
    mlflow_process = start_mlflow()
    time.sleep(5)  # Give MLflow server time to start

    # Start backend
    backend_process = start_backend()
    time.sleep(5)  # Give backend time to start

    # Start frontend
    frontend_process = start_frontend()

    # Wait for all processes to complete
    mlflow_process.wait()
    backend_process.wait()
    frontend_process.wait()