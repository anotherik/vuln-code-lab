from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h3>Upload User Profile (XML)</h3>
        <form method="POST" action="/upload" enctype="multipart/form-data">
            <input type="file" name="xmlfile">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('xmlfile')
    if not file:
        return "No file provided", 400

    try:
        parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
        tree = etree.parse(file, parser)
        root = tree.getroot()

        name = root.findtext('name')
        email = root.findtext('email')

        return f"<h4>Parsed Profile:</h4><p>Name: {name}<br>Email: {email}</p>"

    except Exception as e:
        return f"Error parsing XML: {e}", 400

if __name__ == '__main__':
    app.run(debug=True, port=8090)
