# 📘 Personal Blog

A simple personal blog web application built with **Flask**, allowing you to create, view, and manage blog posts locally. Posts are stored in a JSON file, and the app includes a minimal admin login system for adding new articles.

---

## 🗂 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)

---

## 🧭 Introduction

**Personal Blog** is a lightweight blogging platform that runs locally on your machine.  
It allows you to:
- Add and publish new articles.
- View individual posts.
- Manage blog data easily without setting up a full database.

All blog entries are saved to a local `data.json` file, making this an ideal project for small-scale personal use or learning Flask fundamentals.

---

## ✨ Features

- 📝 Create and view blog posts dynamically  
- 📁 JSON-based data storage (no external database required)  
- 🔒 Basic admin authentication via `.env`  
- 💻 Simple HTML templates and static assets  
- ⚙️ Easy to customize and extend  

---

## 🏗 Project Structure
```
Personal Blog/
├── api.py # Main Flask application
├── data.json # JSON file storing blog posts
├── templates/ # HTML templates for pages
│ ├── homepage.html
│ ├── admin_add_article.html
│ └── article.html
├── static/ # CSS
├── .env # Admin credentials
├── .gitignore
└── README.md
```
---

## ⚙️ Installation

### 1. Clone the repository
```
git clone https://github.com/Grotle4/Personal-Blog.git
cd Personal-Blog
```
### 2. Create a virtual environment
```
python -m venv venv
```
```
source venv/bin/activate  # On macOS/Linux
```

```
venv\Scripts\activate     # On Windows
```


### 3. Install dependencies
```
pip install flask python-dotenv
```

### 🔧 Configuration
Create a .env file in the project root (if not already present):
```
USER=your_username
PASSWORD=your_password
```
This file defines the simple admin credentials used when adding posts.

🚀 Usage
Run the Flask app:
```
python api.py
```
Open your browser and visit:
```
http://127.0.0.1:5000/
```
Use the “Add Article” page to create a new post (login credentials are pulled from .env).

🧩 Example
Add a Post
Navigate to /add

Enter your title and content

Click Submit

Your new article will appear on the homepage and can be viewed individually.

🛠 Troubleshooting
Issue	Possible Cause	Solution
App doesn’t start	Flask not installed	Run pip install flask
Blank homepage	data.json missing or empty	Create an empty data.json ([])
Login not working	Incorrect .env values	Verify USER and PASSWORD entries

👥 Contributors
Dylan Troche – Creator and maintainer

---
Inspiration: https://roadmap.sh/projects/personal-blog