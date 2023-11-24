
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set your OpenAI GPT-3 API key
openai.api_key = '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'  # Replace with your actual API key

def generate_response(user_input):
    prompt = f"You: {user_input}\nChatGPT:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

@app.route('/endpoint', methods=['POST'])
def get_response():
    try:
        user_input = request.json.get('user_input', '')
        response = generate_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
