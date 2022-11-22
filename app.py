import requests
import requests.auth
import json
import sys
import getToken
import postSchema_pb2 as pb # the file that compilet from '.proto'
from google.protobuf.json_format import MessageToJson, Parse

# Definitions #
TOKEN = sys.argv[1]
KEYWORD = sys.argv[2]
LIMIT = sys.argv[3]
HEADERS = {**getToken.headers, **{"Authorization": f"bearer {TOKEN}"}}


# Reading old data from .json file
file = open('posts.json')
data = json.dumps(json.load(file))
file.close()

postList = Parse(data,pb.PostList()) # Converting data to Protobuf object
after = postList.posts[-1].name

# Request
result = requests.get("https://oauth.reddit.com/search", 
                        headers = HEADERS,
                        params={'q':KEYWORD,'limit':LIMIT,'after':after}
                    )
# try:

for item in result.json()['data']['children']:
    post = item['data']

    # Declare Post model
    p = postList.posts.add()

    # Add values to the model.
    p.name = post['name']
    p.subreddit = post['subreddit']
    p.author_fullname = post['author_fullname']
    p.title = post['title']
    p.subreddit_name_prefixed = post['subreddit_name_prefixed']
    p.ups = post['ups']
    p.thumbnail = post['thumbnail']
    p.created = post['created']
    p.subreddit_id = post['subreddit_id']
    p.id = post['id']
    p.url = post['url']
    p.num_comments = post['num_comments']
    p.total_awards_received = post['total_awards_received']

# Open file and rewrite file with new data
file = open('posts.json','w',encoding='utf-8')
file.write(MessageToJson(postList)) # Convert Model to Json format
file.close()

# except Exception as e:
#     print(f"Error occurred: {e}. \n Program is closing...")
