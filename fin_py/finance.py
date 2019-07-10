def futureValue_simple():
    """\nThis funtion calculates the future value\nwith simple interset rate of present value.\nThis will be a financial program!\n"""

    # taking input from the user
    presentValue = int(input("What is your present value:\n"))
    interestRate = float(input("What is your interst rate?\nDo not use '%':"))
    time = int(input("For how many years or months do you want to invest:\n"))

    # Calculations
    rate = (1 + interestRate/100) ** time
    result = rate * presentValue

    # printing out the results
    return "The future value of {} of {} years is '%.3f'".format(
        presentValue, time) % result


def futureValue_compound():
    """\nThis funtion calculates the future value\nwith compound interset rate of present value.\nThis will be a financial tool!\n"""

    # taking input from the user
    presentValue = int(input("What is your present value:\n"))
    interestRate = float(input("What is your interst rate?\nDo not use '%':"))
    time = int(input("For how many years or months do you want to invest:\n"))
    compound = int(input("How many time in a year do you need interest:\n"))

    # Calculations
    rate = (1 + (interestRate/100)/compound) ** (time*compound)
    result = rate * presentValue

    # printing out the results
    return "The future value of {} of {} years is %.3f".format(
        presentValue, time) % result
