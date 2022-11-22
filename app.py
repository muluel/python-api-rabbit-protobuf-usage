import requests
import requests.auth
import json
import sys
import getToken
import postSchema_pb2 as pb # the file that compilet from '.proto'

# Definitions #
TOKEN = sys.argv[1]
keyword = sys.argv[2]
limit = sys.argv[3]
after =''
respond = ''
postList = pb.PostList()
p = postList.posts.add()
headers = {**getToken.headers, **{"Authorization": f"bearer {TOKEN}"}}

# Adding data to Proto Post model
def promptForPost(p, post):
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

with open('posts', 'wb+') as file:
    while respond != "q":
        response = requests.get("https://oauth.reddit.com/search", 
                                headers = headers,
                                params={'q':keyword,'limit':limit,'after':after}
                            )
        for item in response.json()['data']['children']:
            post_details = item['data']
            # After first request takes last post name. 
            after = post_details['name']
            promptForPost(p,post_details)
          
        file.write(postList.SerializeToString())
        respond = input("Press 'q' for quit:")