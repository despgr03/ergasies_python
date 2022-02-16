import string,re
f = open("LICENSE.txt")
new = f.read()
f.close()   
kai = re.sub(r'[^A-Za-z ]+', ' ', new)
data = kai.split()
#afou xoriso to keimeno se mia lista arxikopoio tis metablhtes mou
string = ""
sumzugoi = 0
sum3 = 0
sum5 = 0
sum7 = 0
#pairno ka8e gramma apo ka8e le3h kai ton metatrepo se akolou8ia ari8mon 0 kai ena 7 bits kai ta apo8hkeuo sth metablhth string
for i in range(0,len(data)):
    for x in data[i]:
        le3 = bin(ord(x))
        le3 = le3[2:]
        while len(le3)<7 :
            le3 = str(0)+le3
        string = string + le3[:2]+le3[5:]       
if len(string.encode("utf8"))//16<len(string.encode("utf8"))/16:#elegxo an mporoun na dhmiourgh8oun akolou8ies ton 16 bits akribos allios na pros8eso mhdenika mprosta apo thn teleutaia
    data3 = string
    data2 = [data3[:16]]
    data3 = data3[16:]
    for i in range(1,len(string.encode("utf8"))//16):
        data2.append(data3[:16])
        data3 = data3[16:]
    while len(data3.encode("utf8"))<16:
        data3 = str(0) + data3
    data2.append(data3)
else:
    data3 = string
    data2 = [data3[:16]]
    data3 = data3[16:]
    for i in range(1,len(string.encode("utf8"))/16):
        data2.append(string[:16])
        data3 = data3[16:]
stoixeia = len(data2)
for i in range(0,stoixeia):
    ar = int(data2[i])
    if ar%2 == 0:
        sumzugoi += 1
    if ar%3 == 0:
        sum3 += 1
    if ar%5 == 0 :
        sum5 += 1
    if ar%7 == 0:
        sum7 +=1
if stoixeia != 0:
    poszugoi = sumzugoi/stoixeia *100
    pos3 = sum3/stoixeia *100
    pos5 = sum5/stoixeia *100
    pos7 = sum7/stoixeia *100
print(poszugoi,pos3,pos5,pos7)
print(sumzugoi,stoixeia)

        
