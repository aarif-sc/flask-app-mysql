from flask import Flask, make_response, request, jsonify
import pandas as pd
from datetime import datetime, time
from flask import Flask, render_template



app = Flask(__name__)


def check_time(start_end, time_value):
    start = datetime.strptime(start_end.split('-')[0], '%H:%M').time()
    end = datetime.strptime(start_end.split('-')[1], '%H:%M').time()
    time_value = datetime.strptime(time_value, '%H:%M').time()
    return start < time_value < end




def check_item_status(item, time_value):
    time_list = item["timestring"].split(',')
    for item_time in time_list:
        if check_time(item_time, time_value):
            return {item["item_name"]: "available"}
    return {item["item_name"]: "not available"}


@app.route('/settime', methods = ['GET'])
def setCookie():
    c_time = request.args.get('time')
    print("c_time-->", c_time)
    response = make_response()
    response.set_cookie('time_id',c_time)
    return response

@app.route('/hello', methods = ['GET'])
def hello_world():
    return "Hello Aarif"

@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')






@app.route('/isitemavailable', methods = ['POST'])
def check_item():
    c_time = request.cookies.get('time_id')
    file = request.files['file']
    data = pd.read_csv(file, quotechar="'")
    item_list = data.to_dict('records')
    item_list_status = list()
    for item in item_list:
        item_list_status.append(check_item_status(item, c_time))
    print("c_time-->", c_time)
    return jsonify(item_list_status)


if __name__=="__main__":
    app.run()
