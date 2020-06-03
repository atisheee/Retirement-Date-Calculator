import datetime

def age_calculator():
    print("\nYou will be retired in: ",y+gy,"Years, ",m, "Months, ",d,"Days\n")
    print("Total job duration in your hand from now : ", y+gy-cy,"Years,",m-cm, "Months",abs(d-cd), "Days\n")
    print("Thank You.")
while True:
    #birth_date=int(input("Enter your date of birth in format of dd/mm/yyyy:"))
    y=int(input("Enter Your Birth Year:"))
    m=int(input("Enter Your Birth Month Number:"))
    d=int(input("Enter Your Birth Day:"))
    gy=int(input("Enter your Government approved service duration in years: "))

    import datetime

    today = str(datetime.datetime.today())
    #print(today)
    cy=int(today[0:4])
    cm=int(today[5:7])
    cd=int(today[8:10])

    age_calculator()
    break

