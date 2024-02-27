from flask import Flask, render_template
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'src/templates')  # Path to templates folder
print("Current Directory:", current_dir)
print("Template Directory:", template_dir)

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
