from flask import Flask, render_template, request
from scraper import fetch_case_data
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import datetime

app = Flask(__name__)
engine = create_engine('sqlite:///db.sqlite3', echo=False)
meta = MetaData()

queries = Table(
    'queries', meta,
    Column('id', Integer, primary_key=True),
    Column('case_type', String),
    Column('case_number', String),
    Column('year', String),
    Column('timestamp', String),
    Column('raw_response', String),
)

meta.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type'].upper()
    case_number = request.form['case_number']
    year = request.form['year']

    data, raw_response = fetch_case_data(case_type, case_number, year)

    with engine.connect() as conn:
        conn.execute(queries.insert().values(
            case_type=case_type,
            case_number=case_number,
            year=year,
            timestamp=str(datetime.datetime.now()),
            raw_response=raw_response[:1000]
        ))

    if data:
        return render_template('result.html', data=data)
    else:
        return render_template('index.html', error="❌ Case not found or unavailable.")

@app.route('/history')
def history():
    with engine.connect() as conn:
        result = conn.execute(queries.select().order_by(queries.c.id.desc()))
        rows = result.fetchall()
    return render_template('history.html', history=rows)

if __name__ == '__main__':
    app.run(debug=True)
