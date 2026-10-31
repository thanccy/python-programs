
# Electricity Bill Calculation with Exception Handling

try:
    units = float(input("Enter the electricity units consumed: "))

    if units < 0:
        raise ValueError("Units cannot be negative")

except ValueError as e:
    print("Invalid input:", e)

else:
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 5)

    print("Electricity units consumed:", units)
    print("Total electricity bill: Rs.", bill)

finally:
    print("Electricity bill calculation completed.")
