from config import Config as SampleConfig

class Config(SampleConfig):
    # Enable logging for debugging (True for development, False for production)
    LOGGER = True

    # Telegram Bot Token (get from @BotFather)
    API_KEY = "7897047070:AAHpo5Wch-KQ3_dS6QyRUuDLB7OrTql4-70"  # Replace with your real token

    # Your Telegram User ID (to get it, send /id to your bot)
    OWNER_ID = 7178662611  # Replace with your real Telegram user ID (as an integer)

    # List of chat IDs to forward messages **from**
    FROM_CHATS = [-1001203493551]  # Replace with your actual source group/channel/chat IDs

    # List of chat IDs to forward messages **to**
    TO_CHATS = [-1002565975919, -1002667260218, -1002671676345, -1002588974171, -1002344790513, -1002580838888]  # Replace with your actual destination group/channel/chat IDs

    # Webhook settings (optional, only needed if using webhooks like on Render or Heroku)
    WEBHOOK = False
    IP_ADDRESS = "0.0.0.0"  # Use "0.0.0.0" for Heroku or Render deployments
    URL = None              # Optional: public URL to be used for webhooks (e.g., via ngrok or Render)
    PORT = 5000             # Port for webhooks
    CERT_PATH = None        # SSL cert path if needed (mostly unused in basic bot hosting)

    # Number of workers for concurrent updates
    WORKERS = 8
