
class strategy:
    data = {}
    result = []
    instanceName=""
    isSimulation = False
    baseCurrency = "INR"

    def __init__(self, data, instanceName, isSimulation, baseCurrency):
        # Nothing to do rn, add your initilizing algoritms/depedency here
        self.data = data
        self.instanceName = instanceName
        self.isSimulation = isSimulation
        self.baseCurrency = baseCurrency


    # Main body of algorithm, do some work and generate nested actions list, which gives back
    # and tells the other python files what to do!
    def execute(self):
        # Do some logic here
        action = {"type":"buy","currencyBase":"INR","targetCurrency":"BTC","amount":20, "exchangeRate":470047}
        self.result.append(action.copy())
        return self.result;
