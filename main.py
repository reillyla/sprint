#Newfoundland Chocolate Company Travel Claims Processing System
#Author: Reilly Lane

def chocolateCompany():

    userChoice = ""
    while userChoice != (1, 5):
        print("1. Enter employee travel claim.")
        print("2. Fun interview question.")
        print("3. Cool stuff with string & dates.")
        print("4. Something old, Something New.")
        print("5. Quit Program.")
        print()
        userChoice = input("Please enter a number between 1-5: ")
        if userChoice == "1":
            etClaim()
            break
        elif userChoice == "2":
            funIQ()
            break
        elif userChoice == "3":
            coolStuff()
            break
        elif userChoice == "4":
            graphClaims()
            break
        elif userChoice == "5":
            break
        else:
            print("Error: Please enter a number between 1-5.")
            chocolateCompany()


def etClaim():

    import datetime

    # User Inputs:
    empNum = str(input("Please enter the employee number: "))
    while len(empNum) != 5:
        print("Error: Employee number must be 5 characters.")
        empNum = input("Please enter the employee number: ")
    empNum = str(empNum)
    empFName = input("Please enter the employee's first name: ").title()
    empLName = input("Please enter the employee's last name: ").title()
    tripLoc = input("Please enter the trip location: ").title()
    # Trip Start Date:
    tripSDate = str(input("Please enter the trips start date in the following format: YYYY-MM-DD "))
    while tripSDate != "":
        try:
            datetime.datetime.strptime(tripSDate, "%Y-%m-%d")
            break
        except ValueError:
            print("This is the incorrect date format. It should be YYYY-MM-DD")
            tripSDate = input("Please enter the trips start date in the following format: YYYY-MM-DD")
        tripSDate = str(tripSDate)
    # Trip End Date:
    tripEDate = str(input("Please enter the trips end date in the following format: YYYY-MM-DD "))
    while tripEDate != "":
        try:
            datetime.datetime.strptime(tripEDate, "%Y-%m-%d")
            pass
        except ValueError:
            print("This is the incorrect date format. It should be YYYY-MM-DD")
            tripEDate = input("Please enter the trips end date in the following format: YYYY-MM-DD ")
        # To make sure end date is within 7 days of start date
        tripStartDays = datetime.datetime.strptime(tripSDate, "%Y-%m-%d")
        tripEndDays = datetime.datetime.strptime(tripEDate, "%Y-%m-%d")
        tripdeltaDays = (tripEndDays - tripStartDays).days
        if tripdeltaDays >= 1 and tripdeltaDays <= 7:
            break
        elif tripdeltaDays > 7:
            print("Error: Trip end date must be within 7 days of the start date.")
            tripEDate = input("Please enter the trips end date in the following format: YYYY-MM-DD ")
        tripEDate = str(tripEDate)

    # Function to validate own car or rental input
    def getCarUsed():
        carUsed = input("Please specify if own vehicle was used or a rental('O' for own,'R' for rental): ").upper()
        carTypes = 'OR'
        while len(carUsed) != 1 or carUsed not in carTypes:
            print("Error: Please enter O or R.")
            carUsed = input("Please specify if own vehicle was used or a rental('O' for own,'R' for rental): ").upper()
        return carUsed
    theCarUsed = getCarUsed()

    while theCarUsed == "O":
        totalKMtrav = int(input("Please enter the total kilometers travelled: "))
        if totalKMtrav <= 2000:
            break
        elif totalKMtrav > 2000:
            print("Error: Total kilometers must not exceed 2000.")
        totalKMtrav = int(totalKMtrav)
    if theCarUsed == "R":
        pass

    # Function to validate claim type input
    def getClaimType():
        claimType = input("Please enter the claim type as standard or executive('S' for standard, 'E' for executive): ").upper()
        claimTypes = 'SE'
        while len(claimType) != 1 or claimType not in claimTypes:
            print("Error: Please enter E or S.")
            claimType = input("Please enter the claim type as standard or executive('S' for standard, 'E' for executive): ").upper()
        return claimType
    theClaimType = getClaimType()

    from datetime import date
    # Finding day of year to see if input trip start date is between December 15th-22nd
    tripSDate_str = date(*map(int, tripSDate.split('-')))
    tripSDate_dayOfYear = tripSDate_str.timetuple().tm_yday
    dateRangeBeg_dayOfYear = date(tripSDate_str.year, 12, 15).timetuple().tm_yday
    dateRangeEnd_dayOfYear = date(tripSDate_str.year, 12, 22).timetuple().tm_yday
    # Constants and Equations:
    bonus = 0
    tax = 0.15
    mileageCost = 0
    sdateDays = datetime.datetime.strptime(tripSDate, "%Y-%m-%d")
    edateDays = datetime.datetime.strptime(tripEDate, "%Y-%m-%d")
    totalTripDays = (edateDays - sdateDays).days

    if theClaimType == "E":
        bonus += (45.00 * totalTripDays)
    elif theClaimType == "S":
        bonus += 0

    if theCarUsed == "O":
        mileageCost = (0.17 * totalKMtrav)
    elif theCarUsed == "R":
        mileageCost = (65.00 * totalTripDays)

    if theCarUsed == "O" and totalKMtrav > 1000:
        bonus += (0.04 * totalKMtrav)

    if totalTripDays > 3:
        bonus += 100

    if dateRangeBeg_dayOfYear <= tripSDate_dayOfYear <= dateRangeEnd_dayOfYear:
        bonus += (50.00 * totalTripDays)

    perDiemAmount = (totalTripDays * 85.00)
    claimAmount = perDiemAmount + mileageCost + bonus
    hst = (tax * perDiemAmount)
    claimTotal = (claimAmount + hst)

    # Print Statements:
    print(f"Employee Number: {empNum}")
    print(f"Employee Name: {empFName} {empLName}")
    print("Trip Location:", tripLoc)
    print(f"Trip Duration: {totalTripDays} Days")
    print(f"Trip Start Date: {sdateDays.strftime('%B %d, %Y')}")
    print(f"Trip End Date: {edateDays.strftime('%B %d, %Y')}")
    print("Rental or Own Vehicle:", theCarUsed)
    if theCarUsed == "O":
        print("Total Kilometers Travelled:", totalKMtrav)
    print("Claim Type:", theClaimType)
    print(f"Per Diem Amount:{f'${perDiemAmount:.2f}':>18s}")
    print(f"Mileage Cost:{f'${mileageCost:.2f}':>21s}")
    print(f"Bonus:{f'${bonus:.2f}':>28s}")
    print(f"Claim Amount:{f'${claimAmount:.2f}':>21s}")
    print(f"HST:{f'${hst:.2f}':>30s}")
    print(f"Claim Total:{f'${claimTotal:.2f}':>22s}")
    anotherClaim = input("Would you like to enter another sales claim? Enter 'y' for yes, or 'n' for no: ").upper()
    if anotherClaim == "Y":
        etClaim()
    elif anotherClaim == "":
        print("Error. Input must not be blank.")
    elif anotherClaim == "N":
        chocolateCompany()


def funIQ():
    for i in range(1, 101):
        if i % 5 == 0 and i % 8 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 8 == 0:
            print("Buzz")
        else:
            print(i)
    mainMenu = input("Press enter to continue...")
    if mainMenu == "":
        chocolateCompany()


def coolStuff():

    import datetime

    # User Input:
    empFName = input("Please enter the employee's first name: ").title()
    empLName = input("Please enter the employee's last name: ").title()
    empPhoneNum = str(input(" Please enter the employee's 10-digit phone number: "))
    while len(empPhoneNum) != 10 or (not empPhoneNum.isdigit()):
        print(" Error: This is not a 10-digit phone number.")
        empPhoneNum = input(" Please enter the employee's 10-digit phone number:")
    empPhoneNum = str(empPhoneNum)
    empStartDate = input("Please enter the employee's start date in the following format: YYYY-MM-DD ")
    while empStartDate != "":
        try:
            datetime.datetime.strptime(empStartDate, "%Y-%m-%d")
            break
        except ValueError:
            print("This is the incorrect date format. It should be YYYY-MM-DD")
            empStartDate = input("Please enter the employee's start date in the following format: YYYY-MM-DD ")
        empStartDate = str(empStartDate)
    empBDay = input("Please enter the employee's birthday in the following format: YYYY-MM-DD ")
    while empBDay != "":
        try:
            datetime.datetime.strptime(empBDay, "%Y-%m-%d")
            break
        except ValueError:
            print("This is the incorrect date format. It should be YYYY-MM-DD")
            empBDay = input("Please enter the employee's birthday in the following format: YYYY-MM-DD ")
        empBDay = str(empBDay)

    # Equations:
    currentDate = str(datetime.date.today())
    empBDayeq = datetime.datetime.strptime(empBDay, "%Y-%m-%d")
    currentDatedayseq = datetime.datetime.strptime(currentDate, "%Y-%m-%d")
    empStartDatedayseq = datetime.datetime.strptime(empStartDate, "%Y-%m-%d")
    daysWorked = (currentDatedayseq - empStartDatedayseq).days
    birthday = datetime.datetime(currentDatedayseq.year, empBDayeq.month, empBDayeq.day)
    days_until_birthday = (birthday - currentDatedayseq).days
    days_alive = (currentDatedayseq - empBDayeq).days
    hoursWorked = (daysWorked * 8)

    # Print Statements:
    print(f"Employee Name: {empFName} {empLName[:1]}.")
    print(f"Employee Phone Number: {empPhoneNum[3:]}")
    print(f"Current Date and Time: {currentDatedayseq.strftime('%A %b %-d %Y')}")
    print(f"Employee Start Date: {empStartDatedayseq.strftime('%B %-d, %Y')}")
    print(f"Employee Birthday: {empBDayeq.strftime('%B %-d, %Y')}")
    print(f"Total Days Worked: {daysWorked:>} days ({hoursWorked:>} hours)")
    print(f"You are {days_alive} days old.")
    if days_until_birthday > 0:
        print(f"Only {days_until_birthday} days until your birthday!!")
    elif days_until_birthday == 0:
        print(f"Happy Birthday {empFName.title()}!!!")
    else:
        print("Your birthday has already passed you'll have to wait until next year for another birthday :(")
    mainMenu = input("Press enter to continue...")
    if mainMenu == "":
        chocolateCompany()


def graphClaims():

    # Use matplotlib to graph monthly claims based on users input:
    import matplotlib.pyplot as plt

    x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y_axis = []

    for months in range(1, 13):

        while True:
            try:
                monthlySales = float(input("Please enter the monthly sales total for " + x_axis[months - 1] + ": "))
                break
            except ValueError:
                print("Input must be a numeric value.")
        y_axis.append(monthlySales)

    plt.title("Monthly Claims Totals", fontsize=20)
    plt.plot(x_axis, y_axis, "indigo", marker=".")
    plt.ylim(ymin=0)
    plt.xlabel("Months from Jan-Dec", fontsize=16)
    plt.ylabel("Monthly Sales Totals", fontsize=16)
    plt.grid(True)
    plt.show()
    print()
    mainMenu = input("Press enter to continue...")
    if mainMenu == "":
        chocolateCompany()


chocolateCompany()
