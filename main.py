import os
from flask import Flask, render_template

template_dir = os.path.abspath('./src/frontend')
print(template_dir)

app = Flask(__name__, template_folder = template_dir)

@app.route('/')
def index():
  return render_template('index.html')
  
if __name__ == '__main__':
  app.run(debug=True)
