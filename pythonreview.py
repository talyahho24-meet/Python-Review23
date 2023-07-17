def create_youtube_video(title, description):
	cl = {"title": title , "description": description, "likes": 0, "dislikes": 0,  "comments":{}}
	return cl 

def likes (cl):
	if "likes" in cl:
		cl["likes"] +=1 
	return cl 

def dislikes (cl):
	if "dislikes" in cl:
		cl["dislikes"] +=1 
	return cl

def add_comment(cl, username, comment_text):
	if comments in cl:
		cl['comments'][username] = comment_text
    return video

NEWVIDEO = {"title":"pop culture moments that eep me up at night", "likes":0, "dislikes":0, "comments":"kjhjhg"}
NEWVIDEO = dislike(NEWVIDEO)
NEWVIDEO = like(NEWVIDEO)
NEWVIDEO = comment_text(NEWVIDEO)

for i in range (495):
		my_video = like(MEWVIDEO)
print(NEWVIDEO)

