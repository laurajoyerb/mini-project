# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:21:53 2019

@author: Felipe
"""
#example from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hyello'

if __name__=='__main__':
    app.run()