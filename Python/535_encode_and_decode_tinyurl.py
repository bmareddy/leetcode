class Codec:
    def __init__(self):
        self.urls_dict = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        import uuid
        short_id = str(uuid.uuid1)[:8]
        self.urls_dict[short_id]  = longUrl
        return 'http://tinyurl.com/'+short_id
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls_dict[shortUrl.replace('http://tinyurl.com/','')]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))