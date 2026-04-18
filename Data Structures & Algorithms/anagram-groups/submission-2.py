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

        strings_to_counter = {}

        for i, string in enumerate(strs):
            string_count  = [0] * 26
            for item in string:
                item_index  = ord(item) - ord("a")
                string_count[item_index]  += 1
            key = tuple([i,string])
            strings_to_counter[key] = tuple(string_count)
        
        counter_to_stings = {}
        for (indext,string), counter in strings_to_counter.items():
            if counter not in counter_to_stings:
                counter_to_stings[counter] = [string]
            else:
                counter_to_stings[counter].append(string)

        return list(counter_to_stings.values())



        






            
