from flask import Blueprint, request, jsonify
from utils.ai import get_ai_response

chat_bp = Blueprint('chat', __name__)

CHAT_UI_HTML = """<html>
    <head>
        <title>AI Chat</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }
            #chatbox { height: 400px; border: 1px solid #ccc; overflow-y: auto; padding: 10px; background: #f9f9f9; margin-bottom: 10px; }
            .message { margin: 10px 0; padding: 8px; border-radius: 5px; }
            .user { background: #007bff; color: white; text-align: right; }
            .ai { background: #e9ecef; text-align: left; }
            #input-box { width: 85%; padding: 10px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>💬 AI Chat</h1>
        <div id="chatbox"></div>
        <input type="text" id="input-box" placeholder="Type your message...">
        <button onclick="sendMessage()">Send</button>
        <script>
            async function sendMessage() {
                const input = document.getElementById('input-box');
                const message = input.value.trim();
                if (!message) return;
                
                // Add user message to chat
                const chatbox = document.getElementById('chatbox');
                const userMsg = document.createElement('div');
                userMsg.className = 'message user';
                userMsg.textContent = message;
                chatbox.appendChild(userMsg);
                input.value = '';
                chatbox.scrollTop = chatbox.scrollHeight;
                
                // Get AI response
                try {
                    const response = await fetch('/api/chat', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({message: message})
                    });
                    const data = await response.json();
                    
                    const aiMsg = document.createElement('div');
                    aiMsg.className = 'message ai';
                    aiMsg.textContent = data.response;
                    chatbox.appendChild(aiMsg);
                    chatbox.scrollTop = chatbox.scrollHeight;
                } catch(error) {
                    const errMsg = document.createElement('div');
                    errMsg.className = 'message ai';
                    errMsg.textContent = 'Error: ' + error;
                    chatbox.appendChild(errMsg);
                }
            }
            document.getElementById('input-box').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') sendMessage();
            });
        </script>
    </body>
    </html>"""

@chat_bp.route("/chat")
def chat():
    return CHAT_UI_HTML

@chat_bp.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.json
    user_message = data.get('message', '').strip()
    
    ai_response = get_ai_response(user_message)
    return jsonify({'response': ai_response})
