import praw
import re
import requests

reddit = praw.Reddit(client_id='0yndMz8j6XX_Fg',
                     client_secret='hXmGU7oe3kqsNvC7cHss8Wctu4I',
                     redirect_uri='http://localhost:8080',
                     user_agent='UserAgent')

subNames = ['Funny', 'Memes', 'Gaming']

metaData = open("MetaData.txt", "w+")

for x in subNames:
    subreddit = reddit.subreddit(x).hot(limit=5)

    for submission in subreddit:

        url = submission.url

        picName = submission.permalink

        picName = picName.split("/")
        picName = picName[5]
        print(x)
        print(picName)
        numComments = submission.num_comments
        print(numComments)

        if len(picName) == 0:
            picName = re.findall("/(.*?)", url)
        img = requests.get(url)

        auth = str(submission.author)
        print(auth + '\n')

        if '.jpg' in url or 'jpeg' in url:
            picName += ".jpg"
        elif '.png' in url:
            picName += ".png"
        elif 'imagur' in url:
            picName += ".png"
        else:
            continue

        with open(picName, "wb") as f:
            f.write(img.content)
            metaData.write('name: %s  auth: %s subreddit: %s number of comments: %d \n' % (
            str(picName), str(auth), x, numComments))
