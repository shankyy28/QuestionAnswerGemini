import os
from flask import Flask
import google.generativeai as genai
from dotenv import load_dotenv, get_key

load_dotenv()

app = Flask(__name__)

@app.route('/')

def index():

    gemini_key = os.getenv("GOOGLE_API_KEY")

    genai.configure(api_key = gemini_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content("Who is Jeff Bezos?")

    return (response.text)

if __name__ == "__main__":
    app.run(debug = True)