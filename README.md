# Prices Predictor System 

Welcome to the **Prices Predictor System**! This repository contains an end-to-end Machine Learning pipeline project that I built to predict prices using modern MLOps practices. 

Instead of a basic Jupyter Notebook, this project utilizes a robust architecture incorporating experiment tracking, scalable pipelines, and continuous deployment capabilities.

## 🛠️ Tech Stack

*   **Python:** Core programming language.
*   **ZenML:** To build and orchestrate reproducible machine learning pipelines.
*   **MLflow:** Used as an experiment tracker (recording metrics/parameters) and a model deployer (serving the trained model).
*   **Scikit-Learn & Pandas:** For data manipulation, feature engineering, and model training.

## 📁 Project Structure

*   `data/` & `extracted_data/`: Contains the datasets used for training and testing.
*   `src/`: Modularized source code for data ingestion, splitting, feature engineering, and model creation.
*   `steps/`: ZenML pipeline steps (individual tasks like data loading, training, evaluation).
*   `pipelines/`: ZenML pipelines that stitch together the steps (`training_pipeline.py`, `deployment_pipeline.py`).
*   `analysis/`: Jupyter notebooks and scripts used for Exploratory Data Analysis (EDA).
*   `run_pipeline.py`: The entry point script to execute the training pipeline.
*   `run_deployment.py`: The entry point script to execute the continuous deployment and prediction pipeline.

##  Getting Started

### 1. Set Up the Environment
It is highly recommended to use a virtual environment (Python 3.10 is used here).

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Training Pipeline
To ingest data, train the model, and evaluate it:

```bash
python run_pipeline.py
```
*After running, you can view the tracked experiments in the MLflow UI by running `mlflow ui`.*

### 3. Running Continuous Deployment
To run a pipeline that trains the model, checks if it performs better than the existing one, and deploys it as a local prediction server:

```bash
python run_deployment.py
```

To stop the model prediction service, run:
```bash
python run_deployment.py --stop-service
```

##  Learning Outcomes
Building this system helped me understand how machine learning models transition from experimental notebooks into production-ready software using tools like ZenML and MLflow.
