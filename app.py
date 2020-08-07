# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from datetime import datetime

# from flask import request

# CHANGE ALL THE PEOPLE NAMES TO ALL THE COUNTRY NAMES !!!!!!!!!!!!!!
# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())


@app.route('/asians')
def asians():
    return render_template('asians.html', time=datetime.now())


@app.route('/asians/chinese')
def asianschinese():
    return render_template('asians/chinese.html', time=datetime.now())


@app.route('/asians/japanese')
def asiansjapanese():
    return render_template('asians/japanese.html', time=datetime.now())


@app.route('/asians/korean')
def asianskorean():
    return render_template('asians/korean.html', time=datetime.now())


@app.route('/asians/malaysian')
def asiansmalaysian():
    return render_template('asians/malaysian.html', time=datetime.now())


@app.route('/asians/indian')
def asiansindian():
    return render_template('asians/indian.html', time=datetime.now())


@app.route('/asians/indonesian')
def asiansindonesian():
    return render_template('asians/indonesian.html', time=datetime.now())


@app.route('/asians/bangladeshis')
def asiansbangladeshis():
    return render_template('asians/bangladeshis.html', time=datetime.now())


@app.route('/asians/thais')
def asiansthais():
    return render_template('asians/thais.html', time=datetime.now())


@app.route('/asians/vietnamese')
def asiansvietnamese():
    return render_template('asians/vietnamese.html', time=datetime.now())


@app.route('/asians/hongkongers')
def asianshongkongers():
    return render_template('asians/hongkongers.html', time=datetime.now())


@app.route('/asians/myanmars')
def asiansmyanmars():
    return render_template('asians/myanmars.html', time=datetime.now())


@app.route('/asians/laotians')
def asianslaotians():
    return render_template('asians/laotians.html', time=datetime.now())


@app.route('/asians/israelis')
def asiansisraelis():
    return render_template('asians/israelis.html', time=datetime.now())


@app.route('/asians/iranians')
def asiansiranians():
    return render_template('asians/iranians.html', time=datetime.now())


@app.route('/asians/taiwanese')
def asianstaiwanese():
    return render_template('asians/taiwanese.html', time=datetime.now())


@app.route('/asians/saudiArabian')
def asianssaudiArabian():
    return render_template('asians/saudiArabian.html', time=datetime.now())


@app.route('/asians/mongolian')
def asiansmongolian():
    return render_template('asians/mongolian.html', time=datetime.now())


@app.route('/asians/bruneian')
def asiansbruneian():
    return render_template('asians/bruneian.html', time=datetime.now())


@app.route('/asians/nepal')
def asiansnepal():
    return render_template('asians/nepal.html', time=datetime.now())


@app.route('/asians/afganistan')
def asiansafganistan():
    return render_template('asians/afganistan.html', time=datetime.now())


@app.route('/asians/sriLanka')
def asianssriLanka():
    return render_template('asians/sriLanka.html', time=datetime.now())


@app.route('/americanIndian')
def americanIndian():
    return render_template('americanIndian.html', time=datetime.now())


@app.route('/pacificIslander')
def pacificIslander():
    return render_template('pacificIslander.html', time=datetime.now())


@app.route('/Hispanic')
def hispanic():
    return render_template('hispanic.html', time=datetime.now())
