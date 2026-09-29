x=int(input())
y=int(input())
if x>0 and y>0:
    print("This point lies in first quadrant.")
elif x<0 and y>0:
    print("This point lies in second quadrant.")
elif x<0 and y<0:
    print("This point lies in third quadrant.")
elif x>0 and y<0:
    print("This point lies in fourth quadrant.")
else:
    print("This point lies in origin.")