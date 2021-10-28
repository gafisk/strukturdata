import que as qu

jumlah = int(input("Jumlah proses yang akan dijadwal di CPU: "))
proses = []
antrian = qu.queue()

for i in range(jumlah):
  data=[]
  data.append(input("nama proses ke-"+str(i)+" : "))
  data.append(int(input("waktu proses : ")))
  proses.append(data)

print("List Antrian proses : ",proses)

waktu = int(input("Waktu proses CPU : "))
for j in proses:
  qu.enqueue(antrian,j)
print ("Antrian beserta waktu proses :",antrian)

temp=1
while not qu.isEmpty(antrian):
  print ("iterasi ke-"+str(temp)+" :")
  inproses = qu.dequeue(antrian)
  inproses[1] -= waktu
  if inproses[1] < 1:
    print ("proses",inproses[0],"telah selesai diproses")
    print("data proses yang tersisa :",antrian)
  else:
    print ("proses",inproses[0],"sedang diproses, dan sisa waktu proses",inproses[0],"=",inproses[1])
    qu.enqueue(antrian,inproses) 
    print("data proses yang tersisa :",antrian)
  temp += 1
