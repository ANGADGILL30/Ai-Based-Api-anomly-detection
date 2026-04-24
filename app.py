from flask import Flask, render_template
import random
from detector import AnomalyDetector
from Healer import SelfHealer

app = Flask(__name__)

@app.route("/")
def home():
    detector = AnomalyDetector(window_size=5)
    healer = SelfHealer()

    api_traffic = [random.randint(90, 110) for _ in range(10)]
    api_traffic += [300, 450]

    results = []

    for value in api_traffic:
        detector.add_metric(value)

        if detector.detect(value):
            action = "⚡ Rate limiting applied"
            results.append((value, "Anomaly", action))
        else:
            results.append((value, "Normal", "-"))

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)