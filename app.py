from flask import Flask, render_template, request, jsonify
from backend import generate_financial_report, generate_from_text
import os
import tempfile
import pdfplumber
import docx as docx_lib  # Renamed to avoid conflict with local 'docx.py'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate_or_upload', methods=['POST'])
def generate_or_upload():
    query = request.form.get('query', '').strip()
    file = request.files.get('document')
    content = ""

    try:
        if file:
            filename = file.filename.lower()
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                file.save(temp.name)

                if filename.endswith('.pdf'):
                    with pdfplumber.open(temp.name) as pdf:
                        content = "\n".join(page.extract_text() or "" for page in pdf.pages)

                elif filename.endswith('.docx'):
                    doc = docx_lib.Document(temp.name)
                    content = "\n".join(p.text for p in doc.paragraphs)

                elif filename.endswith('.txt'):
                    with open(temp.name, "r", encoding="utf-8") as f:
                        content = f.read()
                else:
                    return jsonify({'error': 'Unsupported file type'})

        if content:
            report = generate_from_text(content)
        elif query:
            report = generate_financial_report(query)
        else:
            return jsonify({'error': 'Please enter a query or upload a document'})

        return jsonify({'report': report})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
