from __future__ import print_function
import os
from flask import Flask, render_template, request, session, redirect, url_for,flash
app = Flask(__name__)

# @app.route("/")
# @app.route("/hello")
# def home():
#     return "Hello world, this is test message"
class API:
    def hello(self, revNo=''):
        print ("*"*100)
        print (revNo)
        print ("*"*100)
        return "hello" +str(revNo), 200
    def logout(self):
        session['user'] = ''
        return redirect(url_for('login'))
    def login(self):
        if request.method == 'GET' and session.get('user') == '':
            return render_template('login.html',data={})
        else:
            error = None
            if request.form.get('name')=='':
                error = 'invalid user'                
                return render_template('login.html',error=error)

            user_data = session.get('user')
            if session.get('user') in ['',None]:
                session['user'] = request.form['name']
                user_data = session['user']
            flash('Login succeed')                
            return render_template('main.html', user=user_data)
api = API()

app.add_url_rule('/','home',home)
app.add_url_rule('/login','login',api.login, methods=['GET','POST'])
app.add_url_rule('/logout','logout', api.logout, methods=['GET'])
app.add_url_rule('/logout','logout', api.logout, methods=['POST'])
app.add_url_rule('/hello/','hello',api.hello)
app.add_url_rule('/hello/<int:revNo>','hello',api.hello)
if __name__ == "__main__":
    app.secret_key='welcome'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)