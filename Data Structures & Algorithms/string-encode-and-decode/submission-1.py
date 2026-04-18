class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["hello" , "world", "!"] >> #
        # ["hello#world#!"]
        # s2=["hello" , "#world", "!"] >> ["5$hello6$world1$!"]
        encoded_strs = []
        for string in strs:
            len_string = len(string)
            encoded_string = str(len_string)+"$"+string
            encoded_strs.append(encoded_string)

        return "".join(encoded_strs)



        

    def decode(self, s: str) -> List[str]:
        final_strings = []
        
            # while loop for extracting length 
        i = 0
        while True:
            if i>=len(s):
                break
            length = ""
            while s[i] != "$":
                length = length +s[i]
                i +=1
            length = int(length)
            word = s[i+1:i+1+length]
            i = i+1+length
            final_strings.append("".join(word))
        
        return final_strings
            
                

                

                
        