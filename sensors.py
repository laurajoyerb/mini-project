# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:55:29 2019

@author: Felipe
"""

from dataclasses import dataclass
import random
from typing import List

sensor_locations = ['Living Room', 'Kitchen', 'Porch', 'Bedroom', 'Greenhouse',
                    'Hallway', 'Elephant room']

@dataclass
class sensor:
    name: str
    temp: int
    humidity: int
    
    def __init__(self, name: str, temp: int, humidity: int): #just initializes
        self.temp = temp
        self.humidity = humidity
        self.name = sensor_locations[random.randint(0, (len(sensor_locations) - 1))]
        
    def current_vals(self):
        nt = self.temp + random.randint(-5,5) #new temperature
        self.temp = nt if (nt > -273) else self.temp #kelvin cause why not
        nh = self.humidity + random.randint(-3,3) #new humidity
        self.humidity = nh if ((nh > 0) and (nh < 100)) else self.humidity #humidity only between 0-100
        
@dataclass
class yuser:
    usr_nem : str
    probes : List[int] #indexes into Sensors
    visits : int
    
    def __init__(self, nem: str):
        self.usr_nem = nem
        self.probes = []
        self.visits = 0
        
    def add_sensor(self, sensor_num: int):
        if ( not (sensor_num in self.probes)):
            self.probes.append(sensor_num)
        else: 
            print('Already added that sensor')
    
    
Sensors : List[sensor] = []
Users : List[yuser] = []
    


#def read_sensor(sensor_id):
#    lim = len(Sensors)
#    if (sensor_id > lim):
#        return 'You get nothing'
#    else:
#        return (str(Sensors[sensor_id].temp) + ',' + str(Sensors[sensor_id].humidity))
    
def associate_sensor(sensor, yuser):
    return 0

def static_test_setup():
    usercount = 10
    nems = 'User'
    s_count = 0
    for i in range(usercount):
        s_lim = random.randint(1,3) #sensor_limit
        usr = yuser(str(nems+str(i)))
        for j in range(s_lim):
            s_count = s_count + 1
            sen = sensor(str(s_count), random.randint(50,70), random.randint(20,40))
            usr.add_sensor(s_count)
            Sensors.append(sen)
        Users.append(usr)
        print(usr)
        
            
        
    
