import requests
import requests.auth
import json
import sys
import getToken
import postSchema_pb2 as pb # Protoc dosyasından üretilen paketi ekledik

TOKEN = sys.argv[1]
keyword = sys.argv[2]
limit = sys.argv[3]
after=''
respond= ''

headers = {**getToken.headers, **{"Authorization": f"bearer {TOKEN}"}}

with open('posts.json', 'w+', encoding='utf-8') as file:
    while respond != "q":
        response = requests.get("https://oauth.reddit.com/search", 
                                headers = headers,
                                params={'q':keyword,'limit':limit,'after':after}
                            )
        json_object = {
            'posts':[]
        }
        for item in response.json()['data']['children']:
            post = item['data']
            after = post['name']
            json_object['posts'].append({
                    'name': post['name'],
                    'subreddit': post['subreddit'],
                    'author_fullname': post['author_fullname'],
                    'title': post['title'],
                    'subreddit_name_prefixed': post['subreddit_name_prefixed'],
                    'ups': post['ups'],
                    'thumbnail': post['thumbnail'],
                    'created': post['created'],
                    'subreddit_id': post['subreddit_id'],
                    'id': post['id'],
                    'url': post['url'],
                    'num_comments': post['num_comments'],
                    'total_awards_received': post['total_awards_received']
                })
            print(post['title'])
        
        file.write(json.dumps(json_object,indent=2))
        respond = input("Press 'q' for quit:")


def promptForPost(p,post):
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

pL = pb.PostList()
for post in json_object['posts']:
    p = pL.posts.add()
    promptForPost(p,post)

for post in pL.posts:
    print(post)