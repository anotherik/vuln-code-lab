from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            Upload JSON File: <input type="file" name="datafile">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['datafile']
    data = f.read()

    try:
        obj = json.loads(data.decode())
    except UnicodeDecodeError:
        return "Error: Uploaded file is not valid UTF-8. Expected a JSON file.", 400
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}", 400

    return f"Parsed data: {obj}"

if __name__ == '__main__':
    app.run(debug=True, port=8090)

