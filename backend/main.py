from flask import Flask, request, render_template, url_for, redirect
from pathlib import Path
import json


app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/api', methods=['GET', 'POST'])
def api():
    url = "http://127.0.0.1:8081"
    return redirect(url)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
