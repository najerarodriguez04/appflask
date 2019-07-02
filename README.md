Pile-of-money
{{ url_for('faqsroi') }}
#Dependencias
pip install flask
pip install Flask-SQLAlchemy
pip install Flask-Mail


#Rutas URL
Inicio start

    introduccion
    faq generar
    faq uso
    faq sroi

User
    login
    login error
    perfil
    signup
    logout

General
    master
    empresa
    dashboard

Generar
    posicionamiento en internet
    reconocimiento de tendencias
    canales de comunicacion
    monitoreo de la competencia
    busqueda de clientes
    efectividad del mensaje de ventas

Uso
    subir informacion financiera
    er
    bg
    fe
    politicas de pago
    politicas de cobro
    depreciacion 
    ver finanzas
    suposicionesinternas (Suposicones y variables)


SROI
    mercado
    riesgos 
    barreras de entrada
    sostenibilidad
    verproyectos 


Configuraciones del sistema y error
    error

Gestiondatos
    create
    delete
    update
    view
    viewtodos

Frontend
    arbol
    cohete
    frontend
    navbar
    reloj


#Base de datos

CREATE TABLE `contact` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`entidad`	TEXT NOT NULL,
	`tel`	TEXT,
	`email`	TEXT,
	`representante`	TEXT,
	`usuario`	TEXT,
	`emailusuario`	TEXT,
	`dedica`	TEXT,
	`productoservice`	TEXT,
	`pagweb`	TEXT,
	`mensajeventas`	TEXT,
	`redessociales`	TEXT,

GENERAR
	`comunicacion`	TEXT,
	`competidores`	TEXT,
    `segmento`	TEXT,
	`porquepagan`	TEXT,
	`palabrasclaves`	TEXT,

SROI
	`nombreproyecto`	TEXT,
	`objetivouno`	TEXT,
	`objetivodos`	TEXT,
	`objetivotres`	TEXT,

SISTEMA
dashboard
	`consejouno`	TEXT,
	`consejodos`	TEXT,
	`consejotres`	TEXT,
	`consejocuatro`	TEXT,
sroi
	`sroiuno`	TEXT,
	`soidos`	TEXT,
	`sroitres`	TEXT,
	`sroicuatro`	TEXT,
	`moreuno`	TEXT,
	`moredos`	TEXT,
	`moretres`	TEXT,
	`morecuatro`	TEXT,
	`morecinco`	TEXT,
	`moreseis`	TEXT,
	`moresiete`	TEXT,
	`moreocho`	TEXT,
  	`status`	TEXT
    `gasto`	TEXT,
	`montogasto`	TEXT,
	`ingreso`	TEXT,
	`montoingreso`	TEXT
  	`descripcionproyecto`	TEXT

);