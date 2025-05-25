import sys
import os
from flask import Flask, jsonify, request,session,Blueprint
from dotenv import load_dotenv
import psycopg2
import hashlib
from config.db_config import get_db_connection  # type: ignore

auth = Blueprint('Auth', __name__)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not all([username, email, password]):
        return jsonify({"error": "Missing required Field"}), 400
    hashed_password = hash_password(password)
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
        temp = cursor.fetchone()
        if temp is not None:
            return jsonify({'error': 'user already exists'}), 401
        cursor.execute('INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)',
                       (username, email, hashed_password))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
@auth.route('/login',methods=['POST'])
def login():
    data=request.json
    email=data.get('email')
    password=data.get('password')
    if not all([email,password]):
        return jsonify({"error":"Missing required fields"}),400
    hashed_password = hash_password(password)
    conn=None
    cursor=None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
        user = cursor.fetchone()
        if user is None:
            return jsonify({"error": "Invalid email"}), 401
        if user[3] != hashed_password:  # Assuming the password hash is in the 4th column
            return jsonify({"error": "Invalid password"}), 401
        # Store user ID in session
        session['user_id'] = user[0]  # Assuming the first column is user_id
        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()





