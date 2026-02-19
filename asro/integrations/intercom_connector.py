from intercom import Intercom

class IntercomIntegration:
    def __init__(self):
        self.intercom = Intercom(
            app_id="your_intercom_app_id",
            secret_key="your_intercom_secret_key"
        )
    
    def send_notification(self, user_id: str, message: str) -> bool:
        """Send a notification to a user."""
        try:
            response = self.intercom.conversations.create(
                user_id=user_id,
                type='message',
                message=message
            )
            return True if response['success'] else False
        except Exception as e:
            logging.error(f"Failed to send notification: {str(e)}")
            return False

    def get_user_data(self, user_id: str) -> Dict[str, Any]:
        """Retrieve user data from Intercom."""
        try:
            user = self.intercom.users.find(user_id=user_id)
            return {
                'name': user['name'],
                'email': user['email'],
                'last_activity': user['last_active_at']
            }
        except Exception as e:
            logging.error(f"Failed to retrieve user data: {str(e)}")
            return {'error': True}