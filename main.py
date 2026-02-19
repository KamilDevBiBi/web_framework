from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")