import requests
from config import HUGGINGFACE_API_URL, HUGGINGFACE_API_TOKEN

def get_ai_response(user_message):
    """
    Get response from HuggingFace AI API
    
    Args:
        user_message (str): User's message
    
    Returns:
        str: AI-generated response
    """
    if not user_message:
        return "Please enter a message."
    
    try:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
        response = requests.post(
            HUGGINGFACE_API_URL,
            json={"inputs": user_message},
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                ai_response = result[0].get('generated_text', 'I couldn\'t generate a response.')
                return ai_response
        
        return "AI service temporarily unavailable. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"
