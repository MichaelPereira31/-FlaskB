from flask import render_template, flash
from flask_login import login_user
from app import app, db

from app.models.forms import LoginForm
from app.models.tables import User

'''@app.route("/index")
@app.route("/") #aplicar uma funcao em cima de outra funcao
def index():
    return render_template('index.html')'''

@app.route("/index")
@app.route("/")
def index():
  return render_template("index.html")


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():#validacao
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.data.password:
            login_user(user)
            flash("Logged in.")
        else:
            flash("Invalid login.")
    
    return render_template('login.html',form=form)




@app.route("/testCreate/<info>")
@app.route("/testCreate", defaults={'info': None})
def testCreate(info):
    i = User('Michael','123', 'Michael Pereria', 'michaelpereria@gmail.com')
    db.session.add(i)
    db.session.commit()#salva no banco
    return "ok"

@app.route("/testSelect/<info>")
@app.route("/testSelect", defaults={'info': None})
def testSelect(info):
    r = User.query.filter_by(username="Michael").all()
    print(r)
    return "ok"

@app.route('/testUpgrade/<info>')
@app.route('/testUpgrade', defaults={'info': None})
def testUpgrade(info):
    r = User.query.filter_by(username="Michael").first()
    r.username = 'Pereira'
    db.session.add(r)
    db.session.commit()
    print(r)
    return "ok Upgrade"


'''#recebendo parametro do usuario na tora
@app.route("/test")
# @app.route("/test",defalts={'name': None})
@app.route("/test/<str:name>")
def test(name=None):
    if name:
        return "Olá!, %s" %name
    else:
        return "Olá!"'''
