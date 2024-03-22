# Map() function

List1=input("Enter numbers seperated by spaces :").split()
print(f"{List1=}")

Map=map(int,List1)
print(f"{Map=}")

# Visualising Mapping

# 1st method
# Type Casting (List/Tuple)
print("\n1st Method")
List2=list(Map)
print(f"{List2=}")

# Once a map is printed completely the map gets emptied. So create map again.

# 2nd method
# Next function
print("\n2nd Method")
Map=map(int,List1)
nex1=next(Map)
nex2=next(Map)
print(nex1,nex2)

# 2 elements of map have been printed/utilised. 2 more remaining in the map for furthur use.

# 3rd method
# Looping
print("\n3rd Method")
for i in Map:
    print(i)