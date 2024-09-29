from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "http://localhost:5001"  # Backend mock API

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cv2/reviewpreview', methods=['GET'])
def get_review_preview():
    product_id = request.args.get('product_id')
    response = requests.get(f"{BASE_URL}/cv2/reviewpreview", params={"Filter": product_id})
    return jsonify(response.json())

@app.route('/cv2/reviewstats', methods=['GET'])
def get_review_stats():
    product_id = request.args.get('product_id')
    response = requests.get(f"{BASE_URL}/cv2/reviewstats", params={"Filter": product_id})
    return jsonify(response.json())

@app.route('/cv2/reviewsubmit', methods=['POST'])
def submit_review():
    data = {
        "productId": request.form['product_id'],
        "rating": request.form['rating'],
        "text": request.form['text']
    }
    response = requests.post(f"{BASE_URL}/cv2/reviewsubmit", json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
