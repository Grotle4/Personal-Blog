from flask import Flask, render_template, request, redirect, url_for, abort
import json
import uuid
import os
import dotenv

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

def count_files():
    try:
        folder_path = r"C:\Users\light\OneDrive\Documents\Python Projects\Personal Blog\templates\articles"
        entries = os.listdir(folder_path)

        file_count = sum(1 for entry in entries if os.path.isfile(os.path.join(folder_path, entry)))
        return file_count
    except FileNotFoundError:
        print("file not found, returning 1")
        return 1
    except Exception as e:
        print(f"An error has occurred: {e}")


@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/add")
def add_article():
    return render_template("admin_add_article.html")

@app.route("/submit", methods=["POST"])
def submit():
    title = request.form["title"]
    content = request.form["content"]

    pages = load_data()
    page_id = count_files()

    new_page = {
        "id": page_id,
        "title": title,
        "content": content
    }

    pages.append(new_page)
    save_data(pages)

    return redirect(url_for("article", page_id=page_id))

@app.route("/article/<string:page_id>")
def view_page(page_id):
    pages = load_data()
    page = next((p for p in pages if p["id"] == page_id), None)
    if not page:
        abort(404)
    return render_template("page.html", page=page)

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
            print("pass 2 passed")
            return render_template("admin_dashboard.html") #TODO: Set up the admin page and ability to add articles so that way the rest of the application can be implemented
        else:
            print("password does not match") #TODO: Return user to login page with proper error message saying that password or user does not match
    else:
        print("username does not match")
    return "something went wrong" #TODO: Return bools here saying if pass or user is correct and then update HTML elements to show user that


@app.route("/return")
def goto_home():
    return render_template("homepage.html")

@app.route("/viewarticle", methods=["POST"])
def load_article():
    if request.method == "POST":
        article_id = request.form.get("item_id")
        action = request.form["action"]
        print(article_id)
        print(action)
        match action:
            case "Delete":
                return f"Deleting article {article_id}" #TODO: Get article id to delete the article once actual article json is setup
            case "Edit":
                return render_template("admin_edit_article.html", article_id=article_id) #TODO: Setup article edit page to be able to edit articles once real articles are setup
        return "This is testing"
    
@app.route("/returnadmin")
def return_admin():
    return render_template("admin_dashboard.html")
    

if __name__ == "__main__":
    app.run(debug=True)

