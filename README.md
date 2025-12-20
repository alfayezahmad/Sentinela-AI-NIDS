# 🛡️ Sentinela AI: Real-Time Network Forensics Engine

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-macOS%20ARM64%20(Optimized)-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
**Sentinela** is a lightweight, AI-powered Network Intrusion Detection System (NIDS) designed for real-time traffic analysis. 

Built during a 48-hour intensive engineering sprint, this engine bridges low-level packet capture with high-level machine learning. It captures live network traffic, extracts flow-based features (inspired by the **CIC-IDS2017** dataset standards), and classifies packets instantly using a **Random Forest Classifier**.

## 🚀 Key Features
* **Live Packet Sniffing:** Utilizes `Scapy` for raw socket interaction and real-time data acquisition.
* **AI-Powered Detection:** Implements a `Random Forest` model trained on synthetic attack signatures (DoS patterns, Port Scanning).
* **Rich Terminal UI:** Features a professional, live-updating dashboard using the `Rich` library.
* **Apple Silicon Optimization:** Tuned for performance on macOS ARM64 architecture (M4 Pro).
* **Modular Architecture:** strictly separates Model Training (`engine.py`) from Real-Time Inference (`watcher.py`).

## 🛠️ Tech Stack
* **Language:** Python 3
* **Networking:** `Scapy` (Packet manipulation & capture)
* **Machine Learning:** `Scikit-Learn` (Random Forest Classifier), `Pandas` (Dataframing), `Joblib` (Model Serialization)
* **Visualization:** `Rich` (Terminal Dashboard)

## 📂 Project Structure
```bash
Sentinela_Engine/
├── engine.py           # The "Brain": Generates synthetic data & trains the ML model
├── watcher.py          # The "Eye": Captures live traffic & runs inference
├── sentinela_model.pkl # The serialized AI model (Auto-generated)
└── README.md           # Documentation