from flask import Flask, request, jsonify
from resume_parser import extract_text_from_pdf
from nlp_analysis import analyze_resume

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume uploaded'}), 400

    resume_file = request.files['resume']
    resume_text = extract_text_from_pdf(resume_file)
    
    analysis_results = analyze_resume(resume_text)
    return jsonify(analysis_results)

if __name__ == '__main__':
    app.run(debug=True)