from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        radio = float(request.form["radio"])

        area = 3.14 * radio * radio
        perimetro = 2 * 3.14 * radio

        return """
        <h1>Resultado</h1>
        <p>Area: {}</p>
        <p>Perimetro: {}</p>
        <a href="/">Regresar</a>
        """.format(area, perimetro)

    return """
    <h1>Circulo</h1>

    <form method="POST">

        Radio:
        <input type="number" name="radio">

        <button type="submit">Calcular</button>

    </form>
    """

app.run(debug=True)
