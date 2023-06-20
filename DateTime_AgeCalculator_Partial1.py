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
        try:
            birthday = self.DateofBirth.replace(year = self.Todays_Date.year)
            print(f"Birthd date is {birthday}")
            # raised when birth date is February 29
            # 	# and the current year is not a leap year
        except ValueError:
             birthday = self.DateofBirth.replace(year = self.Todays_Date.year,month = self.DateofBirth.month + 1, day = 1)
        if birthday > self.Todays_Date:
            return [self.Todays_Date.year - self.DateofBirth.year - 1, (12+(self.Todays_Date.month - self.DateofBirth.month - 1))]
        else:
	        return [self.Todays_Date.year - self.DateofBirth.year, self.Todays_Date.month - self.DateofBirth.month]
def main():
    while(1):
        getDateMonthYear = getPersonsDayMonthYear()
        #DateofBirth_is = str(getDateMonthYear[0]) +"-" +str(getDateMonthYear[1]) + "-" + str(getDateMonthYear[2])
        #print(f"Pesrons date of Birth is {DateofBirth_is}")
        Todays_Date = date.today()
        AgeofPerson = PersonAge(Todays_Date,date(getDateMonthYear[0],getDateMonthYear[1],getDateMonthYear[2]))
        agecalculated = AgeofPerson.AgeCalculatorFunc()
        print(f"You are {agecalculated[0]} years {agecalculated[1]} months old")

def getPersonsDayMonthYear():
    day = int(input("Enter When is Your Date of Birth Accepted Values 1-31\n"))
    month = int(input("Enter When is Your month of Birth Accpted Values - 1-12\n"))
    Year = int(input("Enter When is your Year of Birth\n"))
    return [Year, month, day]

    
    
if __name__ == "__main__":
    main()

##Testcase tried
#DD/MM/YYYY
#1. 1/1/1989
#2. 26/1/1989
# 3. 26/7/1989
#4. 19/9/1998