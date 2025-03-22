from flask import Flask, render_template, request, json

app = Flask(__name__)

# A list of customized questions
questions = [
    "Do you experience challenges with communication and social interactions?",
    "Do you find yourself having very focused or intense interests in specific subjects?",
    "Do you have a sibling who has been diagnosed with Autism Spectrum Disorder (ASD)?",
    "Have you been diagnosed with a genetic or chromosomal condition, such as Fragile X syndrome?",
    "Were your parents older when you were born?",
    "Do you often have trouble understanding if someone is joking or being sarcastic?",
    "Do bright lights or loud noises frequently cause you discomfort?",
    "Did you have frequent temper tantrums or emotional outbursts as a child?",
    "Do you frequently notice small details that others tend to overlook?",
    "Do you find small talk tiring or difficult?"
]

@app.route('/', methods=['GET'])
def index():
    # Pass the questions to the template
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    responses = []
    # Process each question and store responses as an ordered list of dicts
    for i, question in enumerate(questions, start=1):
        answer = request.form.get(f'q{i}')
        responses.append({'question': question, 'answer': answer})
    
    # Append the DNA response separately
    dna_value = request.form.get('dna')
    responses.append({'dna': dna_value})
    
    # Convert responses to JSON with indentation for readability
    json_payload = json.dumps(responses, indent=4)
    
    message = "Thank you for your responses! Your data has been received."
    return render_template('response.html', message=message, json_payload=json_payload)

if __name__ == '__main__':
    app.run(debug=True)