class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        encode a given word into its morse notation
        map above function to all words in the input list
        return the len of the set of the map object returned above
        """
        CONST_MORSE_ENCODING = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
        def encode_word_to_morse(word):
            return ''.join(CONST_MORSE_ENCODING[ord(c)-97] for c in word)
        
        return len(set(map(encode_word_to_morse, words)))