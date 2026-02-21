from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "example123456"


@app.route("/index/<title>")
@app.route("/<title>")
def main_url(title):
    return render_template("base.html", title=title)

@app.route("/training/<prof>")
def url2(prof):
    return render_template("training.html", profession=prof)

@app.route("/list_prof/<list>")
def url3(list):
    return render_template("prof_list.html", list_type=list)

@app.route("/auto_answer")
@app.route("/answer")
def url4():
    params = {}
    params["title"] = "Watny"
    params["surname"] = "Кристанг"
    params["name"] = "Колумб"
    params["education"] = "Химико-технологическое"
    params["profession"] = "Кок"
    params["sex"] = "Мужчина"
    params["motivation"] = "Ради бесплатной пиццы"
    params["ready"] = True

    return render_template("auto_answer.html", **params)

@app.route("/login")
def login_url():
    form = LoginForm()
    return render_template("login.html", form=form, title="Аварийный доступ")

@app.route("/distributions")
def url6():
    astronaut_names = ["Степан Курагин", "Давлетшин Аркадий", "Космостар Евгений", "Отличнев Гусейн"]
    return render_template("distribution.html", names=astronaut_names)

@app.route("/table/<sex>/<int:age>")
def url7(sex, age):
    return render_template("kaut.html", sex=sex, age=age)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")