def lengthOfLongestSubstring(s: str):
    longest = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if len(set(s[i:j])) == len(s[i:j]):
                longest = max(longest, j-i)
    return longest

print(lengthOfLongestSubstring("abcabcbb"))