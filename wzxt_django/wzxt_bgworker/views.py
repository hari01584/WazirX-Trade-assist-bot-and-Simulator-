from django.shortcuts import render
from wzxt_bgworker.API import WZXAPI
from wzxt_bgworker.configManager import myConfig
from importlib import import_module

# Create your views here.
def doTrans(instance_id):
    api = WZXAPI()
    res = api.getMarketStatus()

    cls = getattr(import_module('strategies.'+myConfig.getStrategyFile()[:-3]), 'strategy')
    stra = cls()

    print(())
