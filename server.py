from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hola_mundo():
    return "<h1> Hola Mundo!</h1>"

@app.route('/dojo')

def dojo():
    return "<p> Dojo!</p>"

@app.route('/say/flask')

def holaFlask():
    return "<h1> Hola, Flask!</h1>"

@app.route('/say/<nombre>')

def holaNombre(nombre):

    if isinstance(nombre, str):
        return "Hola " + nombre
    else:
        return "<h1> Intentalo de nuevo </h1>"


@app.route('/repeat/<int:num>/<palabra>')

def repitePalabra(num, palabra):
    output=""
    for i in range (0, num):
        output += palabra + " "
        

    return output


@app.route ('/hola/<nombre>')
def hola_nombre(nombre):
    return "Hola " + nombre




@app.route('/hello')

def hola_mundo2():
    return render_template('index.html', nombre= "John") #JINJA nos deja implementar python en html



if __name__ == "__main__":
    app.run (debug = True)
