'''
Youtube link : https://www.youtube.com/watch?v=EQQp4B_CU5Q&index=2&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p&pbjreload=10
Union and Intersection of two sorted arrarys
'''

def sortedUnion(arr1, arr2):
	union_arr = []
	i = 0
	j = 0
	arr1_len = len(arr1)
	arr2_len = len(arr2)

	while i < arr1_len and j < arr2_len:
		if arr1[i] < arr2[j]:
			union_arr.append(arr1[i])
			i  += 1
		elif arr2[j] < arr1[i]:
			union_arr.append(arr2[j])
			j += 1
		else:
			union_arr.append(arr2[j])
			j += 1
			i += 1
	
	#this is to check if some elements avn't been added yet

	while i < arr1_len:
		union_arr.append(arr1[i])
		i += 1

	while j < arr2_len:
		union_arr.append(arr2[j]);
		j += 1		

	return union_arr	
		


def sortedIntersection(arr1, arr2):
	i = j = 0
	arr1_len = len(arr1)
	arr2_len = len(arr2)

	intersection_arr = []

	while i < arr1_len and j < arr2_len:
		if arr1[i] < arr2[j]:
			i += 1
		elif arr2[j] < arr1[i]:
			j += 1
		else:
			intersection_arr.append(arr2[j])
			j += 1
			i += 1

	return intersection_arr
		
		




def main():
	#first array
	arr1 = [1, 3, 4, 5, 7 ]
	#second array
	arr2 = [2, 3, 5, 6];

	union = sortedUnion(arr1, arr2)
	intersection = sortedIntersection(arr1, arr2)

	#print uinon
	print(union)
	print(intersection)




if __name__ == '__main__':
	main()