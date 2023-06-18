class AgeCalculator:
    def __init(self):
        pass
    def AgeCalculatorFunc(self):
        pass
        
class PersonAge:
    def __init__(self,DateofBirth):
        self.DateofBirth = DateofBirth
        print(f"Inside init {DateofBirth} and {type(DateofBirth)}")
    def AgeCalculatorFunc(self):
        Day = int(self.DateofBirth[0])
        Month = int(self.DateofBirth[1])
        Year = int(self.DateofBirth[2])
        print (f"Inside the class {Day}/{Month}/{Year}")
        DateAge = int(1)
        MonthAge = int(1)
        YearAge = int(2023)
        if Month > MonthAge and Day > DateAge:
            MonthAge_ = 12 - Month
            YearAge_ = YearAge - (Year+1) 
            DateAge_ = 31 - (Day-1)
        elif  Month == MonthAge and Day > DateAge :
            YearAge_ =  Year - (YearAge-1)
            MonthAge_ = 12 - Month
            DateAge_ = 31 - (Day-1)
        else:
            MonthAge_ = Month - MonthAge
            YearAge_ = YearAge- Year
            DateAge_ = Day - DateAge

        return [DateAge_, MonthAge_,YearAge_ ]

def main():
    while(1):
        getDateMonthYear = getPersonsDayMonthYear()
        DateofBirth_is = str(getDateMonthYear[0]) +"-" +str(getDateMonthYear[1]) + "-" + str(getDateMonthYear[2])
        print(f"Pesrons date of Birth is {DateofBirth_is}")
        AgeofPerson = PersonAge(getDateMonthYear)
        agecalculated = AgeofPerson.AgeCalculatorFunc()
        print(f"You are {agecalculated[2]} years {agecalculated[1]} months {agecalculated[0]} days old")

def getPersonsDayMonthYear():
    day = int(input("Enter When is Your Date of Birth Accepted Values 1-31\n"))
    month = int(input("Enter When is Your month of Birth Accpted Values - 1-12\n"))
    Year = int(input("Enter When is your Year of Birth\n"))
    return [day,month,Year]

    
    
if __name__ == "__main__":
    main()