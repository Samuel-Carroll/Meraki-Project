from flask import Blueprint, render_template, redirect, url_for, request, session
import APICommands

views = Blueprint('views', __name__)

# default page
@views.route('/')
def home():
    return render_template("base.html")

# Basic route for login page, with POST and GET enabled. Grabs an example 'nm' variable from the HTML page.
@views.route('/login',methods = ['POST','GET'])
def testLogin():
    if request.method == 'POST':
        # this establishes the API key in the secure cookie
        # which allows us to carry it with us across pages.
        API = request.form['API']
        DATE = request.form['DATE']
        TIME = request.form['TIME']
        # 'key' -> int/str/flt

        # WORKING
        # new APICommand object
        # APICommand.dostuff(APIKEY,DATE,TIME)


        session['API', 'DATE', 'TIME'] = API, DATE, TIME
        print(API)
        return redirect('/user')
        # return redirect(f'/user/{str(user)}')
    else:
        return render_template("login.html")
    if request.method == 'GET':
        return render_template("login.html")


# Working..:

@views.route('/user')
def usermainpage():
    return render_template('mainpage.html')

