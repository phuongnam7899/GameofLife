from flask import Flask,render_template,request,redirect,session,url_for
import mlab
from models.activities import Activities
from models.user import User
from models.habbit import Habbit

mlab.connect()

app = Flask(__name__)
app.config["SECRET_KEY"] = "qazqwsxcedcyhntyu"


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = request.form
        name = form["name"]
        age = form["age"]
        city = form["city"]
        mail = form["mail"]
        usn = form["username"]
        pw = form["password"]
        cf_pw = form["cf_password"]
        exist_user = User.objects(username=usn).first()
        if exist_user != None:
            return "Tên đăng nhập đã tồn tại"
        elif cf_pw != pw :
            return "Mật khẩu nhập lại không chính xác"
        else:
            user = User(name=name, age=age, city=city, mail=mail, username=usn, password=pw)
            user.save()
            return "Đăng kí thành công"


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        usn = form["username"]
        pw = form["password"]
        usns = User.objects(username = usn).first()
        if usns == None:
            return "Username is wrong"
        elif usns.password != pw:
            return "Password is wrong"
        else:
            session["token"] = usn
            return "hello"


@app.route("/logout")
def log_out():
    if "token" in session:
        del session["token"]
    return redirect(url_for("login"))

@app.route("/")
def home():
    return render_template("home.html")



if __name__ == '__main__':
  app.run(debug=True)