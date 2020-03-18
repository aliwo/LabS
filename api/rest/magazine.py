from flask import jsonify


def get():
    return jsonify({'okay':True, 'magazine':[]})
