
def miles_per_gallon():
   all_miles=[]
   all_gallons=[]
   while 1:
      miles= int(input("enter the miles used"))
      gallons=int(input("enter the gallons used"))
      print("The miles/gallon for this tank was", miles/gallons)
      if gallons == -1:
         break
      all_miles.append(miles)
      all_gallons.append(gallons)

   print("the overall average miles/gallons", sum(all_miles)/ sum(all_gallons))

miles_per_gallon()