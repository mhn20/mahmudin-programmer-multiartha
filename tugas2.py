import os

import openai
from flask import Flask, jsonify, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Set API key OpenAI
openai.api_key = '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'

# Fungsi untuk mengirim prompt ke API ChatGPT


def get_chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

# Route untuk menerima input dan mengirimkan respons dari ChatGPT


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('question', '')

    if not user_input:
        return jsonify({'error': 'Input tidak boleh kosong'}), 400

    response = get_chatgpt_response(user_input)
    return jsonify({'response': response})

# Penanganan error jika API gagal merespons


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Gagal menghubungkan ke API atau terjadi kesalahan jaringan'}), 500


if __name__ == '__main__':
    app.run(debug=True)
