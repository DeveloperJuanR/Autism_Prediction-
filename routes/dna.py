from flask import Blueprint, request, render_template
from models.dna_sequence import DNASequence
from models.user import User
from data.questions import questions
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

    # Temporary default user (until form collects real data)
    user_email = "anonymous@example.com"
    user_name = "Anonymous"

    user = User.query.filter_by(email=user_email).first()
    if not user:
        user = User(name=user_name, email=user_email)
        db.session.add(user)
        db.session.flush()

    new_seq = DNASequence(
        user_id=user.user_id,
        sequence=dna_value,
        evaluation="Pending review",
        responses=responses
    )
    db.session.add(new_seq)
    db.session.commit()

    message = "Thank you for your responses! Your data has been saved."
    return render_template('response.html', message=message, responses=responses)


@bp.route('/all', methods=['GET'])
def get_all_sequences():
    sequences = DNASequence.query.all()
    return render_template('all_sequences.html', sequences=sequences)