def func_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif  n%2 ==0 and n in range(2,5):
        print("Not Weird")
    elif n%2 ==0 and n in range(6,20):
        print("Weird")
    elif n%2 ==0 and n > 20:
        print("Not Weird")
    else:
        print("Not Weird")

func_weird(3)
func_weird(24)
func_weird(45)
func_weird(50)