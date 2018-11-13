from flask import Flask, render_template
from models import ActualData, LastData
import config
from exts import db
from common.mysql import mysql_db
from common.time import now_time, now_month, last_month

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
session = mysql_db()


@app.route('/')
def actual():
    date = session.query(ActualData).filter(ActualData.datatime == str(now_time)).first()
    data_list = eval(date.data_list)

    return render_template('now.html', dates=data_list)


@app.route('/nowmoth/')
def nowMonth():
    data_list1 = []
    data_list2 = []
    data = session.query(LastData).filter(LastData.month == str(now_month)).first()
    print(data.data_list)
    for i in range(len(eval(data.data_list))):
        data_dict = eval(eval(data.data_list)[i])
        data_list1.append(data_dict)
    print(data_list1)
    all_data = data_list1[0]
    for k in range(len(data_list1)):
        a = data_list1[k].get('rows')
        data_list2 += a
    print(data_list2)
    return render_template('last.html', datas=data_list2, totle=all_data)

@app.route('/lastmon/')
def lastMonth():
    data_list1 = []
    data_list2 = []
    data = session.query(LastData).filter(LastData.month == str(last_month)).first()
    print(data.data_list)
    for i in range(len(eval(data.data_list))):
        data_dict = eval(eval(data.data_list)[i])
        data_list1.append(data_dict)
    print(data_list1)
    all_data = data_list1[0]
    for k in range(len(data_list1)):
        a = data_list1[k].get('rows')
        data_list2 += a
    print(data_list2)
    return render_template('last.html', datas=data_list2, totle=all_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4398, debug=True)
