from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
import subprocess
import webbrowser
import json


app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = filename
            file.save(filepath)
            # Process the image using 1.py
            result = subprocess.run(['python', '1.py', filepath], capture_output=True, text=True)
            output_text = result.stdout
            print(output_text)
            output_text = output_text.replace("'", '"')
            try:
            # 尝试解析 JSON
                data = json.loads(output_text)
            except json.JSONDecodeError as e:
                print("JSON 解码错误:", e)
                data = []  # 如果出现错误，就默认为一个空的列表
        else:
        # 如果输出为空或 None，就默认为一个空的列表
            data = []  

        # 使用 data 渲染模板
        return render_template('result.html', text=data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
