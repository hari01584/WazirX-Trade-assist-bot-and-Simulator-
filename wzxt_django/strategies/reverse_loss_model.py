# 01-05-2021
# Basic WazirX Trading Bot/Simulator Template File, Written By Harishankar Kumar (https://github.com/hari01584)
# Extend as you wish
from wzxt_bgworker.models import Economy
from wzxt_bgworker.models import Transaction
from decimal import Decimal

class strategy:
    # Some default variables, dont remove these
    data = {}
    result = []
    instanceName=""
    isSimulation = False
    baseCurrency = "inr"
    baseCurrencyAmt = 0
    extras = {}

    targetMarkets = []
    # Define your script specific variables/ configuration variables below, these are useful for having
    # Custom configuration and variables! Good for extensions! :D
    #maxPaymentLimit = 0

    # Initiliaze the template parameters, these parameters can be used in algorithm to make investment or sell
    # them, Optionally there's also *extras* parameter which can be used to pass extra information required by
    # the script, You can set a json property for a script file with key named "extras" and anything inside it
    # will be sent to the respective basic template script!
    eco = None
    PARAM_MINI_BALANCE = 400
    BUY_MARKET_LOWER_BOUND = -20
    INDIVIDUAL_TRANS_MONEY = 100

    BENEFIT_MARGIN_EACH_TRANS = 5

    def __init__(self, data, instanceName, isSimulation, baseCurrency, baseCurrencyAmt, extras = {}):
        # Nothing to do rn, add your initilizing algoritms/depedency here
        self.data = data
        self.instanceName = instanceName
        self.isSimulation = isSimulation
        self.baseCurrency = baseCurrency
        self.baseCurrencyAmt = baseCurrencyAmt
        self.extras = extras

        # Parse the extras (if sending any) here, and set custom variables from extras here! Useful for many stuff
        # ie you can set a custom config variable which set amount of total money be used for each transaction which
        # Should be user provided, so you can set a variable from parsing extras, which is supposely fed from config!
        # maxPaymentLimit = extras["maxLimit"]
        #<----- reverse_loss_model specifics------>
        try:
            self.targetMarkets = self.extras["targetMarket"]
        except Exception as e:
            raise Exception("Perhaps you are missing some parameters in config?" +
            "Make sure to look at this script's source and see examples for config.json!!"+
            "\n Aborting reverse_loss_model")

        self.eco = Economy.objects.filter(instance_name=self.instanceName,currencyBase=self.baseCurrency).first()
    # Main body of algorithm, do some work and generate action list, which gives back
    # and tells the other python files what to do!
    def execute(self):
        # Do some logic here
        marketTicker = self.data["getMarketTicker"]
        res = [val for key, val in marketTicker.items() if self.baseCurrency.lower() in key]
        for market in res:
            if(market["type"] != "SPOT"): continue
            try:
                perc = ((float(market["last"])   -  float(market["open"])) / (float(market["last"]))) *100
            except:
                continue

            #print(market,"\n% INC ", perc,"\n\n")
            cryp = Transaction.objects.filter(instance_name=self.instanceName,currency=market["base_unit"]+market["quote_unit"])
            if(self.eco and self.eco.amount > self.PARAM_MINI_BALANCE):
                if(perc*(float(market["last"])) < self.BUY_MARKET_LOWER_BOUND):
                    if(not cryp):
                        self.buyActionExecuteMinAsset(market)


            for cryTrans in cryp:
                margin = Decimal(market["last"]) - cryTrans.rate
                if(margin > 0):
                    totalSellVirt = Decimal(market["last"]) * cryTrans.volume
                    benefit = totalSellVirt*Decimal(1.002)  - self.INDIVIDUAL_TRANS_MONEY - self.BENEFIT_MARGIN_EACH_TRANS
                    if(benefit > 0):
                        print("I see a benefit, Margin=",margin,"Totaility:",margin*cryTrans.volume, "Total:",totalSellVirt)
                        print("Coin deetail=",market["base_unit"]+market["quote_unit"],"Net Benefit=",benefit)

        return self.result;


    def buyActionExecuteMinAsset(self, market):
        print("buy",market["base_unit"])
        volume = self.INDIVIDUAL_TRANS_MONEY / float(market["last"])
        action = {"side":"buy","ord_type":"limit","price":str(market["last"]),"volume":str(volume),"market":market["base_unit"]+market["quote_unit"]}

        self.eco.amount -= Decimal(self.INDIVIDUAL_TRANS_MONEY * 1.02)
        self.eco.save()

        self.result.append(action.copy())
