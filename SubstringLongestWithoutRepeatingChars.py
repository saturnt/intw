class Solution(object):
    
    def longest_sub_wo_repeating_chars(self, given_str):
        start=0
        ptr=0
        ht=dict()
        max_len=0
        max_so_far=0
        while(ptr < len(given_str)):
            curr_char = given_str[ptr]
            if curr_char not in ht:
                ht[curr_char]=ptr
                ptr += 1
            else:
                val = ht[curr_char]
                start = max(val + 1, start)
                ht[curr_char] = ptr
                ptr += 1
    
            max_so_far = max(max_so_far, ptr - start)
        
        print max_so_far
        return max_so_far
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.longest_sub_wo_repeating_chars(s)
        
