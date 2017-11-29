#!/usr/bin/env python3
# coding=UTF-8

import os
import time
import sys

'''backup files in a zip on directories named by date'''

source=str(sys.argv[1])
target_up=str(sys.argv[2])

comment=input('Enter a comment -->')

if len(comment)==0:
    name=time.strftime('%H:%M')+'.zip'
else:
    name=time.strftime('%H:%M_')+comment.replace(' ','_')+'.zip'

date=time.strftime('%y,%m,%d')

target_mid=target_up+os.sep+date
target_final=target_up+os.sep+date+os.sep+name

if not os.path.exists(target_mid):
    os.mkdir(target_mid)
    print('Target directory doesn\'t exist,created a new one')

command='zip -r {} {}'.format(target_final,source)

if os.system(command)==0:
    print('Backup finished')
else:
    print('Backup failed')