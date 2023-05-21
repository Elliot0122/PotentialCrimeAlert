from flask import Flask, request, render_template, url_for, redirect
from online_crawl import return_dates, return_event_days
from CrimeData import getCrime
from WordCloud import count_categories

app = Flask(__name__, static_url_path='', static_folder='../frontend/flask/static', template_folder='../frontend/flask/template')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/api', methods=['GET', 'POST'])
def api():
    yearStart = request.args.get('yearStart')
    yearEnd = request.args.get('yearEnd')
    monthStart = request.args.get('monthStart')
    monthEnd = request.args.get('monthEnd')
    dayStart = request.args.get('dayStart')
    dayEnd = request.args.get('dayEnd')
    return_event_days(f'{yearStart}/{monthStart}/{dayStart}', f'{yearEnd}/{monthEnd}/{dayEnd}')
    return_dates()
    getCrime(f'{yearEnd}/{str(int(monthEnd)-1)}/{dayEnd}', f'{yearEnd}/{monthEnd}/{dayEnd}')
    count_categories()
    url = "http://127.0.0.1:8081/"

    return redirect(url)

if __name__ == '__main__':
    app.run(port=3000, debug=True)