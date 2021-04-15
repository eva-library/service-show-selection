import json
import requests
import logging.config
import sys
import os
import sqlite3
from flask import Flask, request, jsonify
from itertools import cycle
app = Flask(__name__)

class DataBase:    
    def __init__(self):
        print("BBDD")

    def showSelection(self):

        try:
             # We save in a variable the request that comes from eva
            req_body = request.json
            item_list = ( req_body['hiddenContext']['selectedMaterialsList'])
            # Transactional response to show the list of selected products
            result = {
                "answer": {
                        "content": {
                                "content": "Confirm your selection and quantity of products.<br><strong>You selected:</strong>",
                                "description": "Transactional response to show the list of selected products",
                                "type": "TEXT",
                                "buttons": [],
                                "quickReply": []
                        },
                        "technicalText": {
                               "type":"multi-option",
                                "code":"PEDIDO_POP",
                                "view": "list",
                                "options": item_list,
                                "text": "<strong>Confirm your selection or add more products</strong>",
                                "buttons": [
                                    { "text": "Add more products", "accion": "ADD_MORE_PRODUCTS" },
                                    { "text": "Confirm selection", "accion": "CONFIRM_SELECTION" }
                            ]
                        },
                        "template": "TEXT"
                },
                "openContext" : req_body["openContext"] ,
                "visibleContext" : req_body["visibleContext"],
                "hiddenContext": req_body["hiddenContext"],
            }
            # returns a transactional response in eva format in JSON format
            return result

        except:
            # If any error happens, this is the answer with the formatvo eva
            result = {
                "answer": {
                        "content": {
                                "content": "ERROR",
                                "description": "",
                                "type": "TEXT",
                                "buttons": [],
                                "quickReply": []
                        },
                        "technicalText": {},
                        "template": "TEXT"
                },
                "openContext" : {} ,
                "visibleContext" : {},
                "hiddenContext": {},
            }
        # returns a transactional response in eva format in JSON format
        return result


@app.route("/show-selection", methods=["POST"])

def test_functions(self):
    database = DataBase()    
    return database.showSelection()
    
if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')