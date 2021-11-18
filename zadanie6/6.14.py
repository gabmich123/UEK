array=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
longest=""
for x in range(0,len(array)):
    if len(array[x])>len(longest):
        longest=array[x]
        
print(longest)