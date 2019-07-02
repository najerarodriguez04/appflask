#Dependencias
import os
import sqlite3
from flask import Flask, render_template, request, session, escape
from flask import render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

#Configuracion general del software
app = Flask(__name__)
app.config['DEBUG'] = True

#Configuracion del email
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'masterlist.suppliers@gmail.com',
    MAIL_PASSWORD = 'Celeste:801020363',
    
)
mail = Mail(app)

#Base de datos login de user
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
DATABASE = "data.db"
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Gestión de la base de datos proveedores
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def change_db(query,args=()):
    cur = get_db().execute(query, args)
    get_db().commit()
    cur.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


#URL start el inicio de la aplicacion
@app.route('/')
def introduccion():
    return render_template("start/introduccion.html")

@app.route('/faqgenerar')
def faqgenerar():
    return render_template("start/faqgenerar.html")

@app.route('/faquso')
def faquso():
    return render_template("start/faquso.html")

@app.route('/faqsroi')
def faqsroi():
    return render_template("start/faqsroi.html")

#URL user como login perfil signup
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return render_template("general/dashboard.html")
        return render_template("user/loginerror.html")


    return render_template("user/login.html")

@app.route("/loginerror", methods=["GET", "POST"])
def loginerror():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return render_template("general/dashboard.html")
        return render_template("user/loginerror.html")

    return render_template("user/login.html")

@app.route('/perfil')
def perfil():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("user/perfil.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/signup')
def signup():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("user/signup.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("user/login.html",contact_list=contact_list)

#URL GENERAL

@app.route('/empresa')
def empresa():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("general/empresa.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/dashboard')
def dashboard():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("general/dashboard.html",contact_list=contact_list)
    return render_template("user/login.html")

#URL generar efectivo
@app.route('/posicionamiento')
def posicionamiento():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("generar/posicionamiento.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/tendencias')
def tendencias():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("generar/tendencias.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/comunicacion')
def comunicacion():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("generar/comunicacion.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/competencia')
def competencia():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("generar/competencia.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/clientes')
def clientes():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("generar/clientes.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/mensaje')
def mensaje():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("generar/mensaje.html",contact_list=contact_list)
    return render_template("user/login.html")

#URL uso de efectivo
@app.route('/subir')
def subir():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/subir.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/er')
def er():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/er.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/bg')
def bg():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/bg.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/fe')
def fe():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/fe.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/pago')
def pago():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/pago.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/cobro')
def cobro():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/cobro.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/depreciacion')
def depreciacion():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/depreciacion.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/verfinanzas')
def verfinanzas():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/verfinanzas.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/suposicionesinternas')
def suposicionesinternas():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("uso/suposicionesinternas.html",contact_list=contact_list)
    return render_template("user/login.html")

#URL SROI evaluacion proyectos de inversion social-ambiental
@app.route('/relojsostenibilidad')
def relojsostenibilidad():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/relojsroi.3.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/arbolsostenibilidad')
def arbolsostenibilidad():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/arbol.4.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/relojriesgos')
def relojriesgos():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/relojsroi.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/arbolriesgos')
def arbolriesgos():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/arbol.3.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/relojbarreras')
def relojbarreras():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/relojsroi.1.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/arbolbarreras')
def arbolbarreras():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/arbol.1.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/relojmercado')
def relojmercado():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/relojsroi.2.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/arbolmercado')
def arbolmercado():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("frontend/arbol.2.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/barreras/<int:id>', methods=['GET', 'POST'])
def barreras(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("barreras.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['barreras'],id]
            change_db("UPDATE contact SET barreras=? WHERE ID=?",values)
            return redirect(url_for("relojbarreras"))
    return render_template("user/login.html")

@app.route('/mercado/<int:id>', methods=['GET', 'POST'])
def mercado(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("mercado.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['cliente'],contact['beneficiario'],contact['soluciona'],contact['ubicacion'],id]
            change_db("UPDATE contact SET cliente=?, beneficiario=?,soluciona=?,ubicacion=? WHERE ID=?",values)
            return redirect(url_for("relojmercado"))
    return render_template("user/login.html")

@app.route('/riesgos/<int:id>', methods=['GET', 'POST'])
def riesgos(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("riesgos.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['riesgo'],id]
            change_db("UPDATE contact SET riesgo=? WHERE ID=?",values)
            return redirect(url_for("verproyectos"))
    return render_template("user/login.html")

@app.route('/sostenibilidad/<int:id>', methods=['GET', 'POST'])
def sostenibilidad(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("sostenibilidad.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['ingreso'],contact['montoingreso'],contact['ingreso1'],contact['montoingreso1'],contact['ingreso2'],contact['montoingreso2'],contact['ingreso3'],contact['montoingreso3'],contact['gasto1'],contact['montogasto1'],contact['gasto2'],contact['montogasto2'],contact['gasto3'],contact['montogasto3'],contact['gasto4'],contact['montogasto4'],contact['gasto5'],contact['montogasto5'],id]
            change_db("UPDATE contact SET ingreso=?,montoingreso=?,ingreso1=?,montoingreso1=?,ingreso2=?,montoingreso2=?,ingreso3=?,montoingreso3=?,gasto1=?,montogasto1=?,gasto2=?,montogasto2=?,gasto3=?,montogasto3=?,gasto4=?,montogasto4=?,gasto5=?,montogasto5=? WHERE ID=?",values)
            return redirect(url_for("relojsostenibilidad"))
    return render_template("user/login.html")

@app.route('/master/<int:id>', methods=['GET', 'POST'])
def master(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("master.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['recomendacion'],contact['sroi'],contact['sroi1'],contact['sroi2'],contact['consejouno'],id]
            change_db("UPDATE contact SET recomendacion=?,sroi=?,sroi1=?,sroi2=?,consejouno=? WHERE ID=?",values)
            return redirect(url_for("verproyectos1"))
    return render_template("user/login.html")

@app.route('/analisis')
def analisis():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("verproyectos.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/verproyectos')
def verproyectos():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("verproyectos.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/verproyectos1')
def verproyectos1():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("verproyectos.1.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/verproyectos2')
def verproyectos2():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("verproyectos.2.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/verproyectos3')
def verproyectos3():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("verproyectos.3.html",contact_list=contact_list)
    return render_template("user/login.html")

#Gestion de la base de datos
#Datos de entidad
@app.route('/crearempresa', methods=['GET', 'POST'])
def crearempresa():
    if "username" in session:
        if request.method == "GET":
            return render_template("crearempresa.html",contact=None)

        if request.method == "POST":
            contact=request.form.to_dict()
            values=[contact['entidad'],contact['tel'],contact['email'],contact['representante'],contact['usuario'],contact['emailusuario'],contact['dedica'],contact['productoservice'],contact['pagweb'],contact['mensajeventas'],contact['redessociales']]
            change_db("INSERT INTO contact (entidad,tel,email,representante,usuario,emailusuario,dedica,productoservice,pagweb,mensajeventas,redessociales) VALUES (?,?,?,?,?,?,?,?,?,?,?)",values)
            return redirect(url_for("empresa"))
    return render_template("user/login.html")

@app.route('/crearproyecto', methods=['GET', 'POST'])
def crearproyecto():
    if "username" in session:
        if request.method == "GET":
            return render_template("crearproyecto.html",contact=None)

        if request.method == "POST":
            contact=request.form.to_dict()
            values=[contact['nombreproyecto'],contact['descripcionproyecto'],contact['objetivouno'],contact['objetivodos'],contact['objetivotres']]
            change_db("INSERT INTO contact (nombreproyecto,descripcionproyecto,objetivouno,objetivodos,objetivotres) VALUES (?,?,?,?,?)",values)
            return redirect(url_for("verproyectos"))
    return render_template("user/login.html")

@app.route('/actualizarempresa/<int:id>', methods=['GET', 'POST'])
def actualizarempresa(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("actualizarempresa.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['entidad'],contact['tel'],contact['email'],contact['representante'],contact['usuario'],contact['emailusuario'],contact['dedica'],contact['productoservice'],contact['pagweb'],contact['mensajeventas'],contact['redessociales'],id]
            change_db("UPDATE contact SET entidad=?,tel=?,email=?,representante=?,usuario=?,emailusuario=?,dedica=?,productoservice=?,pagweb=?,mensajeventas=?,redessociales=? WHERE ID=?",values)
            return redirect(url_for("empresa"))
    return render_template("user/login.html")

@app.route('/actualizarproyecto/<int:id>', methods=['GET', 'POST'])
def actualizarproyecto(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("actualizarproyecto.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['nombreproyecto'],contact['descripcionproyecto'],contact['objetivouno'],contact['objetivodos'],contact['objetivotres'],id]
            change_db("UPDATE contact SET nombreproyecto=?,descripcionproyecto=?,objetivouno=?,objetivodos=?,objetivotres=? WHERE ID=?",values)
            return redirect(url_for("verproyectos"))
    return render_template("user/login.html")


@app.route('/verempresa/<int:id>', methods=['GET', 'POST'])
def verempresa(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("verempresa.html",contact=contact)


    return render_template("user/login.html")

@app.route('/verdashboarduno/<int:id>', methods=['GET', 'POST'])
def verdashboarduno(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("verdashboard.1.html",contact=contact)


    return render_template("user/login.html")

@app.route('/verdashboarddos/<int:id>', methods=['GET', 'POST'])
def verdashboarddos(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("verdashboard.2.html",contact=contact)


    return render_template("user/login.html")

@app.route('/verdashboardtres/<int:id>', methods=['GET', 'POST'])
def verdashboardtres(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("verdashboard.3.html",contact=contact)


    return render_template("user/login.html")

@app.route('/verdashboardcuatro/<int:id>', methods=['GET', 'POST'])
def verdashboardcuatro(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("verdashboard.4.html",contact=contact)


    return render_template("user/login.html")

@app.route('/verproyecto/<int:id>', methods=['GET', 'POST'])
def verproyecto(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("verproyecto.html",contact=contact)


    return render_template("user/login.html")

@app.route('/sroiproyecto/<int:id>', methods=['GET', 'POST'])
def sroiproyecto(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("sroiproyecto.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['sroi'],contact['sroi1'],contact['sroi2'],id]
            change_db("UPDATE contact SET sroi=?,sroi1=?,sroi2=? WHERE ID=?",values)
            return redirect(url_for("verproyectos"))
    return render_template("user/login.html")

@app.route('/borrarempresa/<int:id>', methods=['GET', 'POST'])
def borrarempresa(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("borrarempresa.html",contact=contact)

        if request.method == "POST":
            change_db("DELETE FROM contact WHERE id = ?",[id])
            return redirect(url_for("empresa"))
    return render_template("user/login.html")

@app.route('/borrarproyecto/<int:id>', methods=['GET', 'POST'])
def borrarproyecto(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("borrarproyecto.html",contact=contact)

        if request.method == "POST":
            change_db("DELETE FROM contact WHERE id = ?",[id])
            return redirect(url_for("verproyectos"))
    return render_template("user/login.html")

@app.route('/verempresas', methods=['GET', 'POST'])
def verempresas():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("general/empresa.html",contact_list=contact_list)
    return render_template("user/login.html")


#URL configuraciones del sistema y error
@app.route('/error')
def error():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("configuracion/error.html",contact_list=contact_list)
    return render_template("user/login.html")

@app.route('/error404')
def error404():        
    return render_template("configuracion/error.html")

app.secret_key = "12345"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)