from flask import Flask, make_response, redirect, request, jsonify, render_template, send_from_directory
import dotenv
import os
import requests
import json

dotenv.load_dotenv()


app = Flask(__name__)

# Start the server for local testing
if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')