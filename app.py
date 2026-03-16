from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)

# секретний ключ для session
app.secret_key = "solar_system_secret"


# сторінка входу
@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        nickname = request.form.get("nickname")

        # зберігаємо нік у сесії
        session["user"] = nickname

        # записуємо у файл
        with open("visitors.txt","a",encoding="utf-8") as f:
            f.write(f"{nickname} | {datetime.now()}\n")

        return redirect("/menu")

    return render_template("login.html")


# головне меню
@app.route("/menu")
def menu():

    if "user" not in session:
        return redirect("/")

    return render_template("index.html", user=session["user"])


# сторінка 3D системи
@app.route("/solar3d")
def solar():

    if "user" not in session:
        return redirect("/")

    return render_template("solar3d.html")


# вихід
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)