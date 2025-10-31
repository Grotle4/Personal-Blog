from flask import Flask, render_template, request, redirect, url_for, abort
import json
import uuid
import os

app = Flask(__name__)
DATA_FILE = "data.json"


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

if __name__ == "__main__":
    app.run(debug=True)

