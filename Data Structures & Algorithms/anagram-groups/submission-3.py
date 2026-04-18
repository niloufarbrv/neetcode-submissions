class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  ["act","pots","tops","cat","stop","hat"]
        # act [a:1, c:1, t:1]
        # pots [ p:1, o:1, t:1, s:1]
        # tops [ p:1, o:1, t:1, s:1]
        # stop [ p:1, o:1, t:1, s:1]
        # cat [a:1, c:1, t:1]
        # stop [ p:1, o:1, t:1, s:1]
        # hat [a:1, h:1, t:1 ]

        # generating hashmaps: n * m
        # comparing hashmaps with each other Coparing each two combinarion:
        # n *n *m*

        counter_to_strings = {}

        for i, string in enumerate(strs):
            string_count  = [0] * 26
            for item in string:
                item_index  = ord(item) - ord("a")
                string_count[item_index]  += 1
            if tuple(string_count) in counter_to_strings:
                counter_to_strings[tuple(string_count)].append(string)
            else:
                counter_to_strings[tuple(string_count)] = [string]
    
        return list(counter_to_strings.values())



        






            
