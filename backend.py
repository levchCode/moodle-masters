from flask import Flask, json, render_template, request, url_for, redirect
import os
import re
from moodle_functions import *

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60*60
app.secret_key = "S1h7D2jT0"

@app.route("/", methods=["GET"])
def index():
    courses = get_courses_list()
    return render_template('index.html', cs=courses)

@app.route("/course", methods=["GET"])
def course():
    c_id = request.form.get('id')
    course = get_course(c_id)
    return render_template('course.html', c=course)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)