import string

count=0
# for 1bp overlap
with open('bedfile1','r') as f1, open('bedfile2','r') as f2:



    for i in f1:
        for j in f2:
            info1=i.split('\t')
            info2=j.split('\t')
            if info1[0]==info2[0]:
                if max(info1[1],info2[1])<min(info1[2],info2[2]):
                    count=count+1
                    
                    
print(count)               
                


# for 8bp overlap            
with open('bedfile1','r') as f1, open('bedfile2','r') as f2:

    for i in f1:
        for j in f2:
            info1=i.split('\t')
            info2=j.split('\t')
            if info1[0]==info2[0]:
                if max(info1[1],info12[1])<min(info1[2],info2[2])-8:
                    count=count+1
                    
                    
print(count)               



# for 30bp overlap
with open('bedfile1','r') as f1, open('bedfile2','r') as f2:

    for i in f1:
        for j in f2:
            info1=i.split('\t')
            info2=j.split('\t')
            if info1[0]==info2[0]:
                if max(info1[1],info12[1])<min(info1[2],info2[2])-30:
                    count=count+1
                    
                    
print(count)               
                
