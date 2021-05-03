from wzxt_bgworker.configManager import myConfig
from importlib import import_module
from wzxt_bgworker.API import WZXAPI
from wzxt_bgworker.models import Transaction
from wzxt_bgworker.models import Economy
from decimal import Decimal
import datetime

def moneyWallet(ins_name):
    try:
        me = Economy.objects.get(instance_name=ins_name)
        return me
    except Exception as e:
        raise OperationError("Error, base money not set for instance "+ins_name)

def liveline():
    api = WZXAPI()
    data = api.getMultipleApiData(myConfig.getApiRequired())

    bCurren = myConfig.getBaseCurrency()
    all_strategies = myConfig.getStrategyFile()

    for strategy in all_strategies:
        name = strategy["name"]
        wallet = moneyWallet(name)
        isSim = strategy["isSimulation"]
        extras = {}
        if("extras" in strategy):
            extras = strategy["extras"]

        cls = getattr(import_module('strategies.'+strategy["file"][:-3]), 'strategy')
        stra = cls(data, name, isSim, bCurren, wallet.amount, extras)
        for action in stra.execute():
            processAction(action, name, isSim, bCurren)


def processAction(action, name, isSim, bCurren):
    print("Name %s, Action Type:%s, isSimulated:%d"%(name,action["type"],isSim))
    if(action["type"] == "buy"):
        transc = Transaction()
        transc.instance_name = name
        transc.transationType = "buy"
        transc.currency = action["targetCurrency"]
        transc.time = datetime.datetime.now()
        transc.money = Decimal(200.0)
        transc.rate = Decimal(2.1244)
        transc.save()


class OperationError(Exception):
    """An OperationError Exception"""
    def __init__(self, status):
        self.status = status
    def __str__(self):
        return "WZXAPI Operation Error, aborting, message: {}".format(self.status)
