"""
Project: Sentinela-AI-NIDS
Author: Alfayez Ahmad
Copyright: (c) 2025 Alfayez Ahmad
License: Apache License 2.0
Description: Real-time Network Forensics Engine.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


def build_model():
    print("[*] Initializing Sentinela Brain Training...")

    # Synthetic dataset based on real-world attack patterns
    # Columns: Packet Size, Protocol (TCP=6, UDP=17), Port
    data = {
        'packet_size': [64, 1500, 60, 54, 1450, 40, 1000, 64, 60, 1500, 22, 0, 1234] * 100,
        'protocol': [17, 6, 17, 6, 6, 6, 6, 1, 17, 6, 6, 6, 17] * 100,
        'dest_port': [53, 443, 53, 80, 443, 22, 80, 0, 53, 443, 22, 0, 9999] * 100,
        'is_attack': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1] * 100
    }

    df = pd.DataFrame(data)
    X = df[['packet_size', 'protocol', 'dest_port']]
    y = df['is_attack']

    # Train the "Forest"
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save it for the live watcher
    joblib.dump(model, 'sentinela_model.pkl')
    print("[+] Brain successfully exported to 'sentinela_model.pkl'")


if __name__ == "__main__":
    build_model()
