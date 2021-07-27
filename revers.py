""""
input is through the command line 
"""

def reverse(num):
	if num in range((-1 << 31), (1 << 31)):
		rev = int(str(abs(num))[::-1])
		if rev in range(0, (1 << 31) + 1) and num < 0:
			print(-1 * rev)
		elif rev in range(0, (1 << 31)) and num >= 0:
			print(rev)
		else:
			print(0)
	
	else:
		print('number not in 32bit integer')

num = int(input())
reverse(num)
