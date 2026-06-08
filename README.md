# welcome_page
A beginner-friendly Flask app for learning how to create and render HTML templates using Jinja2.

## Project Structure

```
.
├── app.py               # Main Flask application
├── templates/           # Jinja2 HTML templates
├── requirements.txt     # Python dependencies
├── welcome_env          # Environment configuration
└── LICENSE              # Project license
```

## What You'll Learn

- How to set up a basic Flask app
- How to create HTML templates in the `templates/` folder
- How to render templates using `render_template()`
- How to pass variables from Python into your templates

## Getting Started

### 1. Set up a virtual environment (recommended)

```bash
python3 -m venv welcome_env
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000`.

## How Templating Works

Flask uses the **Jinja2** templating engine. Templates live in the `templates/` folder and are rendered in `app.py` like this:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='World')
```

Inside your template, you can use the variable like this:

```html
<h1>Hello, {{ name }}!</h1>
```

## Requirements

- Python 3.7+
- Flask (see `requirements.txt`)

## License

See the [LICENSE] file for details.

