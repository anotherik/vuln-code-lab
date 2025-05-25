from flask import Flask, make_response

app = Flask(__name__)

@app.route('/settings')
def settings():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Settings</title>
        <script>
            // Framebusting for legacy browsers
            if (self !== top) {
                top.location = self.location;
            }
        </script>
    </head>
    <body>
        <h2>Welcome, Alice</h2>
        <form action="/delete-account" method="POST">
            <button style="background:green;color:white;font-weight:bold;">Delete My Account</button>
        </form>
    </body>
    </html>
    '''
    response = make_response(html)
    # Secure headers
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "frame-ancestors 'none';"
    return response

@app.route('/delete-account', methods=['POST'])
def delete_account():
    return "<h3>Account deletion simulated</h3>"

if __name__ == '__main__':
    app.run(debug=True, port=8090)
