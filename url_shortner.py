#!/usr/bin/env python

# Written by Bijan Ebrahimi (bijanebrahimi@lavabit.com)
# Licensed under the GPL v3.0 or latter
#
# Usage: put ! behind the link to shorten it automatically,
#        place !! to shorten it as much as possible

__module_name__ = "URL Shortner"
__module_version__ = "0.0.1"
__module_description__ = "put ! or !! behind the link you want to shorten it"

import xchat
import os
import re
import urllib

SHORTENER_API_CUT = 7
SHORTENER_API_URL = "http://tinyurl.com/api-create.php?url=%s"
SHORTENER_API_MIN_LEN = 15
STILL_WORKING = False


def url_shortner(m):
    MAXIMUM_SHORTENING = False
    url = m.groups()[0][1:]
    print 'whole: %s' % url
    if url[0] == '!':
        MAXIMUM_SHORTENING = True
        url = url[1:]
    if len(url) > SHORTENER_API_MIN_LEN:
        try:
            short_url = urllib.urlopen(SHORTENER_API_URL % url).read()
            if MAXIMUM_SHORTENING:
                short_url = short_url[SHORTENER_API_CUT:]
            if len(short_url) < len(url):
                return short_url
        except:
            pass
    return url

def url_shortner_function(word, word_eol, userdata): 
    global STILL_WORKING
    evnt_cmd = word_eol[0]
    evnt_text = word_eol[0]
    if STILL_WORKING is False:
        # TODO: more proper regex required
        evnt_text = re.sub(r"(!{1,2}(ht|f)tps?://[^ ]+)", url_shortner, evnt_text)
        STILL_WORKING = True
        xchat.get_context().command("say " + evnt_text)
        STILL_WORKING = False
        return xchat.EAT_ALL
    return xchat.EAT_NONE

xchat.hook_command("", url_shortner_function);


