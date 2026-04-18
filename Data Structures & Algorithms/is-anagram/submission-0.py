class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = {},  {}
        for char in s:
            s_counter[char] = s_counter.get(char, 0) + 1
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1
        
        for char in t:
            if s_counter.get(char, 0) != t_counter.get(char, 0):
                return False 
       
        
        for char in s: 
            if s_counter.get(char, 0) != t_counter.get(char, 0):
                return False 
        
        return True
            
        