from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return "AI Study Assistant Backend Running Successfully!"

# AI Assistant Route
@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()

        # Get user question
        question = data.get('question', '').lower()

        # Fake AI Responses
        if "python" in question:
            answer = "Python is a powerful, beginner-friendly programming language used in web development, AI, data science, and more."

        elif "html" in question:
            answer = "HTML stands for HyperText Markup Language and is used to structure web pages."

        elif "css" in question:
            answer = "CSS is used to style and design web pages."

        elif "javascript" in question:
            answer = "JavaScript is used to make websites interactive and dynamic."

        elif "react" in question:
            answer = "React is a JavaScript library used for building modern user interfaces."

        elif "flask" in question:
            answer = "Flask is a lightweight Python web framework used for backend development."

        elif "database" in question:
            answer = "A database is used to store, organize, and manage application data."

        elif "sql" in question:
            answer = "SQL is a language used to communicate with relational databases."

        elif "ai" in question:
            answer = "Artificial Intelligence enables machines to simulate human intelligence and decision-making."

        elif "machine learning" in question:
            answer = "Machine Learning is a subset of AI where systems learn from data."

        elif "api" in question:
            answer = "An API allows communication between different software applications."

        elif "node" in question:
            answer = "Node.js is a JavaScript runtime environment used for backend development."

        elif "mongodb" in question:
            answer = "MongoDB is a NoSQL database used to store flexible JSON-like documents."

        else:
            answer = "This is an AI-generated response based on your question."

        return jsonify({
            "success": True,
            "question": question,
            "answer": answer
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)