from models.guarderia import Guarderia,Cuidador,Perros,User
from flask import jsonify, Blueprint
from db import db

from flask import render_template, request, flash, redirect, url_for, session,  jsonify

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask import Flask, render_template, url_for, request, session, flash, redirect, make_response

PATH_URL = "Proyecto_guarderia_Web/views"

#user_blueprint = Blueprint('user_bp', __name__, url_prefix="/users")
guarderia_blueprint = Blueprint('guarderia_bp', __name__)

@guarderia_blueprint.route('/')
def index():
    return "Este es la ruta inicial"

""" @guarderia_blueprint.route('/update')
def update():
    return "Este es una ruta para guarderia" """
""" 
def guarderias_routes(app):
    @app.route('/')
    def index():
        return render_template ("index.html")
        #return "Esta es la App de guarderia"
        
        
def guarderias_routes(app):
    @app.route('/p')
    def productos():
        return render_template ("productos.html")
        #return "Esta es la App de guarderia"        
 """
 
def guarderias_routes(app):
    @app.route('/p')
    def productos():
        return render_template ("productos.html")
        #return "Esta es la App de guarderia"

        #return "Esta es la App de guarderia"
##################################################
#@user_blueprint.route('/lista')
#def lista():
#    users=User.query.all()
#    return jsonify({"data": users[1].name}),201 


""" @guarderia_blueprint.route('/list')
def list():
    guarderias =guarderia.query.all()
    return jsonify({"data": guarderias[1].name}),201 

 """



""" @guarderia_blueprint.route('/ingredientes')
def listar_ingredientes():
    ingredientes = Ingrediente.query.all()
    #return render_template("listar_users.html",listar)
    return render_template ("listar_ingredientes.html",ingredientes=ingredientes) # ("listar_users.html",guarderias=guarderias)
 """

""" @guarderia_blueprint.route('/productos')
def listar_productos():
    productos = Producto.query.all()
    #return render_template("listar_users.html",listar)
    return render_template ("listar_productos.html",productos=productos) # ("listar_users.html",guarderias=guarderias)
 """

#@guarderia_blueprint.route('/perros')
#def ver_perros():
#    perros = Perros.query.all()
#    #return render_template("listar_users.html",listar)
#    return render_template ("listar_perros.html",perros=perros) # ("listar_users.html",heladerguarderias=guarderias)
#
#
#
#
#
#@guarderia_blueprint.route('/update')
#def update():
#    return "Ruta para actualizar"



#@app.route('/')
#def index():
# if 'email' in session:
#  username_session = session['email']
#  user_rs = User.query.filter_by(email=username_session).first()
#  return render_template('index.html', user_rs=user_rs)
# else:
#  return redirect('/login')
 
@guarderia_blueprint.route('/login')
def guarderia_perros():
 if 'email' in session:
  username_session = session['email']
  user_rs = User.query.filter_by(email=username_session).first()
  return render_template('index.html', user_rs=user_rs)
 else:
  return redirect('/login')
 
#@app.route('/login')
@guarderia_blueprint.route('/login')
def login():
    passwordhash = generate_password_hash('test2')
    print(passwordhash)
    return render_template('login.html')
   
@app.route('/submit', methods=['POST'])

def login_submit():
 _email = request.form['inputEmail']
 _password = request.form['inputPassword']
 _remember = request.form.getlist('inputRemember')
  
 if 'email' in request.cookies:
  username = request.cookies.get('email')
  password = request.cookies.get('pwd') 
  row = User.query.filter_by(email=username).first()
  if row and check_password_hash(row.password_hash, password):
   print(username + ' ' + password)
   session['email'] = row.email
   return redirect('/')
  else:
   return redirect('/login')
 # validate the received values
 elif _email and _password:
  #check user exists   
  row = User.query.filter_by(email=_email).first()  
  if row:
   if check_password_hash(row.password_hash, _password):
    session['email'] = row.email
    if _remember:
     resp = make_response(redirect('/'))
     resp.set_cookie('email', _email, max_age=COOKIE_TIME_OUT)
     resp.set_cookie('pwd', _password, max_age=COOKIE_TIME_OUT)
     resp.set_cookie('rem', 'checked', max_age=COOKIE_TIME_OUT)
     return resp
    return redirect('/')
   else:
    flash('Invalid Password!')
    return redirect('/login')
  else:
   flash('Invalid Email Or Password!')
   return redirect('/login')   
   
 else:
  flash('Invalid Email Or Password!')
  return redirect('/login')
   
   
@app.route('/logout')
def logout():
 if 'email' in session:
  session.pop('email', None)
 return redirect('/')
  
""" if __name__ == '__main__':
 app.run(debug=True)
 """