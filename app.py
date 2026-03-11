from flask import Flask, render_template
from planets import planets

# створення Flask додатку
app = Flask(__name__)

# головна сторінка
@app.route("/")
def index():
    # передаємо список планет у HTML
    return render_template("index.html", planets=planets)

# сторінка окремої планети
@app.route("/planet/<name>")
def planet(name):

    # отримуємо дані про планету
    data = planets.get(name)

    return render_template(
        "planet.html",
        name=name,
        data=data
    )

# сторінка 3D моделі
@app.route("/solar3d")
def solar3d():
    return render_template("solar3d.html")

# запуск сервера
if __name__ == "__main__":
    app.run(debug=True)