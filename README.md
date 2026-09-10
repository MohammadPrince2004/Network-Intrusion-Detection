# 🛡️ Network Intrusion Detection System (NIDS) API

A High-Performance **FastAPI** application powered by Machine Learning to classify network traffic and detect cyber-attacks in real-time. Built using the benchmark **UNSW-NB15** dataset.

---

## 📌 Project Overview

This project provides a RESTful API service that accepts network flow feature vectors, preprocesses them dynamically (handling categorical encoding, log transformations, and feature alignment), and passes them through a trained Machine Learning model to evaluate whether the connection is **Normal** or an **Attack**, along with a confidence score.

---

## 🛠️ Tech Stack & Dependencies

Below is a detailed breakdown of the libraries and technologies used across the data engineering, machine learning, and API deployment workflows:

### 1. Web & API Framework
* **`FastAPI`**: High-performance, asynchronous web framework used to build the RESTful API endpoints (`/` and `/predict`).
* **`Uvicorn`**: An ASGI web server implementation used to run and serve the FastAPI application in real-time.
* **`Pydantic`**: Data validation and settings management using Python type annotations to define request/response schemas.

### 2. Data Manipulation & Storage
* **`pandas`**: Used for data manipulation, DataFrame structures, categorical feature encoding, and feature alignment during both training and inference.
* **`numpy`**: Provides vector and array computations, specifically used for mathematical operations like logarithmic transformations (`np.log1p`).
* **`pyarrow`**: High-performance columnar data memory library used to efficiently read and parse the Apache Parquet file (`UNSW_NB15_training-set.parquet`).

### 3. Machine Learning & Model Persistence
* **`scikit-learn`**: Core machine learning library used for dataset preprocessing, model evaluation metrics, feature transformations, and classification pipeline execution.
* **`pickle` / `joblib`**: Object serialization modules used to export the trained model from `project.ipynb` and reload it inside `main.py` for inference.

### 4. Interactive Development & Analysis
* **`Jupyter Notebook` (`project.ipynb`)**: Used for Exploratory Data Analysis (EDA), feature engineering experiments, model training, and performance evaluation.

## 📂 Project Structure

```text
├── README.md                        # Project Documentation
├── UNSW_NB15_training-set.parquet   # Training dataset used for EDA & Training
├── main.py                          # FastAPI Application & Inference pipeline
├── project.ipynb                    # Data Analysis & Model Training Notebook
└── model.pkl                        # Pre-trained ML Model (Generated from notebook)
