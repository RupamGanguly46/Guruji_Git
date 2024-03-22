units = int(input(" Please enter Number of Units you Consumed : "))

if(units <= 50):
    amount = units * 0.50
elif(units <= 150):
    amount = 50*0.50 + ((units - 50) * 0.75)
elif(units <= 250):
    amount = 50*0.50 + 100*0.75 + ((units - 150) * 1.20)
else:
    amount = 50*0.50 + 100*0.75 + 100*1.20 + ((units - 250) * 1.50)
surcharge=0.2*amount
total = amount + surcharge
print("\nElectricity Bill = %.2f"%total)
