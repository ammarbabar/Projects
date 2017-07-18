a=[0 for i in range(100000)]
global count
def fileRead():
    i=0
    with open('IntegerArray.txt', 'r') as f:
      for line in f:
        for s in line.split('\0'):
          a[i]=(int(s))
          i=i+1
    return

def mergeSort(alist,count):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        count=mergeSort(lefthalf,count)
        count=mergeSort(righthalf,count)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
                count=count+(len(lefthalf)-i)        
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return count
count=0
fileRead()
count=mergeSort(a,count)
print(count)
