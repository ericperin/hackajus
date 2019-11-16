import os
from flask import Flask, render_template

template_dir = os.path.abspath('./src')
print(template_dir)

app = Flask(__name__, template_folder = template_dir, static_url_path = '', static_folder = './src/frontend/dist')

@app.route('/')
def index():
  return render_template('frontend/dist/index.html')

@app.route('/admin')
def admin():
  return render_template('backend/index.html')
  
if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host = '0.0.0.0', port = port, debug = True)
