from flask import Flask, request
import pickle
import io

app = Flask(__name__)

# Custom restricted unpickler
class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Only allow safe built-in types
        allowed = {
            "builtins": {"dict", "list", "str", "int", "float", "bool", "set", "tuple"}
        }

        if module in allowed and name in allowed[module]:
            return super().find_class(module, name)
        
        raise pickle.UnpicklingError(f"Blocked unsafe class: {module}.{name}")

def restricted_loads(s):
    return RestrictedUnpickler(io.BytesIO(s)).load()

# Flask routes
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

    try:
        obj = restricted_loads(data)
    except pickle.UnpicklingError as e:
        return f"Unsafe pickle rejected: {e}", 400
    except Exception as e:
        return f"Deserialization failed: {e}", 500

    return f"Deserialized safely: {obj}"

if __name__ == '__main__':
    app.run(debug=True, port=8090)
