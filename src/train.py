from data_loader import load_data
from model import get_model

def train_model(data_path: str):
    df = load_data(data_path)
    X = df.drop('target', axis=1)
    y = df['target']

    model = get_model()
    model.fit(X, y)
    print("Model trained.")
