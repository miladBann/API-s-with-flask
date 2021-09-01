import requests
from flask import Flask, render_template
from requests.models import Response


app = Flask(__name__)


@app.route("/")
def hello():

    return "hello world"


@app.route("/<name>")
def hello_world(name):
    Data = {
        "name": name
    }
    response = requests.get("https://api.genderize.io?", params=Data).json()
    result1 = response['gender']

    Data2 = {
        "name": name
    }
    response2 = requests.get("https://api.agify.io?", params=Data2).json()
    result2 = response2["age"]

    return render_template("index.html", gender=result1, age=result2, nameo=name)


@app.route("/blog")
def get_blog():
    all_posts = requests.get(
        " https://api.npoint.io/cc717244241955673fea").json()

    return render_template("blog.html", posts=all_posts)


###################################the blog############################
all_posts = requests.get(
    " https://api.npoint.io/cc717244241955673fea").json()
post_objects = []
for post in all_posts:
    post_obj = {
        "id": post["id"],
        "title": post["title"],
        "subject": post["subject"],
        "body": post["body"]
    }
    post_objects.append(post_obj)



@app.route("/blogcontent/<int:index>")
def get_blog_content(index):

    for post in post_objects:
        if post["id"] == index:
            requested_post = post
            return render_template("blog_content.html", post=requested_post)
