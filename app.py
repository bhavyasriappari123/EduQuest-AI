from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():

    notes = request.form['notes']

    prompt = f"""
    Read the following notes and generate:

    1. Five MCQs
    2. Five 10-mark questions
    3. A 3-day study plan

    Notes:
    {notes}
    """

    response = model.generate_content(prompt)

    return f"<pre>{response.text}</pre>"

if __name__ == "__main__":
    app.run(debug=True)