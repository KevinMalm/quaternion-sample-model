from __future__ import annotations

_THRESHOLD = 0.5


class QuaternionSampleModelModel:

    model = None

    def __init__(self, model):
        super().__init__()
        self.model = model

    @staticmethod
    def constant(tag: str) -> str | None:
        if tag == "THRESHOLD":
            return _THRESHOLD
        return None

    def format(self, x: str):
        return x**2

    def predict(self, x):
        return 1 if x > _THRESHOLD else 0

    def custom_training(self, training, validation):
        return None

    @staticmethod
    def withModel(model) -> QuaternionSampleModelModel:
        return QuaternionSampleModelModel(model)

    @staticmethod
    def buildModel() -> object:
        return None
