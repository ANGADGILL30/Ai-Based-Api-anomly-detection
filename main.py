import random
from detector import AnomalyDetector
from Healer import SelfHealer

def main():
    detector = AnomalyDetector()
    healer = SelfHealer()

    # simulate normal traffic
    api_traffic = [random.randint(90, 110) for _ in range(25)]

    # simulate anomaly spike
    api_traffic += [300, 450, 500]

    print("🚀 Starting API Monitoring...\n")

    for value in api_traffic:
        detector.add_metric(value)

        if detector.detect(value):
            print(f"\n🚨 Anomaly detected: {value}")
            healer.handle_traffic_spike()
        else:
            print(f"Normal traffic: {value}")

if __name__ == "__main__":
    main()