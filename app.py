import requests
import requests.auth
import json
import sys
import getToken
import postSchema_pb2 as pb # the file that compilet from '.proto'

# Definitions #
TOKEN = sys.argv[1]
KEYWORD = sys.argv[2]
LIMIT = sys.argv[3]
AFTER = sys.argv[4]
HEADERS = {**getToken.headers, **{"Authorization": f"bearer {TOKEN}"}}

postList = pb.PostList()

try:
    with open('posts', 'ab+') as file:
        respond = ''
        while respond != "q":
            # Request
            result = requests.get("https://oauth.reddit.com/search", 
                                    headers = HEADERS,
                                    params={'q':KEYWORD,'limit':LIMIT,'after':AFTER}
                                )
            for item in result.json()['data']['children']:
                post = item['data']
                # After first request takes last post name. 
                AFTER = post['name']
                # Declare Post model
                p = postList.posts.add()
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
                
            respond = input("Press 'q' for quit:")

        file.write(postList.SerializeToString())

except Exception as e:
    print(f"Error occurred: {e}. \n Program is closing...")
