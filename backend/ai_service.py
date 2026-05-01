import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def generate_mock_test_from_syllabus(syllabus_text, section="full"):
    """
    Calls the real Gemini API to generate questions based on the syllabus.
    """
    # Get the API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("WARNING: GEMINI_API_KEY not found in .env file. API calls will fail.")
        
    genai.configure(api_key=api_key)
    
    # Using Gemini 2.5 Flash as it has much higher free tier rate limits
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    questions = []
    
    # Optimize to make only 1 API call to avoid rate limits
    if section == "full":
        prompt_sections = "General Hindi, General Knowledge, and Uttarakhand GK"
        instructions = "Create exactly 7 highly difficult questions for EACH of the three sections (21 questions total)."
    else:
        prompt_sections = section
        instructions = f"Create exactly 20 highly difficult questions for the '{section}' section."

    prompt = f"""
    You are an expert exam setter for the UKSSSC VDO/Patwari exam. 
    {instructions}
    Base the context on this syllabus info: '{syllabus_text}'.
    
    CRITICAL REQUIREMENT: The actual question "text", all 4 "options", the "correct_answer", and the "explanation" MUST be written entirely in the Hindi language (Devanagari script). This is mandatory because the actual exam is administered in Hindi.
    
    Respond ONLY with a raw JSON array of objects in the following exact format, with NO markdown formatting, NO backticks, and NO extra text. Make sure the "section" field exactly matches one of these in English: {prompt_sections}:
    [
        {{
            "section": "Section Name Here",
            "text": "यहाँ हिंदी में प्रश्न लिखें?",
            "options": ["विकल्प ए", "विकल्प बी", "विकल्प सी", "विकल्प डी"],
            "correct_answer": "विकल्प ए",
            "explanation": "यहाँ हिंदी में विस्तृत व्याख्या लिखें।"
        }}
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        
        # Clean up the response in case the model wraps it in markdown blocks
        response_text = response.text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        elif response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        generated_data = json.loads(response_text.strip())
        
        # Add stringified options for our database compatibility
        for q in generated_data:
            q['options'] = json.dumps(q['options'])
            questions.append(q)
            
    except Exception as e:
        print(f"Failed to generate/parse AI response: {e}")
        # Fallback to a safe question if parsing fails
        questions.append({
            "section": section,
            "text": f"API Error: Failed to generate question. Please check terminal for details.",
            "options": json.dumps(["Error A", "Error B", "Error C", "Error D"]),
            "correct_answer": "Error A",
            "explanation": str(e)
        })
        
    return questions
