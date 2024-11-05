voltOne = int(input("Enter the first voltage you want to average: "))
voltTwo = int(input("Enter the second voltage you want to average: "))
voltThree = int(input("Enter the third voltage you want to average: "))
voltFour = int(input("Enter the fourth voltage you want to average: "))
voltFive = int(input("Enter the fifth voltage you want to average: "))

averageVoltage = (voltOne + voltTwo + voltThree + voltFour + voltFive) / 5

if averageVoltage > 220:
    print("ALTO VOLTAJE")
else: 
    print("VOLTAJE CORRECTO")
    