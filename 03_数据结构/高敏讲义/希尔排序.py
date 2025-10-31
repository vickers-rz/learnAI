
#python实现希尔排序

arr=[8,9,1,7,2,3,5,4,6,0]

gap=5
   #[8         3]
   #[  9         5]
   #[    1         4]
   #[      7         6]
   #[        2         0]
def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        print("gap:",gap)
        for i in range(gap,n): #i (5,10)  #(2,10)  #(1,10)
            key=arr[i]
            j=i
            print(arr[j-gap],key)
            print("j******=",j)
            while j>=gap and arr[j-gap] >key:
                arr[j]=arr[j-gap]
                j-=gap
                #print("j&&&&&&",j)
                #print(arr)
            print("j====",j)
            arr[j]=key
            print(arr)
        gap//=2

print(arr)
shell_sort(arr)
print(arr)