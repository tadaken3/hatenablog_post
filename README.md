# hatenablog_post
python　script for posting hatena blog.
you nedd pｙthon 3 more.

# How to use
## Preparation
~~~~
$ git clone https://github.com/tadaken3/hatenablog-post.git
~~~~

maybe you need <code>requests, chardet</code> library. Execute below command

~~~~
$ sudo pip install requests, chardet
~~~~

## Setting
 Customize below part of `hatenablog-post.py` according to your hatena blog setting

~~~~
username = 'username'
password = 'API key'
blogname = 'yourblogname.hatenablog.com'

~~~~
## Posting
 Execute below command to post hatena blog. `blog.md` is text file written title and content.
 The first line is title.
 
~~~~
$ python hatenablog-post blog.md
~~~~

## Licence

[MIT](https://github.com/tadaken3/hatenablog_post/blob/master/LICENSE)

## Author
