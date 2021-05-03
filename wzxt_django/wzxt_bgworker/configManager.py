# 01-05-2021
# Simple python Configuration File using json, Written By Harishankar Kumar (https://github.com/hari01584)
# Extend as you wish

import json
import os.path

class MyConfig:
    # Basic template for your config, this will be created if config file not found
    config = {
        "enableMain": True,
        "enableV1": False,
        "baseCurrency": "INR",
        "requiredAPI": ["getMarketStatus","getMarketTicker","",""],
        "strategy_to_use": [
            {
                "name": "Basic Template",
                "isSimulation": False,
                "file": "01_basic_template.py"
            }
        ],
        "token": "token"
    }


    # Initialize for a file name, note: if given a simple name like abc.xyz, then it will create/look for sample folder
    # ie current dir/root, optionally you can also provide full path of your configs (Not recommended)
    def __init__(self,file):
        if not os.path.isfile(file):
            self.createFromTemplate(file)
        with open(file, 'r') as jsonFile:
            self.config = json.load(jsonFile)

    #Function to create file from template, triggered in case no file exists!
    def createFromTemplate(self, file):
        with open(file, "w") as jsonfile:
            json.dump(self.config, jsonfile, indent=4)

    # ONLY FOR DEVELOPMENT, Optionally this should be commented as it gives too much scope to user, well if
    # your config is gonna be short, it could still be feasible
    def getConfig(self):
        return self.config

    # Get a specfic setting/config in the file, Good to use, just some boilerplate code tho :D
    def getStrategyFile(self):
        return self.config["strategy_to_use"]

    # List out all apis required for all scripts, ie preload all data before sending and executing logic
    def getApiRequired(self):
        return self.config["requiredAPI"]

    # Get base currency of user in which all transactions is to be made
    def getBaseCurrency(self):
        return self.config["baseCurrency"]


myConfig = MyConfig('config.json')
