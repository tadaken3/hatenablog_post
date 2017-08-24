# hatenablog_post
python script for posting hatena blog.　<br>
you need python 3 more.　　

# How to use
## Preparation
~~~~
$ git clone https://github.com/tadaken3/hatenablog_post.git
~~~~

maybe you need <code>requests, chardet</code> library. Execute below command

~~~~
$ sudo pip install requests
$ sudo pip install chardet
~~~~

## Setting
 Customize below part of `hatenablog_post.py` according to your hatena blog setting

~~~~
username = 'username'
api_key = 'API key'
blogname = 'yourblogname.hatenablog.com'
~~~~

## Posting
 Execute below command to post hatena blog. `blog.md` is text file written title and content.<br>
 The first line is title.
 
~~~~
$ python hatenablog_post.py blog.md
~~~~

## Licence

[MIT](https://github.com/tadaken3/hatenablog_post/blob/master/LICENSE)

## Author

[tadaken3](https://github.com/tadaken3)
