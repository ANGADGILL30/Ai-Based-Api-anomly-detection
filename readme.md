AI-Based API Anomaly Detection & Self-Healing System

Introduction

This project is a prototype system that monitors API behavior and detects anomalies in real time.
Instead of relying on fixed thresholds, it analyzes API traffic patterns dynamically to identify unusual activity.

When an anomaly is detected, the system automatically triggers self-healing actions to maintain stability and reduce downtime.

⸻

Features

* Real-time API traffic simulation
* Anomaly detection using statistical analysis (mean + standard deviation)
* Detects sudden spikes and abnormal usage patterns
* Automatic self-healing actions:
    * Rate limiting
    * Fallback switching
    * Service isolation
* Simple Flask-based web dashboard for visualization

⸻

Tech Stack

* Python
* Flask
* NumPy

⸻

How to Run

pip install -r requirements.txt
python3 app.py


API Endpoint

GET

Displays API monitoring dashboard with anomaly detection results