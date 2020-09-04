# Add two number
def two_num(lis1, lis2):
    # reverse the order of both lists
    # print()
    lis1 =lis1[::-1]
    lis2 = lis1[::-1]
    #convert into single digit
    string=(str(int) for int in lis1)
    string2=(str(int) for int in lis2)
    int1=int("".join(string))
    int2 = int("".join(string2))
    output=int1+int2
    output= list(map(int, str(output)))
    # reverse and return output
    return print(output[::-1])
two_num([1,2,3],[1,4,2])