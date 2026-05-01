import requests

def get_ai_response(user_message):
    """
    Get response from free AI API (no auth required)
    
    Args:
        user_message (str): User's message
    
    Returns:
        str: AI-generated response
    """
    if not user_message:
        return "Please enter a message."
    
    try:
        # Try using Open-WebUI API (if running locally on port 8000)
        # Falls back to a simple rule-based response
        
        # Option 1: Try local Ollama/Open-WebUI API
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "neural-chat", "prompt": user_message, "stream": False},
                timeout=5
            )
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'I couldn\'t generate a response.')
        except:
            pass
        
        # Option 2: Use API Ninjas free endpoint (simple Q&A)
        try:
            response = requests.get(
                "https://api.api-ninjas.com/v1/riddles",
                timeout=5
            )
            if response.status_code == 200:
                result = response.json()
                if result:
                    return f"Here's something interesting: {result[0]['riddle']}"
        except:
            pass
        
        # Fallback: Simple rule-based response
        return generate_simple_response(user_message)
        
    except Exception as e:
        return f"Error: {str(e)}"


def generate_simple_response(message):
    """Generate a simple response based on keywords"""
    message_lower = message.lower()
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What's on your mind?",
        "how are you": "I'm doing well, thanks for asking! How are you?",
        "what's your name": "I'm an AI assistant running on your HomeServer!",
        "who are you": "I'm an AI chat assistant here to help you.",
        "bye": "Goodbye! Feel free to chat anytime.",
        "thanks": "You're welcome!",
        "help": "I can chat with you about various topics. Just type your message!",
    }
    
    # Check for keyword matches
    for keyword, response in responses.items():
        if keyword in message_lower:
            return response
    
    # Default response
    return f"That's interesting! You said: '{message}'. I'm a simple AI, so I might not have all the answers, but I'm here to chat!"

