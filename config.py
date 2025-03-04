### config.py
HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HUGGING_FACE_API_TOKEN = "hf_youractualapikey"  # Replace with your Hugging Face token
headers = {"Authorization": f"Bearer {HUGGING_FACE_API_TOKEN}"}