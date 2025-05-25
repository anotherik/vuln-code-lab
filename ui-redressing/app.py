from flask import Flask, request

app = Flask(__name__)

@app.route('/settings')
def settings():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Settings</title>
    </head>
    <body>
        <h2>Welcome, Alice</h2>
        <form action="/delete-account" method="POST">
            <button style="background:red;color:white;font-weight:bold;">Delete My Account</button>
        </form>
    </body>
    </html>
    '''
    return html

@app.route('/delete-account', methods=['POST'])
def delete_account():
    return "<h3>Your account has been deleted (not really)</h3>"

if __name__ == '__main__':
    app.run(debug=True, port=8090)
