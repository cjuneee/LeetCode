import string
import random

full_tiny = {}
tiny_full = {}
chars = string.ascii_letters + string.digits


class Codec:

    def encode(self, longUrl):
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            tmp = [random.choice(chars) for i in range(6)]
            tmp = ''.join(tmp)
            full_tiny[longUrl] = tmp
            tiny_full[tmp] = longUrl
            return "http://tinyurl.com/" + tmp
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

    def decode(self, shortUrl):
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return 0
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))