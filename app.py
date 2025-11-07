from flask import Flask, render_template, request, jsonify
from google import generativeai as ai

app = Flask(__name__)

# Configure your API key here
mykey = "YOUR_API_KEY_HERE"  # Replace with your Gemini API key
ai.configure(api_key=mykey)

model = ai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")
    result = chat.send_message(user_message)
    return jsonify({"reply": result.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
