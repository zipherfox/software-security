"""
Deliberately INSECURE sample for Week 2 scanning practice.
Do NOT copy these patterns into real code. Find them with SAST + secret scanning.
"""
import sqlite3, hashlib, subprocess, argon2
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv('secrets.env') #Fix CWE-259: hardcoded secrets (in .env file)

app = Flask(__name__)
@app.route("/user")
def user():
    name = request.args.get("name", "")
    con = sqlite3.connect("app.db")
    # Fix CWE-89: SQL injection (string formatting into query)
    query = "SELECT * FROM users WHERE name = ?"
    con.execute(query, (name,))

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # Fix CWE-78: OS command injection (shell=True with user input)
    return subprocess.check_output(["ping", "-c", "1", host], shell=False)

def store_password(pw):
    # Fix CWE-327: weak hash for passwords
    return argon2.PasswordHasher().hash(pw)

if __name__ == "__main__":
    app.run(debug=False)  # Fix CWE-489: debug mode in production
