import praw 
from praw.models import MoreComments
import re
from pymongo import MongoClient

# Establishing connection for MongoDB
client = MongoClient()


reddit = praw.Reddit(client_id = 'MNzwZZ8NzvaG7g', 
	client_secret = 'rsCmArJ4Bact9Aa1rSi5_Aa89s8',
	user_agent = 'chrome:com.example.testpythonscript:v1 (by /u/throwawayacc832)')

	

nbastreams = reddit.subreddit('nbastreams')

removed_comments = []
deleted_comments = []
edited_comments = []
comments = []
counter = 0

def find_url(string):
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
	return url 

def matching_url(string, matching):
	low = 0
	while (low < len(string)):
		if matching == string[low:low + len(matching)]:
			return string
			# print(string)
		low+=1
	return None

for submission in nbastreams.new(limit=100):
	print(submission.id)
	print(submission.title)
	if (submission.id == '9ycgq6'):
		for comment in submission.comments:
			if (comment.body == '[removed]'):
				removed_comments.append(comment)
			if (comment.body == '[deleted]'):
				deleted_comments.append(comment)
			if (comment.edited):
				edited_comments.append(comment)
			comments.append(comment)

for comment in removed_comments:
	print("Comment " + comment.id + " was removed")

print("Total number of " + str(len(removed_comments)) + " removed")

for comment in deleted_comments:
	print("Comment " + comment.id + " was deleted")

print("Total number of " + str(len(removed_comments)) + " deleted")

for comment in edited_comments:
	print("Comment " + comment.id + " was edited")

print("Total number of " + str(len(edited_comments)) + " edited")

all_urls = []

for comment in comments:
	print(comment.body)
	print("---------------------- by " + str(comment.author))
	for url in find_url(comment.body):
		all_urls.append(url)

print("Total number of " + str(len(comments)) + " comments")

for url in all_urls:
	print(url)
	str = 'nbastream.io'
	if matching_url(url, str) != None:
		print('URL MATCH SEARCHING FOR \'' + str + '\' in ' + url)


	# for comment in submission.comments:
	# 	print(comment.author)
	# 	print(comment.id)
		# print(comment.id + " added to array")
		# print(comment.body)
		# comments_from_buffstreams.append(comment)

# counter = 0
# for comment in comments_from_buffstreams:
# 	print(comment)
# 	counter += 1

# print("total num of comments: " + str(counter))




	

# for submission in nbastreams.new(limit=10):
# 	print(submission.title)
# 	print(submission.score)
# 	print(submission.id)
# 	print(submission.url)






