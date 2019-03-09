from flask import Flask
import praw 
from praw.models import MoreComments
import re
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost/myDatabase"
mongo = PyMongo(app)
@app.route('/')
def hello():
    reddit = establish_connection_reddit()
    nbastreams = reddit.subreddit('nbastreams')
    print(mongo.db)
    return str(find_matching_urls(find_all_urls(nbastreams), 'givemereddit'))
    # print_submission_posts(nbastreams)

def establish_connection_reddit():
    return praw.Reddit(client_id = 'MNzwZZ8NzvaG7g', 
        client_secret = 'rsCmArJ4Bact9Aa1rSi5_Aa89s8',
        user_agent = 'chrome:com.example.testpythonscript:v1 (by /u/throwawayacc832)')

def print_submission_posts(subreddit):
    submissions = []
    for submission in subreddit.new(limit=100):
        submissions.append(submission.id)
    return submissions

def find_all_urls(subreddit): # finds all urls in a subreddit and returns an array
    all_urls = []

    for submission in subreddit.new(limit=100):
        for comment in submission.comments: 
            for url in find_url(comment.body):
                all_urls.append(url)
    return all_urls

def find_url(str): # finds url in a given string and returns an array
    # url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str) 
    url = re.findall(r'(https?://\S+)', str)

    return url
    

def find_matching_urls(urls, str): # finds urls that have the given string
    matching_urls = []
    for url in urls:
        low = 0
        while (low < len(url)):
            if str == url[low:low + len(str)]:
                matching_urls.append(url)
                # print(string)
            low+=1
    return matching_urls
    
# TODO: Game submissions that matches a format. 
def game_submissions(subreddit):
    


# TODO: If game submissions match format, must retrieve links that match buffstreams and two top. Put into database

if __name__ == '__main__':
    app.run()