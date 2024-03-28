from yahoo_finance import Share

class YahooData:
    def __init__(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate

    def getYahooData(self, keyword):
        yahoo = Share(keyword)
        historical_data = yahoo.get_historical(self.startDate, self.endDate)
        return historical_data