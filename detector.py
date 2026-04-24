import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=20):
        self.window_size = window_size
        self.history = []

    def add_metric(self, value):
        self.history.append(value)
        if len(self.history) > self.window_size:
            self.history.pop(0)

    def detect(self, value):
        if len(self.history) < self.window_size:
            return False

        mean = np.mean(self.history)
        std = np.std(self.history)

        if std == 0:
            return False

        return value > mean + 3 * std