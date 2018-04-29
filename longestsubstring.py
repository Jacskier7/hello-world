str1 = "aabcdecfegihjkih" 

dict = {}

sub = ""
presub = ""
pos = 0
for i in range(len(str1)):
    if str1[i] not in dict:
       dict[str1[i]] = i
       sub = sub+str1[i]
    else:
       if len(sub) > len(presub):
           presub = sub
           print sub
       k = dict[str1[i]]-pos
       sub = sub[k+1:]+str1[i]
       print("sub--- ", sub)
       dict = {}
       for j in range(len(sub)):
          dict[sub[j]]=j

    print("AAA ",sub,pos)   

if len(sub) > len(presub):
    print sub    
     

