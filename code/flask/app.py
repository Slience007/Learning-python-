from flask import request,Flask,render_template
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def Home():
    return render_template("Home.html")
@app.route('/signin',methods=['GET'])
def sign_in():
    return render_template("sign_in.html")
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    if username=="admin" and password=="Huawei@123":
        return  render_template('login_ok.html',username=username)
    return  render_template('sign_in.html',message='username or password wrong',username=username)


if __name__=='__main__':
    app.run(debug=True)
