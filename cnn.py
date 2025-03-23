import random

def predict_waste(img_path):
    """Simulates waste classification prediction"""
    class_labels = ["Organic", "Recyclable"]
    predicted_class = random.choice(class_labels)
    confidence = round(random.uniform(0.7, 1.0), 2)  # Confidence between 70% and 100%
    return predicted_class, confidence
