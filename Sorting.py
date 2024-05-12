def SelectionSort(list):
    #O(N^2) in any case. My fav one
    for i in range(0, len(list)):
        for x in range(i, len(list)):
            if list[i] > list[x]:
                temp = list[x]
                list[x] = list[i]
                list[i] = temp
    print(list)

SelectionSort([5,6,1,2])


def InsertionSort(list):
    #Best Case: O(n) (Already sorted)
    #Avg + Worst case: O(n^2) (Reverse order)
    for i in range(0,len(list)):
        for x in range(i, 0, -1):
            if list[x] < list[x-1]:
                temp = list[x]
                list[x] = list[x-1]
                list[x-1] = temp

    print(list)

InsertionSort([5,6,1,2])

def merge(a, aux, lo,mid,hi):
    #merges two lists
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if (i>mid):
            aux[k] = a[j]
            j += 1
        elif (j>hi):
            aux[k] = a[i]
            i += 1
        elif (a[j]<a[i]):
            aux[k] = a[j]
            j+= 1
        else:
            aux[k] = a[i]
            i+= 1

    
def sort(a,aux,lo,hi):
    #keep splitting recursively then merge 
    #O(nlog(n)) in all cases
    #M(n) Not In Place
    #Stable
    if(hi<=lo):
        return
    mid = lo + (hi-lo) // 2

    sort(a,aux,lo,mid)
    sort(a,aux,mid+1,hi)
    merge(a,aux,lo,mid,hi)

a = [5,4,1,7]
aux = a.copy()
sort(a,aux,0,len(a)-1)
print(a)


def partition(a,lo,hi):
    #Avg Case: O(nlog(n))
    #Worst Case: 1/2(N^2)
    #In-Place
    #Not Stable
    i = lo
    j = hi+1
    p = a[lo]
    while True:
        i += 1
        while(a[i] < p):
            if(i==hi):
                break
            i += 1
        j -= 1
        while(p<a[j]):
            if(j==lo):
                break
            j -= 1
        if(i>= j):
            break
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    temp = a[lo]
    a[lo] = a[hi]
    a[hi] = temp
    return j

def qSort(a,lo,hi):
    if(hi<=lo):
        return
    j = partition(a,lo,hi)
    qSort(a,lo,j-1)
    qSort(a,j+1,hi)
    