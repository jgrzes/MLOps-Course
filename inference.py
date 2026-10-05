import joblib


class IrisModel:
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        target_names = ["setosa", "versicolor", "virginica"]

        features = [
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"],
            ]
        ]

        prediction_idx = self.model.predict(features)[0]
        return target_names[int(prediction_idx)]


def load_model(model_path):
    model = joblib.load(model_path)
    return IrisModel(model)
