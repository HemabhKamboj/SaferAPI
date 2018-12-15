from flask import Flask, jsonify, request, render_template
from p import *
import numpy as np

app = Flask(__name__)

def getParameters():
    source = request.args.get('source')
    destination = request.args.get('destination')
    vtype = request.args.get('vtype')

    return(source, destination, vtype)

@app.route('/directions', methods=['GET'])
def directions():
    source, destination, vtype = getParameters()
    all_paths = get_path(source, destination, vtype)

    return jsonify(
        {
            "all_paths": all_paths
        }
    )

@app.route('/')
def index():
    return render_template('index.html')

if __name__  == '__main__':
    app.run(debug=True)