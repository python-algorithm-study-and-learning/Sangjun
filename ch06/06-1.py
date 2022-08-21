import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', "", s)
        return res.lower() == res[::-1].lower()
