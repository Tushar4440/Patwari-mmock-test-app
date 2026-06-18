import json
import os
import google.generativeai as genai # Updated import to address FutureWarning
from dotenv import load_dotenv
import random

# Load environment variables from the .env file
load_dotenv()

def generate_mock_test_from_syllabus(syllabus_text, section="full", num_questions_per_section=5):
    """
    Calls the real Gemini API to generate questions based on the syllabus.
    """
    # Get the API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("WARNING: GEMINI_API_KEY not found in .env file. API calls will fail.")
        
    genai.configure(api_key=api_key)

    # Using Gemini 1.5 Flash as it is stable and fast for generative tasks
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    questions = []
    
    # Dynamically set instructions based on num_questions_per_section
    if section == "full":
        prompt_sections = "General Hindi, General Knowledge, and Uttarakhand GK"
        instructions = f"Create exactly {num_questions_per_section} highly difficult questions for EACH of the three sections ({num_questions_per_section * 3} questions total)."
    else:
        prompt_sections = section
        instructions = f"Create exactly {num_questions_per_section} highly difficult questions for the '{section}' section."

    prompt = f"""
    You are an expert exam setter for the UKSSSC VDO/Patwari exam. 
    {instructions}
    Base the context on this syllabus info: '{syllabus_text}'.
    
    CRITICAL REQUIREMENT: Generate the question text and explanation in BOTH Hindi (Devanagari) and English, strictly adhering to the style and content of the provided B.S. Negi examples.
    Options should be in the format: "Hindi Text / English Text".
    
    Respond ONLY with a raw JSON array of objects in the following exact format, with NO markdown formatting, NO backticks, and NO extra text. Make sure the "section" field exactly matches one of these in English: {prompt_sections}:
    [
        {{
            "section": "Section Name Here",
            "text_hi": "यहाँ हिंदी में प्रश्न लिखें?",
            "text_en": "Write the question in English here?",
            "options": ["विकल्प / Option A", "विकल्प / Option B", "विकल्प / Option C", "विकल्प / Option D"],
            "correct_answer": "विकल्प / Option A",
            "explanation_hi": "यहाँ हिंदी में विस्तृत व्याख्या लिखें।",
            "explanation_en": "Write detailed explanation in English here."
        }}
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        
        # More robust cleaning for markdown blocks and extra text
        response_text = response.text.strip()
        
        # Remove markdown code block fences if present
        if response_text.startswith("```json"): # Specific for JSON markdown
            response_text = response_text[len("```json"):].strip()
        elif response_text.startswith("```"): # General markdown
            response_text = response_text[len("```"):].strip()
        if response_text.endswith("```"): # Closing markdown fence
            response_text = response_text[:-len("```")].strip()
            
        # Attempt to extract only the JSON array part
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']')
        if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
            response_text = response_text[start_idx : end_idx + 1]
        else:
            # If a valid JSON array cannot be extracted, raise an error
            raise ValueError(f"AI response did not contain a valid JSON array: {response_text[:200]}...")
            
        generated_data = json.loads(response_text.strip())
        
        # Add stringified options for our database compatibility
        for q in generated_data:
            opts = q.get('options', [])
            random.shuffle(opts) # Shuffle options here
            q['options'] = opts # Return as list of strings
            questions.append(q)
            
    except Exception as e:
        print(f"Failed to generate/parse AI response: {e}")
        # Fallback to a safe question if parsing fails
        questions.append({
            "section": section,
            "text_hi": f"API त्रुटि: प्रश्न बनाने में विफल। कृपया टर्मिनल देखें।",
            "text_en": f"API Error: Failed to generate question. Please check terminal for details.",
            "options": ["Error A", "Error B", "Error C", "Error D"],
            "correct_answer": "Error A",
            "explanation_hi": f"त्रुटि विवरण: {str(e)}",
            "explanation_en": f"Error details: {str(e)}"
        })
        
    return questions
