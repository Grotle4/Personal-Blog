from flask import Flask, render_template, request, redirect, url_for, abort
import json
import uuid
import os
import dotenv
import time
import datetime

app = Flask(__name__)
DATA_FILE = "data.json"
dotenv.load_dotenv()

username = os.getenv("USER")
password = os.getenv("PASSWORD")


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    pages = load_data()
    return render_template("homepage.html", pages=pages) #TODO: Load JSON data and display article titles on homepage and have it reflect on admin page as well.

@app.route("/add")
def add_article():
    return render_template("admin_add_article.html")

@app.route("/submit", methods=["POST"])
def submit():
    this_time = time.time()
    timestamp = datetime.datetime.fromtimestamp(this_time).strftime("%m-%d-%Y")
    title = request.form["title"]
    content = request.form["content"]
    date = timestamp

    pages = load_data()
    page_id = uuid.uuid1()

    new_page = {
        "id": str(page_id),
        "title": title,
        "content": content,
        "date": str(date)
    }

    pages.append(new_page)
    save_data(pages)

    return redirect(url_for("view_page", page_id=page_id))

@app.route("/article/<string:page_id>")
def view_page(page_id):
    pages = load_data()
    page = next((p for p in pages if p["id"] == page_id), None)
    if not page:
        abort(404)
    return render_template("articlepage.html", page=page)

@app.route("/login")
def login():
    return render_template("admin_login.html")

@app.route("/loginsubmit", methods=["POST"])
def check_login():
    posted_user = request.form.get('username_input')
    posted_password = request.form.get('password_input')
    print(posted_password)
    print(password)
    if posted_user == username:
        print("pass 1 passed")
        if posted_password == password:
            pages = load_data()
            return render_template("admin_dashboard.html", pages=pages) #TODO: Set up the admin page and ability to add articles so that way the rest of the application can be implemented
        else:
            print("password does not match") #TODO: Return user to login page with proper error message saying that password or user does not match
    else:
        print("username does not match")
    return "something went wrong" #TODO: Return bools here saying if pass or user is correct and then update HTML elements to show user that

@app.route("/return")
def goto_home():
    pages = load_data()
    return render_template("homepage.html", pages=pages)

@app.route("/viewarticle", methods=["POST"])
def load_article():
    if request.method == "POST":
        article_id = request.form.get("item_id")
        action = request.form["action"]
        print(article_id)
        print(action)
        match action:
            case "Delete":
                pages = load_data()
                for idx, page in enumerate(pages):
                    if page["id"] == article_id:
                        del pages[idx]
                save_data(pages)
                return render_template("admin_dashboard.html", pages=pages) #TODO: Get article id to delete the article once actual article json is setup
            case "Edit":
                pages = load_data()
                for idx, page in enumerate(pages):
                    if page["id"] == article_id:
                        return render_template("admin_edit_article.html", page=page) #TODO: Setup article edit page to be able to edit articles once real articles are setup
        return "This is testing"
    
@app.route("/returnadmin")
def return_admin():
    return render_template("admin_dashboard.html")


@app.route("/returnedit", methods=["POST"])
def return_edit():
    pages = load_data()
    page_id = request.form.get("id")

    page_title = request.form.get("title")
    page_content = request.form.get("content")
    for idx, page in enumerate(pages):
        print(f"page: {page_id}")
        print(f"page_id: {page["id"]}")
        if page["id"] == page_id:
            print(pages[idx])
            pages[idx]["title"] = page_title
            pages[idx]["content"] = page_content
    save_data(pages)
    return render_template("admin_dashboard.html", pages=pages)


if __name__ == "__main__":
    app.run(debug=True)

