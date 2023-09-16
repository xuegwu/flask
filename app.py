# app.py
from flask import Flask, request, render_template
from translator import translate

app = Flask(__name__)

# 添加静态文件配置
app.static_folder = 'templates/static'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        translated_text = translate(text)
        return render_template('index.html', translated_text=translated_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')