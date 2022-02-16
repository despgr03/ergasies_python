import string,re
#xrishmopoihsa to arxeio license.txt dioti to tales of two cities.txt ekane poly ora sto laptop mou na bgalei apotelesma(pano apo 2 ores),oi le3eis pou emfanizotan perissotero kai h suxnothta tous jtan oi e3hs: 1.the 8241 2.and 5071 3.of 4143 4.to 3653 5.a 3017 6.in 2665 7.it 2082 8.his 2011 9.i 1990 10.that 1956
f = open("LICENSE.txt")
new = f.read()
f.close()   
new = new.lower()
kai = re.sub(r'[^a-z ]+', ' ', new)
data = kai.split()#dhmiourgo lista me ka8e le3h afou prota exo epe3ergastei to keimeno
#arxikopoio tis metablhtes pou 8a mpoun oi 10 dhmofhlesteres le3eis kai ta sum tous
le3h1 = ""
le3h2 = ""
le3h3 = ""
le3h4 = ""
le3h5 = ""
le3h6 = ""
le3h7 = ""
le3h8 = ""
le3h9 = ""
le3h10 = ""
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0
#arxikopoio tis metablhtes pou 8a mpoun oi 3 protoi sundiasmoi ton 2 proton grammaton pou arxizoun oi perissoteres le3eis
f2le1 = ""
f2le2 = ""
f3l3 = ""
sumf2le1 = 0
sumf2le2 = 0
sumf2le3 = 0
#arxikopoio tis metablhtes pou 8a mpoun oi 3 protoi sundiasmoi ton 3 proton grammaton pou arxizoun oi perissoteres le3eis
f3le1 = ""
f3le2 = ""
f3le3 = ""
sumf3le1 = 0
sumf3le2 = 0
sumf3le3 = 0
stoixeia = len(data)
for i in range(0,stoixeia):
  #arxikopoio ta sum kai tis metablhtes bazontas sthn ka8e mia le3eis pou kai tis sullabes pou 8a epanalambanontai
  sum2f = 0
  sum3f = 0
  sumf = 0
  le3h = data[i]
  le2 = le3h[:2]
  le3 = le3h[:3]
  for w in range(0,stoixeia):
    if le2 == data[w][:2] and len(le2) == 2 :
        sum2f += 1
    if le3 == data[w][:3] and len(le3) == 3:
        sum3f +=1
    if le3h == data[w]:
        sumf += 1
  if sum1<=sumf :
    sum1 = sumf
    le3h1 = le3h
  elif sum2<=sumf :
    sum2 = sumf
    le3h2 = le3h
  elif sum3<=sumf :
    sum3 = sumf
    le3h3 = le3h
  elif sum4<=sumf:
    sum4 = sumf
    le3h4 = le3h
  elif sum5<=sumf :
    le3h5 = le3h
    sum5 = sumf
  elif sum6<=sumf:
    le3h6 = le3h
    sum6 = sumf
  elif sum7<=sumf:
    sum7 = sumf
    le3h7 = le3h
  elif sum8<=sumf:
    sum8 = sumf
    le3h8 = le3h
  elif sum9<=sumf:
    sum9 = sumf
    le3h9 = le3h
  elif sum10<=sumf:
    sum10 = sumf
    le3h10 = le3h
  if sum2f>=sumf2le1 :
    f2le1 = le2
    sumf2le1 = sum2f
  elif sum2f>=sumf2le2:
    f2le2 = le2
    sumf2le2 = sum2f
  elif sum2f>=sumf2le3:
    f2le3 = le2
    sumf2le3 = sum2f
  if sum3f>=sumf3le1:
    f3le1 = le3
    sumf3le1 = sum3f
  elif sum3f>=sumf3le2:
    f3le2 = le3
    sumf3le2 = sum3f
  elif sum3f>=sumf3le3:
    f3le3 = le3
    sumf3le3 = sum3f
print("oi deka dhmofilesteres le3eis einai:",le3h1,",",le3h2,",",le3h3,",",le3h4,",",le3h5,",",le3h6,",",le3h7,",",le3h8,",",le3h9,",",le3h10)     
print("oi 3 protoi sundiasmoi ton 2 proton grammaton pou arxizoun oi perissoteres le3eis einai:",f2le1,",",f2le2,",",f2le3)
print("oi 3 protoi sundiasmoi ton 3 proton grammaton pou arxizoun oi perissoteres le3eis einai:",f3le1,",",f3le2,",",f3le3)

