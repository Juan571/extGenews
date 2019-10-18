from gnewsclient import NewsClient

from pprint import pprint

client = NewsClient();
#client.location = ''

# client = gnewsclient.NewsClient(language='hindi', location='india', topic='Business', max_results=3)

#pprint(client.get_news())
## pprint(client.languages)
client.language = 'spanish'

client.location = 'venezuela'
client.query = 'maduro'

pprint(client.get_news())
#pprint(client.topics)