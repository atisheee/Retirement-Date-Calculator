def age_calculator():
    print("\nYou will be retired in: ",y+gy,"Years, ",m, "Months, ",d,"Days\n")
    print("Total job duration in your hand from now : ", y+gy-cy,"Years,",m-cm, "Months",abs(d-cd), "Days\n")
    print("Thank You.")
while True:
    y=int(input("Enter Your Birth Year:"))
    m=int(input("Enter Your Birth Month Number:"))
    d=int(input("Enter Your Birth Day:"))
    gy=int(input("Enter your Government approved service duration in years: "))

    cy=int(input("Enter Current Year:"))
    cm=int(input("Enter Current Month Number: "))
    cd=int(input("Enter Current Day:"))
    age_calculator()
    break