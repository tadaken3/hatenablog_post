#!/usr/bin/env python
#coding=utf-8
import sys
import datetime
import random
import hashlib
import base64

import requests
from chardet.universaldetector import UniversalDetector

username = 'username'
api_key  = 'API key'
blogname = 'yourblogname.hatenablog.com'

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file-name' % sys.argv[0])

    file = sys.argv[1]
    charset = check_encoding(file)
    title, body = parseText(file, charset)
    data = create_data(title, body)
    post_hatena(data)

def wsse(username, api_key):
    created = datetime.datetime.now().isoformat() + "Z"
    b_nonce = hashlib.sha1(str(random.random()).encode()).digest()
    b_digest = hashlib.sha1(b_nonce + created.encode() + api_key.encode()).digest()
    c = 'UsernameToken Username="{0}", PasswordDigest="{1}", Nonce="{2}", Created="{3}"'
    return c.format(username, base64.b64encode(b_digest).decode(), base64.b64encode(b_nonce).decode(), created)

def create_data(title,body):
    template = """<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom"
           xmlns:app="http://www.w3.org/2007/app">
      <title>{0}</title>
      <author><name>name</name></author>
      <content type="text/plain">{1}</content>
      <updated>2013-09-05T00:00:00</updated>
      <app:control>
        <app:draft>yes</app:draft>
      </app:control>
    </entry>
    """
    data = template.format(title, body).encode()
    return data

def parseText(file, charset):
    with open(file, encoding=charset) as f:
        obj = f.readlines()
        title = ""
        body  = ""
        for i, line in enumerate(obj):
            if i == 0:
                title = line
            else:
                body = body + line
    return title, body

def check_encoding(file):
    detector = UniversalDetector()
    with open(file, mode='rb') as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    charset = detector.result['encoding']
    return charset

def post_hatena(data):
    headers = {'X-WSSE': wsse(username, api_key)}
    url = 'http://blog.hatena.ne.jp/{0}/{1}/atom/entry'.format(username, blogname)
    r = requests.post(url, data=data, headers=headers)
    if r.status_code != 201:
        sys.stderr.write('Error!\n' + 'status_code: ' + str(r.status_code) + '\n' + 'message: ' + r.text)

if __name__ == '__main__':
    main()
