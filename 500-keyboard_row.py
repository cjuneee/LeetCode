class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        tab1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        tab2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        tab3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

        strs = []

        for i in range(len(words)):
            length1 = length2 = length3 = 0
            for s in words[i]:
                if s in tab1:
                    length1 += 1
                if s in tab2:
                    length2 += 1
                if s in tab3:
                    length3 += 1
                if length1 == len(words[i]) or length2 == len(words[i]) or length3 == len(words[i]):
                    strs.append(words[i])
        return strs

        res = []
        m = {}

        for k in 'qwertyuiop':
            m[k] = 1

        for k in 'asdfghjkl':
            m[k] = 2

        for k in 'zxcvbnm':
            m[k] = 3

        for w in words:
            ok = True
            k = m[w[0].lower()]
            for c in w:
                if m[c.lower()] != k:
                    ok = False
                    break
            if ok:
                res.append(w)
        return res

class Solution:
	def findWords(self, words):
		set1 = set(list('QWERTYUIOP'))
		set2 = set(list('ASDFGHJKL'))
		set3 = set(list('ZXCVBNM'))
		result =[]
		if words==[]:
			return result
		for word in words:
			word1 = word.upper()
			if (set(word1)|set1)==set1 or (set(word1)|set2)==set2 or (set(word1)|set3)==set3:
				result.append(word)
		return result


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = "qwertyuiop"
        b = "asdfghjkl"
        c = "zxcvbnm"
        res = []
        for word in words:
            x, y, z = 0, 0, 0
            for w in word:
                if w in a or w.lower() in a:
                    x += 1
                elif w in b or w.lower() in b:
                    y += 1
                elif w in c or w.lower() in c:
                    z += 1
                else:
                    pass
                if x == len(word) or y == len(word) or z == len(word):
                    res.append(word)
        return res


