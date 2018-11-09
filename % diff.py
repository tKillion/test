def percentDiff(numA,numB):
   return (numA-numB)/((numA+numB)/2)*100


while(True):
    x=float(input("nominal: "))
    y=float(input("measured: "))
    print(percentDiff(x,y))
