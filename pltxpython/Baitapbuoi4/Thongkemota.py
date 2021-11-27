#1,
def mean(A):
    print("Số trung bình là:",sum(A)/len(A)) 
#2, 
def median(m):
    n = len(m)
    sorted_m = sorted(m)
    mid = n // 2
    number = 0
    if n % 2 == 1:
        number = sorted_m[mid]
        print(number)  
    else:
        lo = mid - 1
        hi = mid
        number = (sorted_m[lo] + sorted_m[hi]) / 2
        print("Số trung vị là:",number)
#3,
from collections import Counter
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    for x_i,count in counts.items():
        if count == max_count:
            print ("Mode của dãy là:", x_i)
A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
mean(A)
median(A)
mode(A)
