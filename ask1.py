import random

sumf = 0
for i in range(0,100):
    #arxikopoihsh metablhton oste ka8e mege8os na mhn yparxei sto paixidi pano apo 9 fores 
    #ka8e grammh einai lista 3 8eseon pou ka8e mia periexei lista 3 8eseon oste na mpainou oi daktulioi olon ton mege8on 
    sum1 = 0
    sum2 = 0
    sum3 = 0
    gr1 = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]
    gr2 = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]
    gr3 = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]
    flag = "false"
    while flag == "false":
        grammh = random.randrange(0,3)
        sthlh = random.randrange(0,3)
        mege8os = random.randrange(0,3)
        if mege8os == 0:
            sum1 = 1 + sum1
        elif mege8os == 1:
            sum2 = 1 + sum2
        elif mege8os == 2:
            sum3 = 1 + sum3    
        if (mege8os == 0 and sum1<=9)or(mege8os == 1 and sum2<=9)or(mege8os == 2 and sum3<=9): 
            if grammh == 0 and gr1[sthlh][mege8os] == [0]:
                gr1[sthlh][mege8os] = mege8os + 1
                sumf = sumf + 1
                if gr1[0][mege8os] == gr1[1][mege8os] and gr1[0][mege8os] == gr1[2][mege8os]: #orizontia gia idio mege8os
                    flag = "true"
            elif gr1[sthlh][mege8os] != [0] and grammh == 0:
                #elegxos se periptosh pou sth 8esh pou epile3ei o xrhsths na balei daxtulio na mhn upaexei hdh kapoios mesa
                #ean uparxei afaireitai oste na exoun thn eukairia na mpoun 9 daxktulioin kapoiou mege8ous se 9 diaforetikes 8eseis
                if mege8os == 0:
                    sum1 = sum1 - 1
                elif mege8os == 1:
                    sum2 = sum2 - 1
                elif mege8os == 2:
                    sum3 = sum3 - 1
            elif grammh == 1 and gr2[sthlh][mege8os] == [0]:
                gr2[sthlh][mege8os] = mege8os + 1
                sumf = sumf + 1
                if gr2[0][mege8os] == gr2[1][mege8os] and gr2[0][mege8os] == gr2[2][mege8os]: #orizontia gia idio mege8os
                    flag = "true"
            elif gr2[sthlh][mege8os] != [0] and grammh == 1:
                #elegxos se periptosh pou sth 8esh pou epile3ei o xrhsths na balei daxtulio na mhn upaexei hdh kapoios mesa
                #ean uparxei afaireitai oste na exoun thn eukairia na mpoun 9 daxktulioin kapoiou mege8ous se 9 diaforetikes 8eseis
                if mege8os == 0:
                    sum1 = sum1 - 1
                elif mege8os == 1:
                    sum2 =  sum2 - 1
                elif mege8os == 2:
                    sum3 = sum3 - 1
            elif grammh == 2 and gr3[sthlh][mege8os] == [0]:
                gr3[sthlh][mege8os] = mege8os+1
                sumf = sumf + 1
                if gr3[0][mege8os] == gr3[1][mege8os] and gr3[0][mege8os] == gr3[2][mege8os]: #orizontia gia idio mege8os
                    flag = "true"
            elif gr2[sthlh][mege8os] != [0] and grammh == 2:
                #elegxos se periptosh pou sth 8esh pou epile3ei o xrhsths na balei daxtulio na mhn upaexei hdh kapoios mesa
                #ean uparxei afaireitai oste na exoun thn eukairia na mpoun 9 daxktulioin kapoiou mege8ous se 9 diaforetikes 8eseis
                if mege8os == 0:
                    sum1 = sum1 - 1
                elif mege8os == 1:
                    sum2 = sum2 - 1
                elif mege8os == 2:
                    sum3 = sum3 - 1   
            if gr1[sthlh][mege8os] == gr2[sthlh][mege8os] and gr1[sthlh][mege8os] == gr3[sthlh][mege8os] : #ka8etos gia idio mege8os
                flag = "true"
            elif gr1[0][mege8os] == gr2[1][mege8os] and gr1[0][mege8os] == gr3[2][mege8os] and gr1[0][mege8os] != [0]: #diagonia gia idio mege8os
                flag = "true"
            elif gr1[2][mege8os] == gr2[1][mege8os] and gr1[2][mege8os] == gr3[0][mege8os] and gr1[2][mege8os] != [0] : #diagonia gia idio mege8os
                flag = "true"
            elif gr1[sthlh][0] == 1 and gr2[sthlh][1] == 2 and gr3[sthlh][2] == 3: #ka8etos gia au3anomeno mege8os
                flag = "true"
            elif gr1[sthlh][2] == 3 and gr2[sthlh][1] == 2 and gr3[sthlh][0] == 1: #ka8etos gia au3anomeno mege8os
                flag = "true"
            elif gr1[0][0] == 1 and gr2[1][1] == 2 and gr3[2][2] == 3: #diagonios gia au3anomeno mege8os
                flag = "true"
            elif gr1[0][2] == 3 and gr2[1][1] == 2 and gr3[2][0] == 1: #diagonios gia au3anomeno mege8os
                flag = "true"
            elif gr1[2][0] == 1 and gr2[1][1] == 2 and gr3[0][2] == 3:#diagonios gia au3anomeno mege8os
                flag = "true"
            elif gr1[2][2] == 3 and gr2[1][1] == 2 and gr3[0][0] == 1:#diagonios gia au3anomeno mege8os
                flag = "true"
            elif gr1[0][0] == 1 and gr1[1][1] == 2 and gr1[2][2] == 3:#orizontia gia au3anomeno mege8os
                flag = "true"
            elif gr1[0][2] == 3 and gr1[1][1] == 2 and gr1[2][0] == 1: #orizontia gia au3anomeno mege8os
                flag = "true"
            elif gr2[0][0] == 1 and gr2[1][1] == 2 and gr2[2][2] == 3:#orizontia gia au3anomeno mege8os
                flag = "true"
            elif gr2[0][2] == 3 and gr2[1][1] == 2 and gr2[2][0] == 1: #orizontia gia au3anomeno mege8os
                 flag = "true"
            elif gr3[0][0] == 1 and gr3[1][1] == 2 and gr3[2][2] == 3:#orizontia gia au3anomeno mege8os
                 flag = "true"
            elif gr3[0][2] == 3 and gr3[1][1] == 2 and gr3[2][0] == 1: #orizontia gia au3anomeno mege8os
                  flag = "true"
mo=sumf / 100
print("o mesos oros bhmaton gia na termathsei to paixnidi einai",mo,"bhmata")                
            

