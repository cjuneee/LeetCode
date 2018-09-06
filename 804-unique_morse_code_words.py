class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = []
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(words)):
            ss = ''
            for s in words[i]:
                ss += mos[ord(s)-97]
            pd = 0
            for j in range(len(morse)):
                if ss == morse[j]:
                    pd = 1
                    break
            if pd == 0:
                morse.append(ss)
        return (len(morse))


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        passwords = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        i = 0
        decod_words = ['a'] * len(words)
        for word in words:
            for w in word:
                decod_words[i] += passwords[ord(w) - 97]
            i += 1
        last_list = list(set(decod_words))
        return len(last_list)
