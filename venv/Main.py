import os
import discord
import praw
import urllib.request


reddit = praw.Reddit(
    client_id="lryIbttsVw_Tsw",
    client_secret="MvB0t6qjx0VsMOw6TOgX_bae-R4",
    user_agent="Testing script",
)

def PostToDiscord(channel, title, type, content):
    pass
def GetPostContent(submission):
    if not hasattr(submission, 'post_hint'):
        if hasattr(submission, 'selftext'):
            return 'text', submission.selftext
        else:
            return 'empty', ''
    if submission.post_hint == 'hosted:video':
        deeperIntoMedia = submission.media
        if type(deeperIntoMedia) == 'NoneType':
            return 'mediaErr', ''
        url_link = deeperIntoMedia['reddit_video']['fallback_url']
        return 'video', url_link
    elif submission.post_hint == 'image':
        deeperIntoPreview = submission.preview
        url_link = deeperIntoPreview['images'][0]['source']['url']
        return 'image', url_link
    elif submission.post_hint == 'link':
        if  hasattr(submission, 'crosspost_parent'):
            crosspostParent = submission.crosspost_parent
            if crosspostParent[0] + crosspostParent[1] == 't3':
                n = len(crosspostParent)
                i = 3
                crosspostParentLink = ''
                while i < n:
                    crosspostParentLink += crosspostParent[i]
                    i += 1
            else:
                return 'crossErr', ''
            crossSubmission = reddit.submission(crosspostParentLink)
            GetPostContent(crossSubmission)
        #else url attribute with a link to external resource


def RedditMain():
    # memes  Unexpected Whatcouldgowrong UNBGBBIIVCHIDCTIICBG WritingPrompts  worldnews dirtypenpals SpicyWi gentlemanboners
    for submission in reddit.subreddit("Whatcouldgowrong").top("day", limit=10):
        titleC = submission.title
        print(submission.title)
        typeCnt, textCnt = GetPostContent(submission)
        if typeCnt == 'image':
            urllib.request.urlretrieve(textCnt, 'image.png')
            PostToDiscord()
            return
        elif typeCnt == 'video':
            urllib.request.urlretrieve(textCnt, 'video.mp4')
            PostToDiscord()
            return
        elif typeCnt == 'crossErr':
            pass
        elif typeCnt == 'mediaErr':
            pass
        elif typeCnt == 'empty':
            pass


#________________________________________________________________________________________________
#RedditMain()



TOKEN = 'ODIyMDcyMDA4Njk1MDg3MTE0.YFM8OA.m_WTi_VlXpNSGagz1AVRekTzMaQ'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '1':
        await message.channel.send('Hello!')

    if message.content.startswith('!'):
        await message.channel.send(file=discord.File('testVideo.mp4'))

client.run(TOKEN)

u = 8

