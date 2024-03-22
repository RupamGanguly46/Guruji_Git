# try:
#     print("start")
#     print("no error")
#     print("after error")
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")

while 1:
    try:
        a=4
        b=int(input("Enter number or letter"))
        out=a/b
        print(out)
        break
    except ZeroDivisionError as e:
        print("Error:",e)
    except ValueError as e:
        print("Error:",e)
    else:
        print("No error")
    finally:
        print("finished")
    print("loop")


