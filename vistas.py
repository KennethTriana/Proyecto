from flask import Flask, request

app = Flask(_name_)
@app.route("/")
def home():
    app.logger.info(f'Solicitud en la ruta {request.path}')
    return "<p> Bienvenido a la creacion de un nuevo usuario </p>"

@app.route("/Cargo/<string:cargo>")
def Cargo (cargo):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Cargo: {cargo}"
    
@app.route("/Nombres/<string:nombres>")
def Nombre (nombres):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Nombre: {nombres}"

@app.route("/Apellidos/<string:apellidos>")
def Apellidos (apellidos):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Apellido: {apellidos}"

@app.route("/edad/<int:edad>")
def edad (edad):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Edad: {edad}"

@app.route("/Calle/<calle>")
def Calle (calle):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Calle: {calle}"

@app.route("/Telefono/<int:telefono>")
def Telefono (telefono):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Numero: {telefono}"

@app.route("/Correo/<string:correo>")
def Correo (correo):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    return f"Correo: {correo}"
    
@app.route("/Genero/<string:genero>")
def Genero(genero):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    if genero == "M" or "m":
        return "Género: Hombre"
    else:
        return "Género: Mujer"

@app.route("/Identidad/<string:tarjeta>")
def Identidad(tarjeta):
    app.logger.info(f"Solicitud en la ruta {request.path}")
    if tarjeta == "CC" or "cc":
        return "Cedula de Ciudadania"
    if tarjeta == "TT" or "tt":
        return "Tarjeta de Identidad"
    else:
        return "Cedula Extrangera"