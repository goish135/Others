f  = open('a.csv','r',encoding='utf-8')
l = f.readlines()

lista = [] # start
listb = [] # end
listTarget = [] # coach

count = 0 # 貼文數量
row = 0   # 行號
row1 = 0 
row2 = 0 
key_row = 0
for i in l:
	row = row + 1
	if "投稿日期" in i:
		count = count + 1
		lista.append(row)

for j in l:
	row1 = row1 + 1
	if "#靠北排球" in j:
		listb.append(row1)

for k in l:
	key_row = key_row+1
	if "教練" in k:
		listTarget.append(key_row)

#---------------------------------------#		

record = []

for it in listTarget:
	for item in range(0,len(listb)):
		if (item+1)<len(listb) and it > listb[item] and it < listb[item+1] :
				flag = 0 
				#print("start")
				#print(listb[item])
				for e in record:
					if listb[item] == e:
					    flag = 1
				if flag != 1:
					record.append(listb[item])
				#record.append(listb[item])
				#print("end")
				#print(listb[item+1])
				
file = open("out.txt","w",encoding='utf-8')

for a in record:
	#print('a')
	#print(a)
	for b in range(0,len(listb)):
		if a==listb[b]:
			for ans in range(a,listb[b+1]):
				#print(l[ans])
				file.write(l[ans])
	#print(listb[item])

#print(listTarget[0]);

#print('a:')
#print(len(lista))

#print('b:')
#print(len(listb))

#print(len(listTarget))

#for it in listTarget:

#print('sum:')		
#print(count)		
f.close()
		