import datetime

from flask import Blueprint, request, render_template
from models.dna_sequence import DNASequence
from models.user import User
from data.questions import questions
import papermill as pm
from extensions import db

bp = Blueprint('dna', __name__, url_prefix='/dna')

@bp.route('/submit', methods=['POST'])
def submit_sequence():
    # Build question: answer pairs from the form
    responses = {
        question: request.form.get(f"q{i}")
        for i, question in enumerate(questions, start=1)
    }

    # Get the DNA input
    dna_value = request.form.get('dna')

    # Get user information from the form
    name = request.form.get('name')
    age_str = request.form.get('age', '').strip()
    try:
        age = int(age_str)
        if age < 0: raise ValueError("Age cannot be negative")
    except ValueError: age = 0
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Try to find an existing user with the provided email
    user = User.query.filter_by(email=email).first()
    if not user:
        # Create a new user if none exists.
        user = User( name=name, age=age, gender=gender, email=email )
        db.session.add(user)
        db.session.flush()  # Flush to assign an ID to the new user

    new_seq = DNASequence(
        user_id=user.user_id,
        sequence=dna_value,
        evaluation="Pending review",
        responses=responses
    )
    db.session.add(new_seq)
    db.session.commit()


    # Build parameters for notebook analysis from the form data
    analysis_params = {
        'user_email': email,
        'dna_sequence': dna_value,
        'responses': responses
    }

    # Define paths to the input and output notebooks
    input_nb = 'AutismProteinAnalysisBioinformatics.ipynb'
    output_nb = f"executed_analysis_{user.user_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.ipynb"

    try:
        # Run the notebook with Papermill using the parameters
        pm.execute_notebook(
            input_path=input_nb,
            output_path=output_nb,
            parameters=analysis_params
        )
    except Exception as e:
        print("Error running analysis notebook:", e)
        return render_template('response.html', message="Analysis failed", responses=responses)

    # Extract output parameters from the executed notebook
    output_params = extract_output_parameters(output_nb)


    message = "Thank you for your responses! Your data has been saved."
    return render_template('response.html', message=message, responses=responses)


@bp.route('/all', methods=['GET'])
def get_all_sequences():
    sequences = DNASequence.query.all()
    return render_template('all_sequences.html', sequences=sequences)