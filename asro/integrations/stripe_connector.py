import stripe
from typing import Dict, Any

class StripeIntegration:
    def __init__(self):
        self.stripe = stripe.Stripe(
            api_key="your_stripe_api_key",
            version="2023-10-26"
        )
    
    def get_payment_status(self, subscription_id: str) -> Dict[str, Any]:
        """Get payment status of a subscription."""
        try:
            sub = self.stripe.subscriptions.retrieve(subscription_id)
            return {
                'status': sub['status'],
                'current_period_end': sub['current_period_end']
            }
        except stripe.error.StripeError as e:
            logging.error(f"Stripe API error: {str(e)}")
            return {'status': 'error'}
    
    def trigger_renewal(self, subscription_id: str) -> bool:
        """Attempt to renew a subscription."""
        try:
            self.stripe.subscriptions.reactivate(subscription_id)
            return True
        except stripe.error.StripeError as e:
            logging.error(f"Failed to reactivate subscription {subscription_id}: {str(e)}")
            return False

    def get_usage(self, subscription_id: str) -> Dict[str, Any]:
        """Get usage data for a subscription."""
        try:
            usage = self.stripe.subscriptions.get_usage(subscription_id)
            return {
                'feature1_usage': usage['feature1'],
                'feature2_usage': usage['feature2']
            }
        except stripe.error.StripeError as e:
            logging.error(f"Failed to retrieve usage for {subscription_id}: {str(e)}")
            return {'error': True}