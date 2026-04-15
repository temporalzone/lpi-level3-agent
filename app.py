from flask import Flask, render_template, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query_agent():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        result = run_agent(question)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
