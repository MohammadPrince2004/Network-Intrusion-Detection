# 🛡️ Network Intrusion Detection System (NIDS) API

A High-Performance **FastAPI** application powered by Machine Learning to classify network traffic and detect cyber-attacks in real-time. Built using the benchmark **UNSW-NB15** dataset.

---

## 📌 Project Overview

This project provides a RESTful API service that accepts network flow feature vectors, preprocesses them dynamically (handling categorical encoding, log transformations, and feature alignment), and passes them through a trained Machine Learning model to evaluate whether the connection is **Normal** or an **Attack**, along with a confidence score.

---

## 🛠️ Key Features

* **Real-time Prediction**: Fast inference endpoint powered by `FastAPI`.
* **Automatic Feature Engineering**: On-the-fly logarithmic transformation (`np.log1p`), one-hot encoding, and feature alignment.
* **Confidence Scoring**: Returns prediction probabilities to assess model certainty.
* **Trained on UNSW-NB15**: Leverages state-of-the-art network flow parameters for effective anomaly detection.
* **Interactive API Docs**: Built-in Swagger UI for testing API endpoints seamlessly.

---

## 📂 Project Structure

```text
├── README.md                        # Project Documentation
├── UNSW_NB15_training-set.parquet   # Training dataset used for EDA & Training
├── main.py                          # FastAPI Application & Inference pipeline
├── project.ipynb                    # Data Analysis & Model Training Notebook
└── model.pkl                        # Pre-trained ML Model (Generated from notebook)
