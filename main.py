firstVolt = int(input("Enter the first volt: "))
secondVolt = int(input("Enter the second volt: "))
thirdVolt = int(input("Enter the third volt: "))

averageVolt = (firstVolt + secondVolt + thirdVolt) / 3 

if averageVolt < 115:
    print("VOLTAJE CORRECTO")
elif averageVolt > 115 and averageVolt < 220:
    print("ALTO VOLTAJE")
elif averageVolt > 220:
    print("PELIGRO")