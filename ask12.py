from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
pin = []
for i in range(0,100):
    #brisko th 8esh tou round kai afou thn bro mexri na teleiosei h epanalhpsh pairno tis 100 teuleutaies times mia mia fora
    data2 = data.decode('utf8')
    a = data2.find(':')
    b = data2.find(',')
    ar = data2[:b]
    ar = ar[a+1:]
    ar = int(ar)
    ar = ar-i
    ar = str(ar)
    #bazo thn meiomenh timh 
    url = 'https://drand.cloudflare.com/public/{}'
    req = Request(url.format(ar), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data2 = data.decode('utf8')
    #brisko thn 8esh tou ramdomness gia na paro to keimeno kai to metatrepo se 0 kai 1 kai thn bazo sthn lista pin
    th1 = data2.find(":",b)+2
    ram = data2[th1:]
    th2 = ram.find(',')
    ram = ram[:th2-1]
    ram = int(ram,16)
    ram = bin(ram)
    pin.append(ram[2:])
#brisko tis perissoteres sunexomenes fores pou emfanizetai to 0 kai to 1    
max0 = 0
max1 = 0
for i in range(0,100):
    m0 = 0
    m1 = 0
    l = list(pin[i])
    for j in range(0,len(l)):
        if int(l[j]) == 0:
            m0 += 1
        elif m0>=max0:
            max0 = m0
            m0= 0
        elif m0<max0 :
            m0 = 0
        if int(l[j]) == 1:
            m1 +=1
        elif m1>=max1 :
            max1 = m1
            m1 = 0
        elif m1<max1 :
            m1 = 0
#bazo stis listes pin0 kai pin1 to "keimeno" se 0 kai 1 pou emfanizontaie sunexomena ta 0 kai 1             
pin0 = []
pin1 = []
max00 = 0
max11 = 0
for i in range(0,100):
    m0 = 0
    m1 = 0
    l = list(pin[i])
    for j in range(0,len(l)):
        if int(l[j]) == 0:
            m0 += 1
        elif m0>=max00:
            max00 = m0
            m0= 0
        elif m0<max00 :
            m0 = 0
        if int(l[j]) == 1:
            m1 +=1
        elif m1>=max11 :
            max11 = m1
            m1 = 0
        elif m1<max11 :
            m1 = 0
    if max00 == max0 :
        max00 = 0
        pin0.append(pin[i])
    if max11 == max1 :
        pin1.append(pin[i])
        max11 = 0
print(" oi akolou8ies  me to megalutero mhkos se seira mhdenikon einai",len(pin0),"me mhkos sunexomenon mhdenikon",max0,"kai einai oi e3hs")     
for i in range(0,len(pin0)):
    print(pin0[i])
print(" oi akolou8ies  me to megalutero mhkos se seira monadon einai",len(pin1),"me mhkos unexomenon monadon",max1,"kai einai oi e3hs")     
for i in range(0,len(pin1)):
    print(pin1[i]) 
