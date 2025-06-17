import sys
import os
import urllib.parse
from flask import Blueprint, jsonify, request, session,redirect
from config.db_config import get_db_connection
from dotenv import load_dotenv
import hashlib
load_dotenv()
url= Blueprint('URL', __name__)


def generate_short_url(original_url):
    hash_object = hashlib.sha256(original_url.encode())
    short_url= hash_object.hexdigest()[:7]  # Take the first 8 characters of the hash
    return short_url


@url.route('/create', methods=['POST'])
def create_url():
   
    data=request.json
    # check if  useer_id not in session:
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    original_url=data.get('original_url')
    if not original_url:
        return jsonify({"error":"Missing orignal_url"}),400
    short_url = generate_short_url(original_url)
    conn=None
    cursor=None
    try:
        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute('INSERT INTO url (user_id,original_url, short_code) VALUES (%s, %s,%s)', (session['user_id'],original_url, short_url))
        conn.commit()
        return jsonify({"short_url": short_url}), 201
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
@url.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT original_url FROM url WHERE short_code=%s', (short_code,))
        result = cursor.fetchone()
        if result is None:
            return jsonify({"error": "URL not found"}), 404
        original_url = result[0]
        return redirect(original_url)  # Redirect the user to the original URL
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()




