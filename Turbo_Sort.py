def merge_list(list1):

	if len(list1)==1:

		return list1
	else:

		mid=len(list1)//2
		left__list,right_list = merge_list(list1[:mid]),merge_list(list1[mid:])

	sorted_list = []

	i,j=0,0

	while i<len(left__list) and j<len(right_list):

		if left__list[i] > right_list[j]:
			sorted_list.append(right_list[j])
			j+=1
		else:
			sorted_list.append(left__list[i])
			i += 1
	sorted_list+= left__list[i:]
	sorted_list+= right_list[j:]

	return sorted_list
list1 = []
T=int(input())
for i in range(T):
	list1.append(int(input()))
	
a=(merge_list(list1))
for i in a:
	print(i)
