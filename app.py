from flask import Flask, render_template
from config import Config
from data.questions import questions
from extensions import db

app = Flask(__name__)

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
    print(app.url_map)  # This will list all the registered routes.
    app.run(debug=True)
