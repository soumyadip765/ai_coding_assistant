import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(prompt):
    try:
        # Initialize model
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Generate response
        response = model.generate_content(prompt)

        # Return text output
        return response.text if response.text else "No response generated."

    except Exception as e:
        return f"Error from Gemini API: {e}"