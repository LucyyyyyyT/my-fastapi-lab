from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()

# Mount static files folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Point to templates folder
templates = Jinja2Templates(directory="templates")


def get_messages():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''
        SELECT messages.text, messages.created_at, users.username, users.age
        FROM messages
        JOIN users ON messages.user_id = users.id
        ORDER BY messages.created_at DESC
    ''')
    rows = c.fetchall()
    conn.close()
    return [
        {
            "text": r["text"],
            "created_at": r["created_at"],
            "username": r["username"],
            "age": r["age"]
        }
        for r in rows
    ]


@app.get("/")
def index(request: Request):
    messages = get_messages()
    return templates.TemplateResponse(request, "index.html", {"messages": messages})


@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(request, "login.html", {})


@app.get("/logout")
def logout(request: Request):
    return templates.TemplateResponse(request, "logout.html", {})


@app.get("/create_message")
def create_message(request: Request):
    return templates.TemplateResponse(request, "create_message.html", {})


@app.get("/create_user")
def create_user(request: Request):
    return templates.TemplateResponse(request, "create_user.html", {})