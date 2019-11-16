import os
from flask import Flask, render_template
from flask_cors import CORS

template_dir = os.path.abspath('./src')
print(template_dir)

app = Flask(__name__, template_folder = template_dir, static_url_path = '', static_folder = './src/frontend/dist')
CORS(app)

data = 0

@app.route('/')
def index():
  return render_template('frontend/dist/index.html')

@app.route('/admin')
def admin():
  global data
  return render_template('backend/index.html', data = data)

@app.route('/processo')
def processo():
  return render_template('backend/processo.html')

@app.route('/processo/new', methods=['GET', 'POST'])
def new():
  global data
  data = data + 1
  return ''

@app.route('/processo/reset', methods=["GET"])
def reset():
  global data
  data = 0
  return ''

@app.route('/processo/status', methods=["GET"])
def status():
  global data
  return str(data)

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host = '0.0.0.0', port = port, debug = True)
