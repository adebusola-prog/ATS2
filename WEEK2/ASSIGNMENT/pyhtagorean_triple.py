def pythagorean_triple(adjacent, opposite, hypothenus):
   for i in range(1, adjacent+1):
      for j in range(1, opposite+1):
         for k in range(1, hypothenus+1):
            if ((i **2) + (j ** 2) == (k ** 2)):
               print(i, j, k)

pythagorean_triple(20,20,20)
