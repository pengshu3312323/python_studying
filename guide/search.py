##################################################
#---Search tool for the 'guide' page---
#
#---Written by:Peng Shu
##################################################
engine = {
    'baidu': 'https://www.baidu.com/s?wd=',
    }


def keywords(words):
    '''Deal with the keywords string'''
    words_list = words.split()
    keywords = '+'.join(words_list)
    return keywords


def baidu(words):
    '''Return the URL to search on Baidu'''
    url = engine['baidu']+keywords(words)
    return url

