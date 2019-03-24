class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) + ord("a") - ord("A")) if ord(c) >= ord("A") and ord(c) <= ord("Z") else c for c in str)