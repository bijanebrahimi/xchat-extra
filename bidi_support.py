#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Written by Bijan Ebrahimi (bijanebrahimi@lavabit.com)
# Licensed under the GPL v3.0 or latter

__module_name__ = "BiDirectional Support"
__module_version__ = "0.0.1"
__module_description__ = "bidirectional support for xchat"

import sys
import xchat
import unicodedata
import codecs

Your_Message_HOOK = False
Channel_Message_HOOK = False
Channel_Msg_Hilight_HOOK = False
Private_Message_to_Dialog_HOOK = False

def _is_rtl(text):
    ltr_chars = 0
    rtl_chars = 0
    for ch in text:
        ch_code = unicodedata.bidirectional(ch)
        if ch_code in ['L', 'LRO', 'LRE']:
            ltr_chars += 1
        elif ch_code in ['R', 'AL', 'RLO', 'RLE']:
            rtl_chars += 1
    return rtl_chars > ltr_chars


def _bidi_text(event, nickname, msg):
    msg = unicode(msg.strip(codecs.BOM_UTF8), 'utf-8')
    if _is_rtl(msg):
        msg = u'\u200f' + msg
    xchat.emit_print(event, nickname, msg, "")


def _your_message_hook(word, word_eol, userdata):
    global Your_Message_HOOK
    if Your_Message_HOOK is False:
        Your_Message_HOOK = True
        _bidi_text('Your Message', word[0], word[1])
        Your_Message_HOOK = False
        return xchat.EAT_XCHAT


def _channel_message_hook(word, word_eol, userdata):
    global Channel_Message_HOOK
    if Channel_Message_HOOK is False:
        Channel_Message_HOOK = True
        _bidi_text('Channel Message', word[0], word[1])
        Channel_Message_HOOK = False
        return xchat.EAT_XCHAT

def _channel_msg_hilight_hook(word, word_eol, userdata):
    global Channel_Msg_Hilight_HOOK
    if Channel_Msg_Hilight_HOOK is False:
        Channel_Msg_Hilight_HOOK = True
        _bidi_text('Channel Msg Hilight', word[0], word[1])
        Channel_Msg_Hilight_HOOK = False
        return xchat.EAT_XCHAT


def _private_message_to_dialog_hook(word, word_eol, userdata):
    global Private_Message_to_Dialog_HOOK
    if Private_Message_to_Dialog_HOOK is False:
        Private_Message_to_Dialog_HOOK = True
        _bidi_text('Private Message to Dialog', word[0], word[1])
        Private_Message_to_Dialog_HOOK = False
        return xchat.EAT_XCHAT


# HACK: Set default encoding to UTF-8
# Source: http://forum.xchat.org/viewtopic.php?t=3338
if (sys.getdefaultencoding() != "utf-8"):
    oldout, olderr = sys.stdout, sys.stderr         # Backup stdout and stderr
    reload(sys)                                     # This call resets stdout and stderr
    sys.setdefaultencoding('utf-8')                 # Change encoding
    sys.stdout = codecs.getwriter('utf-8')(oldout)  # Set old stdout
    sys.stderr = codecs.getwriter('utf-8')(olderr)  # Set old stderr

xchat.hook_print("Channel Message", _channel_message_hook);
xchat.hook_print("Channel Msg Hilight", _channel_msg_hilight_hook);
xchat.hook_print("Your Message", _your_message_hook);
xchat.hook_print("Private Message to Dialog", _private_message_to_dialog_hook);
