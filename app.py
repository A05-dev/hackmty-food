from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scan_image', methods=['POST'])
def scan_image():
    image = request.files['image'].read()
    hashtable = cv2.scan_image(image)
    return jsonify(hashtable)

if __name__ == '__main__':
    app.run()