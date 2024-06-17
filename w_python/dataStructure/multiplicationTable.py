import numbers

## 구구단 연습
def func_test():
        while True:
            inPut_num = (input("구구단 출력을 위한 숫자를 입력해 주세요.(0 입력시 종료) : "))
            try:
                isInt = new_func(inPut_num) # 정수 겁사
                if( isInt ) :
                    if(int(inPut_num) != 0):
                        print("******%d 단 출력합니다 ******" %int(inPut_num))
                        func_MULTIPLICATION(int(inPut_num))
                    elif (int(inPut_num) == 0):
                        print("입력값 : %d"%int(inPut_num))
                        print("구구단을 종료합니다.")
                        break
            except ValueError: #정수가 아닌 값이 나올 경우 대처
                print("정수가 아닌 수를 입력하였습니다. (입력값 : %s)" %inPut_num)
                print("다시 입력해 주세요.") 
    
def new_func(inPut_num):
    isInt = isinstance(int(inPut_num), numbers.Integral)
    return isInt             
    
def func_MULTIPLICATION(a):
    i = 1;
    value = 0
    while i < 10:
        print("{0} x {1} = {2} ".format(a,i, a*i ))
        i += 1

func_test()