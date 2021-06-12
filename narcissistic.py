#
#
	Copyright 2021 Abir Haque

#	Subject to MIT License in LICENSE file

#
#
#
#	Narcissistic Numbers:
#
#	Find integers that are the summ of their own digits raised to the power of the total number of digits in a given integer.
#
#	Integers that exist are called Narcissistic numbers [1].
#	89 narcissistic numbers have been found, with the largest being:
#
#		115,132,219,018,763,992,565,095,597,973,971,522,401
#
#	An example of a Narcissistic number is 153. Below is an explanation:
#
#		153 contains digits 1, 5, and 3, thus 3 total digits.
#
#		1^3 + 5^3 + 3^3 = 153
#
#	I thought it would be fun to write the program without any APIs, len() function, or substrings.
#
#	This is possible by first figuring out how many digits exist in integer n.
#	That is possible by dividing n by 10 until n equals 0 (use floor division instead of normal division).
#	Each time we divide n, we add 1 to counter variable c.
#	A counter function can look like this:
#
#		def count(n):
#			c=0
#			while(n!=0):
#				n//=10
#				c+=1
#			return c
#
#
#	Next, we must figure out how to isolate each digit as a value to exponentiate by c, then add in series.
#	Let's use n = 153 as an example an try creating a formula that results in 1, 3, and 5.
#	One could modulate n with 10 to get 3, meaning that we have the following so far:
#
#		3 = 153 mod 10
#
#	Now we have to get 5. We can modulate n with 100 to get 53. Next, subtract 3, the previous digit, to get 50.
#	50 divided by 10 gets us 5. This all can be seen below:
#
#		5 = (153 mod 100 - 153 mod 10) / 10
#
#	A pattern is slowly developing, but not fully present, so let's get 1.
#	If we try raising the modulation value we tried to get 5 by one more power, we can get 1 as seen below:
#
#		1 = (153 mod 1000 - 153 mod 100) / 100
#
#	With this pattern recognizable, we can apply it back to 3:
#
#		3 = 153 mod 10
#		3 = (153 mod 10 - 0) / 1
#		3 = (153 mod 10 - 153 mod 1) / 1
#
#	Let us make this into an equation to find the digit at a specific place value:
#
#		k = ((n mode 10^b) - (n mode 10^(b-1)))/(10^(b-1))
#
#		Where k is the digit at place b, and n is our integer.
#
#	To check if n is narcissistic, we have to compare the sum of all values of k^c with n.
#	If the sum equals n, then n is narcissistic.
#
#	Below is a program I wrote after watching another Numberphile video that introduced this problem in mathematics [2].
#	The program only checks up to n = 10000, though you are free to play around with the maximum n value.
#
#	Links:
#	[1] https://en.wikipedia.org/wiki/Narcissistic_number
#	[2] https://www.youtube.com/watch?v=4aMtJ-V26Z4

def count(n):
	c = 0
	while(n!=0):
		n//=10
		c+=1
	return c

def isNarcissistic(n):
	b = 1 #place index variable
	s = 0 #sum variable
	d = count(n) #digits count variable
	for b in range(1,d+1):
		s+=(((n%(10**b))-(n%(10**(b-1))))/(10**(b-1)))**d
	if(s==n):
		return True
	return False

#Test case, finds Narcissistic numbers between 0 and 10^4:
maxValue = 10**4
for n in range(0,maxValue):
	if isNarcissistic(n):
		print(str(n)+" is narcissistic.")