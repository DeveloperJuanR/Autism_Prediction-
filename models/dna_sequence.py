from app import db

class DNASequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sequence = db.Column(db.Text, nullable=False)
    evaluation = db.Column(db.String(20), nullable=True)
    responses = db.Column(db.JSON, nullable=True)  # Store Y/N answers as a JSON object

