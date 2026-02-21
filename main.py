from flask import Flask, render_template, request, url_for
from forms import *
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "example123456"

user_images = ["https://avatars.mds.yandex.net/i?id=8f5146ec20dc94a0d94b3f94f60524d14faf625a-11462831-images-thumbs&n=13"]

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
    login_form = LoginForm()
    return render_template("login.html", form=login_form, title="Аварийный доступ")

@app.route("/distributions")
def url6():
    astronaut_names = ["Степан Курагин", "Давлетшин Аркадий", "Космостар Евгений", "Отличнев Гусейн"]
    return render_template("distribution.html", names=astronaut_names)

@app.route("/table/<sex>/<int:age>")
def url7(sex, age):
    return render_template("kaut.html", sex=sex, age=age)

@app.route("/galery", methods=["GET", "POST"])
def url8():
    galery_form = GaleryForm()
    if request.method == "GET":
        return render_template("galery.html", form=galery_form, images=user_images)
    elif request.method == "POST":
        filename = galery_form.img_file.data.filename
        galery_form.img_file.data.save("static/" + filename)
        user_images.append(url_for("static", filename=filename))
        return render_template("galery.html", form=galery_form, images=user_images)

@app.route("/member")
def url9():
    with open("templates/members.json", encoding="utf-8") as f:
        members = json.load(f)
    print(members)
    return render_template("members.html", members=members)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")