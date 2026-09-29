class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric_str=[char for char in list(s) if char.isalnum()]
        left = 0
        right = len(alpha_numeric_str)-1

        while left<right:
            if alpha_numeric_str[left].lower()!=alpha_numeric_str[right].lower():
                return False
            left+=1
            right-=1
        return True
        
        