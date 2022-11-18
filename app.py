import requests
import requests.auth
import json
import sys
import getToken

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
        json_object={}
        for item in response.json()['data']['children']:
            post = item['data']
            after = post['name']
            json_object[post['name']] = {
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
                }
            print(post['title'])

        json_object = json.dumps(json_object,indent=2)
        file.write(json_object)
        respond=input("Press 'q' for quit:")
