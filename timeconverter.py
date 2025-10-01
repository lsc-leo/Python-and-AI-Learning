def timeConv(inputAmount, inputMetric, desiredOutput):
    if (inputMetric == "sec"):
        if desiredOutput == "min":
            result = inputAmount / 60
        elif (desiredOutput == "h"):
            result = inputAmount / 60 / 60
        elif (desiredOutput == "days"):
            result = inputAmount / 60 / 60 / 24
        elif desiredOutput == "weeks":
            result = inputAmount / 60 / 60 / 24 / 7
        else:
            result == "INVALID output"
    elif inputMetric == "min":
        if desiredOutput == "sec":
            result = inputAmount * 60
        elif desiredOutput == "h":
            result = inputAmount / 60
        elif desiredOutput == "days":
            result = inputAmount / 60 / 24
        elif desiredOutput == "weeks":
            result = inputAmount / 60 / 24 / 7
        else:
            result == "INVALID output"
    elif inputMetric == "h":
        if desiredOutput == "sec":
            result = inputAmount * 3600
        elif desiredOutput == "min":
            result = inputAmount * 60
        elif desiredOutput == "days":
            result = inputAmount / 24
        elif desiredOutput == "weeks":
            result = inputAmount / 24 / 7
        else:
            result == "INVALID output"
    elif inputMetric == "days":
        if desiredOutput == "sec":
            result = inputAmount * 60 * 60 * 24
        elif desiredOutput == "min":
            result = inputAmount * 60 * 24
        elif desiredOutput == "h":
            result = inputAmount * 24
        elif desiredOutput == "weeks":
            result = inputAmount / 7
        else:
            result == "INVALID output"
    elif inputMetric == "weeks":
        if desiredOutput == "sec":
            result = inputAmount * 60 * 60 * 24 * 7
        elif desiredOutput == "min":
            result = inputAmount * 60 * 24 * 7
        elif desiredOutput == "h":
            result = inputAmount * 24 * 7
        elif desiredOutput == "days":
            result = inputAmount * 7
        else:
            result == "INVALID output"
    else:
        result == "INVALID input"
    if type(result) != str and result % 1 == 0:
        result = int(result)
    return result

num1 = float(input("Input the desired number: "))
met = input("Input the type of metric, i.e. 'sec', 'min', 'h', 'days', 'weeks': ")
desOut = input("Input the desired output metric, i.e. 'sec', 'min', 'h', 'days', 'weeks': ")

res = timeConv(num1, met, desOut)

print(res)