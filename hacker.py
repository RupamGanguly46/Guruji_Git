def is_leap(year):
    if year%4==0:
        print("1loop")
        if year%100==0:
            print("2loop")
            if year%400==0:
                print("3loop")
                return(True)
            else:
                return(False)
        else:
            return(True)
    else:
        return(False)

year = int(input())
print(is_leap(year))