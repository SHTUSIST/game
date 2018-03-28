
def operator(s,l):
    
 
    connector=s.replace(" ","")
    
    connector=connector.split("},")

    D,E,F=[],[],[]
    for i in connector:
        mao=i.find(":")+2  
        device=s[1]

        dian=i.find(".")

        inn=i[mao:dian]


        mao2=i.find(":",mao+1)+2
        dian2=i.find(".",dian+1)


        inn2=i[mao2:dian2]


        for i in l:
            if inn==i[0].lower():
             
                
                D.append(i)
                break;
        for i in l:
            if inn2==i[0].lower():

                E.append(i)
                break;

    ss=""
    for i in range(len(D)):
        ss=ss+"""
G1 Z80
G1 """+E[i][1]+" "+E[i][2]

        ss=ss+"""
G1 Z0
G1 E100
G1 Z80
G1 """+D[i][1]+" "+D[i][2]
        ss=ss+"""
G1 Z0
G1 E200"""
     
    f=open('result.txt','w') 
    f.write(ss[1:])
    f.close()
    print("sdf")
        
    
        

        
    
    
a=open('data.txt',encoding='UTF-8')
try:
    s = a.read( )
finally:
    a.close( )
l=[['DEV0', 'X34', 'Y127'], ['DEV1', 'X70', 'Y127'], ['DEV2', 'X34', 'Y90'], ['DEV3', 'X70', 'Y90'], ['DEV4', 'X105', 'Y127'], ['DEV5', 'X143', 'Y127'], ['DEV6', 'X105', 'Y90'], ['DEV7', 'X143', 'Y90'], ['DEV8', 'X178', 'Y127'], ['DEV9', 'X178', 'Y90'],['DEV10', 'X178', 'Y90']]



operator(s,l)