XChat extra
=========

xchat-extra contains extra plugins and scripts  fro XChat2

URL Shortner script
-----------
url shortner script will search sending messages for URL patterns and shortner them.
to do that (after installing scripts, see below) you should place an exclamation mark (!) behind the URL. if you place two exclamation marks (!!), the script will try to shortner the URL as much as possible by removing the obvious parts of short_url (http://). consider following examples:


    !http://wikipedia.org
    http://wikipedia.org (since it's already short)
    
    !http://en.wikipedia.org/wiki/GNU_General_Public_License
    http://tinyurl.com/og5oj (short url)
    
    !!http://en.wikipedia.org/wiki/GNU_General_Public_License
    tinyurl.com/og5oj (removed http:// just to make it shorter)

you can tweak the script by changing the `SHORTENER_*` global values

Installation
-----------

just copy the scripts into your XChat home directory and restart your client

    cp url_shortner.py ~/.xchat2/
   
or use **plugins and scripts** window in Xchat->Window to load them

License
-----------

GPL v3.0 or later

Devloper
-----------

bijan ebrahimi <bijanebrahimi@lavabit.com>
