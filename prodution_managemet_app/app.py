from flask import Flask
from flask import *


app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=False)
