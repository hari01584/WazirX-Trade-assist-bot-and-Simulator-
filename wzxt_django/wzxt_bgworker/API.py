# 01-05-2021
# Simple python WazirX Public API, Written By Harishankar Kumar (https://github.com/hari01584)
# Extend as you wish

# UNUSED variables, added them for scalibility purpose (Can remove safely)
api_url = 'UNDEFINED'
apiKey = 'UNDEFINED'
secret = 'UNDEFINED'

# API server configs, last updated on 01-05-2021, Change if obsolete (ref. https://github.com/WazirX/wazirx-api)
API_PROTO = "https://"
API_BASE = API_PROTO + "api.wazirx.com"
API_LINK_MARKET_STATUS = "/api/v2/market-status"
API_LINK_MARKET_TICKER = "/api/v2/tickers"
API_LINK_MARKET_DEPTH = "/api/v2/depth"
API_LINK_MARKET_TRADE_HISTORY = "/api/v2/trades"

import json, requests

# Define wazirapi class
class WZXAPI(object):
    # Init, set the variables, once again the code is redundant as api doesnt need key or secret atm.
    def __init__(self, api_url="UNDEFINED", apiKey="UNDEFINED", secret="UNDEFINED"):
        self.api_url = api_url
        self.apiKey = apiKey
        self.secret = secret


    # Get multiple api data in dictionary form, useful for multi loading
    def getMultipleApiData(self, requiredAPIs):
        data = {}
        if("getMarketStatus" in requiredAPIs):
            data["getMarketStatus"] = self.getMarketStatus()

        if("getMarketTicker" in requiredAPIs):
            data["getMarketTicker"] = self.getMarketTicker()

        if("getMarketDepth" in requiredAPIs):
            data["getMarketDepth"] = self.getMarketDepth()

        if("getMarketTradeHistory" in requiredAPIs):
            data["getMarketTradeHistory"] = self.getMarketStatus()

        return data


    # Function getMarketStatus, Returns A Nested dictionary comprising of the API Results, You can print to see the data
    # Or optionally check the API output from original wazirx api repo (ref. https://github.com/WazirX/wazirx-api)
    def getMarketStatus(self):
        resp = requests.get(API_BASE+API_LINK_MARKET_STATUS)
        if resp.status_code != 200:
            raise APIError("Error in getMarketStatus, status code="+str(resp.status_code))
        return resp.json()

    # Function getMarketTicker, Returns A Nested dictionary comprising of the API Results, You can print to see the data
    # Or optionally check the API output from original wazirx api repo (ref. https://github.com/WazirX/wazirx-api)
    def getMarketTicker(self):
        resp = requests.get(API_BASE+API_LINK_MARKET_TICKER)
        if resp.status_code != 200:
            raise APIError("Error in getMarketTicker, status code="+str(resp.status_code))
        return resp.json()

    # Function getMarketDepth, Returns A Nested dictionary comprising of the API Results, You can print to see the data
    # Or optionally check the API output from original wazirx api repo (ref. https://github.com/WazirX/wazirx-api)
    def getMarketDepth(self):
        resp = requests.get(API_BASE+API_LINK_MARKET_DEPTH)
        if resp.status_code != 200:
            raise APIError("Error in getMarketDepth, status code="+str(resp.status_code))
        return resp.json()

    # Function getMarketTradeHistory, Returns A Nested dictionary comprising of the API Results, You can print to see the data
    # Or optionally check the API output from original wazirx api repo (ref. https://github.com/WazirX/wazirx-api)
    def getMarketTradeHistory(self):
        resp = requests.get(API_BASE+TRADE_HISTORY)
        if resp.status_code != 200:
            raise APIError("Error in getMarketTradeHistory, status code="+str(resp.status_code))
        return resp.json()



# Boilerplate class to handle exception, You can extend this part to implement custom exception handling and more
# Utilities, Parse the exception into below format (In code)
class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "WZXAPI Error, aborting, message: {}".format(self.status)


# Usage
# api = WZXAPI()
# res = api.getMarketStatus()
# print(res)
