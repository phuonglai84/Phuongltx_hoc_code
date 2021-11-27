my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
count={}
for i in my_list:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
 
print(count)