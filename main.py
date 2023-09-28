from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')

@app.route('/about')
def about() -> str: 
    "О нас"
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)