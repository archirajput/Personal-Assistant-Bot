from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KRY")


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def index():
    session["history"] = []
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction="Your name is Archie. You are a personal assistant created by Archi Rajput, a B.Tech AI & ML student. Always introduce yourself as Archie when asked who you are."
        )
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)