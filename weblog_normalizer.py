#!/usr/bin/env python
# Copyright (c) 2012 Joseph Bowman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in 
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
#    DEALINGS IN THE SOFTWARE.

import re
import gzip
from optparse import OptionParser

# statussearch expects the http status code to be surrounded by spaces
# TODO: Technically this could match a size in bytes as well.
#       Should probably come up with a better way to handle this.
statussearch = re.compile(" [0-9][0-9][0-9] ")
# requestsearch should catch every type of valid http method
requestsearch = re.compile("(GET|POST|HEAD|PUT|OPTIONS|DELETE|TRACE|CONNECT) (.*?)( |\"|')")

def process_file(myfile):
    for line in myfile:
        if line != "":
            #print line
            m = re.search(statussearch, line)
            if m:
                op = "%s" % m.group()
                # print op
                n = re.search(requestsearch, line)
                if n:
                    op += "%s" % n.group()
                    print op
def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read FILE", metavar="FILE")

    (options, args) = parser.parse_args()


# try to read it as a gzip file, if that fails
# just open it and pray it's ascii
    try:
        myfile = gzip.open(options.filename)
        process_file(myfile)
    except:
        myfile = open(options.filename)
        process_file(myfile)

    myfile.close()

if __name__ == "__main__":
    main()
