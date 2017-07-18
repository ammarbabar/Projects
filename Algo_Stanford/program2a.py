a=[0 for i in range(10000)]
global count
def fileRead():
    i=0
    with open('QuickSort.txt', 'r') as f:
      for line in f:
        for s in line.split('\0'):
          a[i]=(int(s))
          i=i+1
    return

def QuickSort(alist,count,pivot,ind,length):
    trigger=0
    if length>1:
        i=ind
        for j in range (length):
            if(i==ind+pivot):
                i=i+1
            if alist[ind+pivot]>alist[j+ind]:
                temp = alist[i]
                alist[i]=alist[j+ind]
                alist[j+ind]=temp
                trigger=1
                i=i+1
        temp=alist[ind+pivot]
        if(i!=0 and trigger==1):
            alist[ind+pivot]=alist[i-1]
            alist[i-1]=temp
        else:
            if(trigger==1):
                alist[ind+pivot]=alist[i]
                alist[i]=temp
        count = count+i-ind-1
        count=QuickSort(alist,count,pivot,ind,i-ind-1)
        count = count+ind+length-i
        count=QuickSort(alist,count,pivot,i,ind+length-i)
    return count
    
count=0
fileRead()
count=QuickSort(a,count,0,0,len(a))
for i in range(10000):
    if(a[i]!=i+1):
       print("false")
    if(i==9999):
        print("YEP")
print(count)
