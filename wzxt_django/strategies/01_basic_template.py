# 01-05-2021
# Basic WazirX Trading Bot/Simulator Template File, Written By Harishankar Kumar (https://github.com/hari01584)
# Extend as you wish

class strategy:
    # Some default variables, dont remove these
    data = {}
    result = []
    instanceName=""
    isSimulation = False
    baseCurrency = "INR"
    baseCurrencyAmt = 0
    extras = {}

    # Define your script specific variables/ configuration variables below, these are useful for having
    # Custom configuration and variables! Good for extensions! :D
    #maxPaymentLimit = 0

    # Initiliaze the template parameters, these parameters can be used in algorithm to make investment or sell
    # them, Optionally there's also *extras* parameter which can be used to pass extra information required by
    # the script, You can set a json property for a script file with key named "extras" and anything inside it
    # will be sent to the respective basic template script!
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

    # Main body of algorithm, do some work and generate action list, which gives back
    # and tells the other python files what to do!
    def execute(self):
        # Do some logic here

        print("Current money: %f"%self.baseCurrencyAmt)
        action = {"type":"buy","currencyBase":"INR","targetCurrency":"BTC","amount":20, "exchangeRate":470047}
        self.result.append(action.copy())
        return self.result;
