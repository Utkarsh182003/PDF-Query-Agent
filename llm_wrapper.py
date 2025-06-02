import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key (and optional base URL) from environment
api_key = os.getenv("GOOGLE_API_KEY")
# base_url = os.getenv("GOOGLE_API_URL")  # Optional if using a custom endpoint

# Configure the Gemini API
genai.configure(
    api_key=api_key,
    # base_url=base_url  # Uncomment if using a custom base URL
)

# Initialize the model once
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating response: {e}"
