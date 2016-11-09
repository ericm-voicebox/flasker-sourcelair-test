import os
import glob
import socket

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from {}!'.format(socket.gethostname())

@app.route('/files')
def get_files():
    files = [f for f in glob.glob('*.*')]
    return '<br/>'.join(files)

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
    except ValueError:
        port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
