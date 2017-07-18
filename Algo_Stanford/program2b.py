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
    if ind<=length:
        i=ind
        j=ind
        while(j!=length+1):
            if alist[pivot]>alist[j]:
                temp = alist[i]
                alist[i]=alist[j]
                alist[j]=temp
                i=i+1
            else:
                trigger=1
            j=j+1
        if trigger==1:
            temp=alist[pivot]
            alist[pivot]=alist[i]
            alist[i]=temp
            
        count = count+i-ind+1
        #print(a[0:15],"b",i-1,ind,i-ind-1)
        count=QuickSort(alist,count,i-1,ind,i-1)
        #print(a[0:15],"a",ind+length-1,i+1,ind+length-i-1)
        count = count+length-i-1
        count=QuickSort(alist,count,length,i+1,length)

    return count
    
count=0
fileRead()
count=QuickSort(a,count,len(a)-1,0,len(a)-1)
for i in range(10000):
    if(a[i]!=i+1):
       print("false",i)
    if(i==9999):
        print("YEP")
print(count)
