from datetime import datetime
from dateutil import relativedelta
from datetime import datetime, timedelta,date
from dateutil.parser import parse
from datetime import datetime
from dateutil import relativedelta

class AgeCalculator:
    def __init(self):
        pass
    def AgeCalculatorFunc(self):
        pass
        
class PersonAge:
    def __init__(self,Todays_Date,DateofBirth):
        self.DateofBirth = DateofBirth
        self.Todays_Date = Todays_Date
        print(f"Inside init {DateofBirth} and {type(DateofBirth)}")
    def AgeCalculatorFunc(self):
        # Get the relativedelta between two dates
        delta = relativedelta.relativedelta(self.Todays_Date, self.DateofBirth)
        print('Years, Months, Days between two dates is')
        print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
        return delta

def main():
    while(1):
        getDateMonthYear = getPersonsDayMonthYear()
        DateofBirth_is = str(getDateMonthYear[0]) +"-" +str(getDateMonthYear[1]) + "-" + str(getDateMonthYear[2])
        #print(f"Pesrons date of Birth is {DateofBirth_is}")
        Todays_Date = date.today()
        print(f'Todays Date is {Todays_Date}')
        # convert string to date object
        start_date = datetime.strptime(DateofBirth_is, "%Y-%m-%d")
        #end_date = datetime.strptime(Todays_Date, "%d/%m/%Y")
        AgeofPerson = PersonAge(Todays_Date,start_date)
        agecalculated = AgeofPerson.AgeCalculatorFunc()
        #print(f"You are {agecalculated[0]} years {agecalculated[1]} months old")

def getPersonsDayMonthYear():
    day = int(input("Enter When is Your Date of Birth Accepted Values 1-31\n"))
    month = int(input("Enter When is Your month of Birth Accpted Values - 1-12\n"))
    Year = int(input("Enter When is your Year of Birth\n"))
    return [Year,month,day]

    
    
if __name__ == "__main__":
    main()