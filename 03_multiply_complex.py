def multComplex(num1, num2):
    real1, imag1 = num1
    real2, imag2 = num2
    real3 = (real1 * real2) - (imag1 * imag2)
    imag3 = (real1 * imag2) + (real2 * imag1)
    if imag3 >= 0:
        result = f"{real3} + i{imag3}"
    else:
        imag3 *= -1
        result = f"{real3} - i{imag3}"
    return result

def splitNum(numInp):
    num = numInp.replace(" ", "")
    plusPos = num.find("+", 1)
    minusPos = num.find("-", 1)
    
    if plusPos != -1:
        splitPos = plusPos
    elif minusPos != -1:
        splitPos = minusPos

    real = float(num[:splitPos])
    if num[splitPos+2:] != "":
        imag = float(num[splitPos+2:])
    else:
        imag = 1

    if minusPos != -1:
        imag *= -1

    return (real, imag)

#if input = x + iy
num1 = input()
num2 = input()
splitNum1 = splitNum(num1)
splitNum2 = splitNum(num2)
print(multComplex(splitNum1, splitNum2))

#if input = real imag
# num1 = map(float, input().split())
# num2 = map(float, input().split())
#print(multComplex(num1, num2))