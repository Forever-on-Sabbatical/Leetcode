

# This solution is apparently better than the others so analyze it
# def isPalindrome(self, x: int) -> bool:
#    	if x<0:
  #  return False

   # inputNum = x
	#newNum = 0
	#while x>0:
	#	newNum = newNum * 10 + x%10
	#return newNum == inputNum
 
class Solution:
    def isPalindrome(self, x: int) -> bool:        
        return str(x) == str(x)[::-1] if x >= 0 else False
