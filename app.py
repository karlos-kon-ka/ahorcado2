from flask import Flask, render_template, request

app = Flask(__name__)

# Palabra secreta (puedes cambiarla)
palabra_secreta = "PYTHON"

# Lista de letras correctas adivinadas
letras_correctas = []

# Intentos permitidos
intentos_maximos = 6
intentos_actuales = 0

@app.route('/')
def inicio():
    return render_template('index.html', palabra_actual=obtener_palabra_actual(), intentos_restantes=intentos_maximos - intentos_actuales)

@app.route('/', methods=['POST'])
def procesar_letra():
    global intentos_actuales
    letra = request.form['letra'].upper()

    if letra.isalpha() and letra not in letras_correctas:
        letras_correctas.append(letra)
        if letra not in palabra_secreta:
            intentos_actuales += 1

    return render_template('index.html', palabra_actual=obtener_palabra_actual(), intentos_restantes=intentos_maximos - intentos_actuales)

def obtener_palabra_actual():
    return ''.join([letra if letra in letras_correctas else '_' for letra in palabra_secreta])

if __name__ == '__main__':
    app.run(debug=True)
