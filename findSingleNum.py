# // Given an array of integers, every element appears twice except for one. Find that single one.

# //Note:
# //Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?



def findSingleNum(arr):
	res=arr[0]
	for i in range(1,len(arr)):
		res=res^arr[i]
	return res

arr=[1,2,1,3,2]
res=findSingleNum(arr)
print res 

