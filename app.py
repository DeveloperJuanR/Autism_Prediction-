from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from config import Config
from data.questions import questions

app = Flask(__name__)
db = SQLAlchemy()

def create_app():
    app.config.from_object(Config)
    db.init_app(app)

    from routes.dna import bp as dna_bp
    app.register_blueprint(dna_bp)

    return app

@app.route('/', methods=['GET'])
def index():
    # Pass the questions to the template
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)