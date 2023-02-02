from flask import Flask, request

app = Flask(__name__)

STORE_IRISES_PATH = 'mock_server/stored_irises/'


@app.route('/signup', methods=['POST'])
def endpoint():
    data = request.get_data()
    boundary = request.headers['Content-Type'].split('=')[1]

    parts = data.split(boundary.encode())
    image_data = None
    json_data = None

    for part in parts:

        if b"Content-Disposition: form-data; name=\"image\"" in part:
            image_data = part.split(b"\r\n\r\n")[1][:-2]

        if b"Content-Disposition: form-data; name=\"id\"" in part:
            start = part.find(b'\r\n\r\n') + 4
            end = part.find(b'\r\n--')
            json_data = {"id": part[start:end].decode('utf-8')}

    if image_data and json_data:
        # use the image hash that was sent as id to crate the file name
        file_name = json_data.get('id', 'file') + '.png'
        with open(STORE_IRISES_PATH + file_name, "wb") as f:
            f.write(image_data)

        return f"Uploaded object {json_data}", 200

    return "Failed to upload object", 400


@app.route('/status', methods=['POST'])
def status():
    data = request.get_json()
    return f"status reported {data}", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
