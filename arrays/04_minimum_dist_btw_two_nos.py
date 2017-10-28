'''
Youtube link: https://www.youtube.com/watch?v=hoceGcqQczM&index=4&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p
This is to find the minimum distance between two nymbers (x,y)
'''

def methodOne(arr, x, y):
	'''
		this uses the brute force method, where the first loop runs
		through the arr and the second loop throu the array and if 
		if x and y is attained by the loops minimum distance is 
		updated
		Time Complexity: O(n*n)
	'''
	min_dist = 100000
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] == x and arr[j] == y:
				temp = abs(i - j)
				if temp < min_dist:
					min_dist = temp
			elif arr[i] == y and arr[j] == x:
				temp = abs(j - i)
				if temp < min_dist:
					min_dist = temp

	return min_dist


def methodTwo(arr, x, y):
	'''
	This is the tricky one u search the array and once u meat x or y
	save it inside prev. den continue search from prev if u find 
	x or y if x is d same as arr[prev] continue if different check for 
	minimum dist
	Time complexity: O(n)
	'''
	prev = -1
	min_dist = 100000
	for i in range(len(arr)):
		if arr[i] == y or arr[i] == x:
			prev = i
			break

	for j in range(x, len(arr)):
		if arr[j] == y or arr[j] == x:
			if arr[j] != arr[prev]:
				temp = abs(j - prev)
				if temp < min_dist:
					min_dist = temp
					prev = j
			else :
				prev = j

	return min_dist
				
			
			

def main():
	arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
	x = 3
	y = 6

	print(methodOne(arr, x, y))
	print('Method two', methodTwo(arr, x, y))


if __name__ == '__main__':
	main()