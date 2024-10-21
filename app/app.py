import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def index():

    try:
        gemini_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key = gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        data = request.get_json()
        question = data.get("question")
        response = model.generate_content(question)

        return (response.text), 200
    
    except:
        return jsonify({"error" : "Internal error"}), 500

if __name__ == "__main__":
    app.run(debug = True)