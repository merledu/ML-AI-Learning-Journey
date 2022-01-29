page  = "1.html"
dic = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
n=len(dic)
new_dict = dict()
for i in dic:
    if len(dic[page])==0:
        new_dict[i]=1/n
    elif i == page and len(dic[i])!=0:
        new_dict[i]=(1-0.85)/n
    
    elif i!=page and i in dic[page]:
        new_dict[i]=(0.85/len(dic[page]))+((1-0.85)/n)
    
    elif i!=page and i not in dic[page]:
        new_dict[i]=(1-0.85)/n
print(new_dict)