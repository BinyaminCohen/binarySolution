def MaxZeroBetweemOne(intNum, false=None, ture=None):

    #x = "1111001110100110"
    print(intNum)
    y = bin(intNum).replace("b", "")

    binList = [char for char in y ]
    print(binList)

    couner = 0
    maxZero = 0
    idx = 0
    flag = False

    for i in binList:
        if idx == 0:
            if i == '1':
                flag = True
        else:
            if i == '0' and flag is True:
                couner += 1
            else:
                if flag is True:
                    flag = False
                    if couner > maxZero:
                        maxZero = couner
                        couner = 0
                        if idx < (len(binList) -1) and binList[idx + 1] == '0':
                            flag = True
                else:
                    if idx < (len(binList) -1) and binList[idx + 1] == '0':
                        flag = True

        idx += 1


    print(maxZero)






    #decNum = DecimalToBinary(intNum)


    #print(decNum)









# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #IntNum = genIntNum()
    MaxZeroBetweemOne(1025)


