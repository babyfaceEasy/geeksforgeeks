'''
Youtube link: https://www.youtube.com/watch?v=lBk6fVhuCyw&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p&index=3
Find the missing number in the array given
'''

def methodOne( nums ):
	#this method finds the total of all the numbers 
	#then removes all available digit from the total 
	#and then the value left is missing number
	
	#using the formula n * (n + 1) / 2
	
	max_num = max(nums)

	total = (len(nums) + 1) * (len(nums) +  2) / 2
	'''
	for x in range(1, (max_num+1)):
		total += x
	'''

	for num in nums:
		total -= num

	return total

def methodTwo( nums ):
	'''
	using the exclusive OR idea where if  u XOR all the elements int the array
	against all the elements expected to be in the array, u would get the final
	missing value
	'''

	elts_in_arr_xor = nums[0]
	elts_xor = 1

	for x in range(1, len(nums)):
	 	elts_in_arr_xor = elts_in_arr_xor ^ nums[x] 

	for x in range(2, max(nums) + 1):
		elts_xor ^= x

	missing_number = elts_in_arr_xor ^ elts_xor
	return missing_number


def main():
	nums = [1, 2, 3, 4, 6, 7, 8]
	
	print('Method One ', methodOne(nums))
	print('Method Two', methodTwo(nums))


if __name__ == '__main__':
	main()