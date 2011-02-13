"""
Two metadata entries define the dates of blog entries.  mtime is ignored.
The first metadata entry is 'pubdate'.  The format is '#pubdate YYYY-MM-DD'.
All date related data for an entry is changed.
Entries are sorted by this date as well.

An additional optional metadata entry 'pubtime', with a 24-hour format of
'#pubtime HH:MM:SS' further defines the date/time used.

Two additional story template tags are defined, '$(displaydate)' and
'$(displaytime)'.  These default to 'full_month_name DD, YYYY' and a
12-hour 'HH:MM AM/PM'.
These can be modified by using the configuration variables 'display_date' and
'display_time'.
These should be set to strings using the strftime tokens found here:
<http://docs.python.org/library/time.html#time.strftime>

Lastly, there is a configuration option 'meta_date_sort'.
If it is set to 1, the entries will be sorted by date, most recent first.
Set to -1 will have the earliest entries first, and setting it to 0 will turn
off meta date sorting (but still read dates from meta variables).

Since only the last occurance of repeated metadata entries is used, multiple
'pubdate' entries can be used to keep track of revisions if you wish.



Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright 2010 Tim Gray
"""

import time

__author__ = 'Tim Gray - tgray at 125px dot com'
__version__ = '0.1 - 8/31/10'
__url__ = 'http://www.125px.com/'
__description__ = 'Sorts entries by date in meta data'

def cb_prepare(args):
    """Takes an entry and resets all date and time variables according to the 'pubdate' and 'pubtime' entries."""

    request = args['request']
    config = request.get_configuration()
    displaydate = config.get("display_date", None)
    displaytime = config.get("display_time", None)
    data = request.get_data()
    entry_list = data["entry_list"]

    if time.daylight:
        tz = time.tzname[1]
    else:
        tz = time.tzname[0]

    for e in entry_list:
        if not e.has_key("pubtime"):
            e["pubtime"] = "00:00:00"

        if e.has_key("pubdate"):
            pubdate = time.strptime(e["pubdate"] + e["pubtime"],"%Y-%m-%d%H:%M:%S")
        else:
            pubdate = time.localtime(e["mtime"])
        e["timetuple"] = pubdate
        e["da"] = time.strftime("%d", pubdate)
        e["mo_num"] = time.strftime("%m", pubdate)
        e["mo"] = time.strftime("%b", pubdate)
        e["yr"] = time.strftime("%Y", pubdate)
        e["ti"] = time.strftime("%H:%M", pubdate)
        e["dw"] = time.strftime("%A", pubdate)
        e["date"] = e["dw"][:3] + time.strftime(", %d %b %Y", pubdate)
        e["fulltime"] = time.strftime("%Y%m%d%H%M%S", pubdate)
        _mtime = time.mktime(pubdate)
        gmtimetuple = time.gmtime(_mtime)
        e['rfc822date'] = time.strftime('%a, %d %b %Y %H:%M GMT', gmtimetuple)
        e["mtime"] = time.mktime(pubdate)
        if not displaydate:
            m = time.strftime("%B", pubdate)
            ddate = "%s %i, %i" % (m, pubdate.tm_mday, pubdate.tm_year)
        else:
            ddate = time.strftime(displaydate, pubdate)
        if not displaytime:
            dtime = time.strftime("%I:%M %p", pubdate)
        else:
            dtime = time.strftime(displaytime, pubdate)
        e["displaydate"] = ddate
        e["displaytime"] = dtime

def cb_sortlist(args):
    """Reads the 'pubdate' and optional 'pubtime' entry and sorts according to them.  If no value is found, the mtime is used.  This function also modifies the 'timetuple' for each entry for later use"""

    entrylist = args["entry_list"]
    request = args['request']
    config = request.get_configuration()
    date_sort = config.get("meta_date_sort", True)

    if not date_sort:
        return None

    entrylist2 = []
    for e in entrylist:
        if not e.has_key("pubtime"):
            e["pubtime"] = "00:00:00"

        if e.has_key("pubdate"):
            pubdate = time.strptime(e["pubdate"] + e["pubtime"],"%Y-%m-%d%H:%M:%S")
        else:
            pubdate = time.localtime(e["mtime"])
        entrylist2.append((pubdate, e))
    entrylist2.sort()

    if date_sort == 1:
        entrylist2.reverse()

    entrylist = [e[1] for e in entrylist2]

    return entrylist

def verify_installation(request):
    config = request.get_configuration()
    flag = False
    if not config.has_key("display_date"):
        print "missing optional config property 'display_date' "
        print "Allows you to specifiy the display date format"
        flag = True

    if not config.has_key("display_time"):
        print "missing optional config property 'display_time' "
        print "Allows you to specifiy the display time format"
        flag = True
    return 1


# Local Variables:
# x-typographers-quotes: false
# tab-width: 4
# x-auto-expand-tabs: true
# End:
