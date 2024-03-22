#Bridge Toll Management System

print('''1. Add Vehicle Entry
2. Display Vehicle Entries
3. Calculate Total Toll Collection
4. Search Vehicle by Number
5. Exit''')

manager=dict()

while True:
    ch=int(input("Enter choice"))
    if ch==1:
        veh_no=input("Enter Vehicle Number:")
        veh_type=input("Enter Vehicle Type (Car/Truck/Bus):")
        toll_amt=input("Enter Toll Amount:")
        manager.update({veh_no:[veh_type,toll_amt]})
    
    elif ch==2:
        print("Vehicle Entries:")
        for i in range(len(manager)):
        
            print("Vehicle Number:",list(manager.keys())[i])
            print("Vehicle Type:",list(manager.values())[i][0])
            print(f"Toll Amount: ${list(manager.values())[i][1]}\n")
    
    elif ch==3:
        total=0
        for i in range(len(manager)):
            total+=float(list(manager.values())[i][1])
        print(f"Total Toll Collection: ${total}")

    elif ch==4:
        veh_no=input("Enter Vehicle Number to Search:")
        print("Vehicle Details:")
        print("Vehicle Number:",veh_no)
        print("Vehicle Type:",manager.get(veh_no)[0])
        print("Toll Amount:",manager.get(veh_no)[1])
    
    elif ch==5:
        break
