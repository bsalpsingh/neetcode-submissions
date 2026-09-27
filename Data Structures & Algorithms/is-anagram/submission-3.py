class Solution:
    def isAnagram( self,s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            s_list= list(s)
            t_list = list(t)

            s_char_count={}
            t_char_count={}


            for char in s_list:
                if s_char_count.get(char) is None:
                    s_char_count[char]=1
                    continue
                s_char_count[char]=s_char_count[char]+1

            for char in t_list:
                if t_char_count.get(char) is None:
                    t_char_count[char]=1
                    continue
                t_char_count[char]=t_char_count[char]+1
        
            for char in t_list:
                if s_char_count.get(char) is None:
                    return False
                if s_char_count[char] == t_char_count[char]:
                    continue
                
                return False
            return True
            

        