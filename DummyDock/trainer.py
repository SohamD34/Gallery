import pandas as pd
import numpy as np
import argparse
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from utils import log_text
import warnings
warnings.filterwarnings("ignore")

TRAIN_LOG_FILE_PATH = 'logs/training_log.txt'


def train_model(X, y, model_type, model_path):
    
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'tree':
        model = DecisionTreeRegressor()
    elif model_type == 'forest':
        model = RandomForestRegressor()
    
    model.fit(X, y)
    os.makedirs(model_path, exist_ok=True)
    with open(os.path.join(model_path, f'{model_type}.pkl'), 'wb') as f:
        pickle.dump(model, f)
    log_text(TRAIN_LOG_FILE_PATH, f"Model trained and saved to {model_path}")

    train_accuracy = evaluate_model(model, X, y)
    return train_accuracy



def evaluate_model(model, X, y):
    predictions = model.predict(X)
    log_text(TRAIN_LOG_FILE_PATH, f"Predictions: {predictions[:5]}")
    accuracy = accuracy_score(y, predictions)
    return accuracy



def parse_args():
    parser = argparse.ArgumentParser(description="Train a model with given parameters.")
    parser.add_argument('--data_path', type=str, required=True, help='Path to the training data CSV file.')
    parser.add_argument('--model_type', type=str, choices=['linear', 'tree', 'forest'], required=True, help='Type of model to train.')
    parser.add_argument('--model_path', type=str, required=True, help='Path to save the trained model.')
    parser.add_argument('--target', type=str, required=True, help='Target column name in the dataset.')
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()
    
    data = pd.read_csv(args.data_path)
    X = data.drop(columns=[args.target])
    y = data[args.target]
    
    train_acc = train_model(X, y, args.model_type, args.model_path)
    log_text(TRAIN_LOG_FILE_PATH, f"Training accuracy: {train_acc}")

    with open(os.path.join(args.model_path, f'{args.model_type}.pkl'), 'rb') as f:
        model = pickle.load(f)
    
    accuracy = evaluate_model(model, X, y)
    log_text(TRAIN_LOG_FILE_PATH, f"Model accuracy: {accuracy}")

    