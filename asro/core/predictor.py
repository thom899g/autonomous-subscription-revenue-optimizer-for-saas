import logging
from typing import Dict, Any
import pandas as pd
from sklearn.linear_model import LogisticRegression

class ChurnPredictor:
    def __init__(self):
        self.model = LogisticRegression()
        self.features = ['days_since_last_login', 'failed_payments_count', 
                        'support_tickets_count', 'feature_usage_pct']
    
    def train(self, data: pd.DataFrame) -> None:
        """Train the model using historical customer data."""
        try:
            X = data[self.features]
            y = data['churn']
            self.model.fit(X, y)
            logging.info("Model trained successfully.")
        except Exception as e:
            logging.error(f"Training failed: {str(e)}")
    
    def predict(self, customer_data: Dict[str, Any]) -> float:
        """Predict churn probability for a customer."""
        try:
            # Prepare input features
            X = pd.DataFrame([customer_data])[self.features]
            prediction = self.model.predict_proba(X)[:, 1][0]
            return prediction
        except Exception as e:
            logging.error(f"Prediction failed: {str(e)}")
            return 0.0

    def get_recommendation(self, customer_data: Dict[str, Any]) -> str:
        """Generate action recommendation based on churn prediction."""
        try:
            prob = self.predict(customer_data)
            if prob > 0.3:
                # High risk of churn
                return "offer_discount"
            elif prob > 0.2:
                # Medium risk
                return "upsell_feature"
            else:
                # Low risk
                return "no_action"
        except Exception as e:
            logging.error(f"Recommendation failed: {str(e)}")
            return "no_action"