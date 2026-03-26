from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)   # ✅ MUST be before anything

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


@app.route("/")
def home():
    return "AI Agent Running"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    response = model.generate_content(question)

    return jsonify({"answer": response.text})


# ✅ SAFE RUN BLOCK
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
