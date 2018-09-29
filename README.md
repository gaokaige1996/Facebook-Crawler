# Facebook
acsi_postids.txt is a file contains poster id and the post id. <br>
----------
In this version: poster id: poster id_ post id. <br>
This can be downloaded from Facebook API<br>

like_people.py is a file that collecting who likes the post <br>
-------------
update.py is a file that collecting replies of the post and the subreplies in that reply. <br>
---------
In this version: postid, reply userid, reply top 20 words, subreply userid, subreply top 20 words
Seperate big files.py is a file that seperate acsi_postids.txt into small txt files that we can do multithreading and run several files at the same time, improving efficiency. 
