import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

FEATURE_NAMES = [
    "Age", "Sex", "ChestPainType", "RestingBP",
    "Cholesterol", "FastingBS", "RestingECG",
    "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"
]

def train_model():
    data = pd.read_csv("heart.csv")

    encoder = LabelEncoder()
    categorical_cols = [
        "Sex", "ChestPainType", "RestingECG",
        "ExerciseAngina", "ST_Slope"
    ]

    for col in categorical_cols:
        data[col] = encoder.fit_transform(data[col])

    X = data.drop("HeartDisease", axis=1)
    y = data["HeartDisease"]

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)

    return model


def predict_with_confidence(model, patient):
    proba = model.predict_proba(patient)[0]
    prediction = model.predict(patient)[0]
    confidence = round(proba[1] * 100, 2)
    return prediction, confidence


def explain_prediction(model, top_n=5):
    importances = model.feature_importances_
    pairs = list(zip(FEATURE_NAMES, importances))
    pairs.sort(key=lambda x: x[1], reverse=True)
    return pairs[:top_n]
