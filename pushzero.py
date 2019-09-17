def pushzero(arr, n):
 count=0
 for i in Range(n):
   if(arr[i]!=0:
 
    arr[count] = arr[i] 
            count+=1
  while count < n:
    arr[count]=0
    count+=1
    
 arr=[2,3,0,5,3,0,8,0,0]
 n= len(arr)
 pushzero(arr,n)
 print("the elements after pushing zeros to end : ")
 print(arr)
    
    
  
 
