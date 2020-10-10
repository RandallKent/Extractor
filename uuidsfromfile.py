#!/usr/bin/env python
'''
  uuidsfromfile.py -- Get all unique UUIDs from a file

  by Randall Kent based on Patrick Mylund Nielsen's  http://patrickmylund.com/projects/emailsfromfile/

  License: WTFPL (http://sam.zoy.org/wtfpl/)
'''

__version__ = '1.1'

import sys
import os
import re
import codecs

# Regular expression matching with inspriation from https://stackoverflow.com/questions/136505/searching-for-uuids-in-text-with-regex
uuid_pattern = re.compile('[0-9a-f-]{36}', re.IGNORECASE)

# Strict UUID4 pattern matching
# uuid_pattern = re.compile('0-9a-f-]{14}4[0-9a-f-]{4}[89ab][0-9a-f-]{16}', re.IGNORECASE)

def main(filename, separator='\n', encoding=None):
    separator_replace = {
        'space': ' ',
        'newline': '\n',
    }
    if not os.path.isfile(filename):
        raise IOError("%s is not a file." % filename)
    results = set()
    with codecs.open(filename, 'rb', encoding) as f:
        for line in f:
            results.update(uuid_pattern.findall(line))
    for k, v in separator_replace.iteritems():
        separator = separator.replace(k, v)
    print(separator.join((list(results))))
    print('count: ' + str(len(results)))
    
if __name__ == '__main__':
    args = len(sys.argv) - 1
    if 0 < args < 4:
        main(*sys.argv[1:])
    else:
        print("Usage: python %s <filename> [separator] [encoding]" % sys.argv[0])
        print("The default separator is a newline. To separate by space, literally enter 'space' as the separator.")
        print("Written for Python 2.7")