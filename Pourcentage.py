#-----Part=numerator---Total=denominator-------
part = float(input("Enter the part value: "))
total = float(input("Enter the total value: "))

percentage = (part / total) * 100
print(f"Percentage: {percentage: .3f}%")