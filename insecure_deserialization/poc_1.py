from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            Upload Pickle File: <input type="file" name="picklefile">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['picklefile']
    data = f.read()

    obj = pickle.loads(data)

    return f"Deserialized object: {obj}"

if __name__ == '__main__':
    app.run(debug=True, port=8090)
