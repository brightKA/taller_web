#from msilib.schema import Environment
from flask import Flask, escape ,request,render_template #importar la libreria

app = Flask(__name__) #inicializamos la app con el nombre.

app.route('/')
def hola(): #Definimos que la ruto de inicio sera aplicada la funcion hola.
    return'hola penguins!'


@app.route('/coach')
def hola_coaches():
    nombre= 'Karim'
    devolver = request.args.get('nombre', nombre)
    return f'hola', {escape(devolver)}

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)


