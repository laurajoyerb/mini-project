# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:21:53 2019

@author: Felipe
"""
#example from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
from sensors import Users
from sensors import Sensors
from sensors import static_test_setup
from flask import Flask
from flask import request
from sensors import read_sensor
#https://stackoverflow.com/questions/22947905/flask-example-with-post
app = Flask(__name__)

set_up = False #if server has been initalized


@app.route('/miniproj/<usr_id>', methods = ['GET', 'POST', 'DELETE'])
def showstuff(usr_id):
    if request.method == 'GET':
        ret_str = 'User ' + str(usr_id)
        uid = int(usr_id)
        if (uid >= len(Users)):
            return 'User exceeds maximum'
        else:
            usr = Users[uid]
            for i in usr.probes:
                sen = Sensors[i]
                ret_str += '\nSensor: ' + sen.name + '\n'
                ret_str += 'Humidity: ' + str(sen.humidity)
                ret_str += ' , Temperature: ' + str(sen.temp)
                ret_str += '\n\n'
            return ret_str
    else:
        return "I have no idea what you're trying to do"
    

@app.route('/setup/')
def setup():
    if (not (set_up)): 
        static_test_setup()
        global set_up
        set_up = True
        return (str(len(Users)) + ' users set up. ' + str(len(Sensors)) + ' sensors set up')
    else:
        return 'You already set it up'

#http://127.0.0.1:5000/miniproj/
@app.route('/miniproj/')
def hello_world():
    return 'Hyello'

if __name__=='__main__':
    app.run()