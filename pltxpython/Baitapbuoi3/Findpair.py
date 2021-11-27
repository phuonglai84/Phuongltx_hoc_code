def find_pair(A, tong):
    i=0 ; j=len(A)-1
    dem = []
    while i < j:
        s = A[i] + A[j]
        if s == tong:
            dem.append((A[i],A[j]))
            j -= 1
        elif s < tong:
            i += 1
        else:
            j -= 1
    print(dem)
find_pair([3, 6, 7, 9, 11, 12], 18)