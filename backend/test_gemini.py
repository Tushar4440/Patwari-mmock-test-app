import sys
import os
import google.generativeai as genai # Updated import to address FutureWarning
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

try:
    print(f"Testing Gemini API with key starting with: {str(api_key)[:5]}...")
    model = genai.GenerativeModel('gemini-2.5-flash') # Using gemini-1.5-flash for testing
    response = model.generate_content("Hello")
    print("Success! Response:")
    print(response.text)
except Exception as e:
    print("\n--- EXACT ERROR ---")
    import traceback
    traceback.print_exc()
    print("-------------------")
    sys.exit(1)
