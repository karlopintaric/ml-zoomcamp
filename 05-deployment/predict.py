import pickle

with open("pipeline_v1.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)


def predict(features):
    X = dv.transform([features])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


if __name__ == "__main__":
    sample_features = {
        "lead_source": "paid_ads",
        "number_of_courses_viewed": 2,
        "annual_income": 79276.0,
    }

    prediction = predict(sample_features)
    print(f"Predicted probability: {prediction:.3f}")
