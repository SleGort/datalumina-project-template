# Code to run model inference with trained models 
import joblib

def save_model(model, filename):
    """
    Save a machine learning model to a file using joblib.

    Parameters:
    model: The machine learning model to save.
    filename: The filename where the model should be saved (e.g., "my_model.pkl").
    """
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

def load_model(filename):
    """
    Load a machine learning model from a file using joblib.

    Parameters:
    filename: The filename from which to load the model (e.g., "my_model.pkl").
    
    Returns:
    The loaded machine learning model.
    """
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model
