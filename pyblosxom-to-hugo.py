#!/usr/bin/env python3

# note this script is not super clean or failsafe.
# but it works for me

py="."
hugo="hugotest"
import glob
import re
import pathlib
import html
import sys

def fixheader(lines, draft=False):
    date = ""
    time = ""
    guid = ""
    tags = []

    for i, line in enumerate(lines):
        print("considering", i, line)
        line = line.strip()
        if i == 0:
            # replace entity refs like &amp; to &
            # if title contains ", those should be escaped for hugo
            title = html.unescape(line.replace('"', '\\\"'))
        else:
            if "pubdate " in line:
                date = re.sub(".*pubdate *", "", line)
            elif "pubtime " in line:
                time = re.sub(".*pubtime *", "", line)
            elif "tags " in line:
                tags = re.sub(".*tags *", "", line).split(",")
            elif "guid " in line:
                guid = re.sub(".*guid *", "", line)
            elif line.startswith("#"):
                raise Exception("unknown header directive: %s", line)
            elif line == "":
                # ignore empty line
                pass
            else:
                break

    if not date or not time:
        raise Exception("incomplete header")

    newheader = [
        "+++\n",
        "title = \"%s\"\n" % title,
        "date = \"%sT%s-04:00\"\n" % (date, time),
        "tags = [%s]\n" % ', '.join(['"%s"' % i for i in tags]),
    ]
    if draft:
        newheader.append("draft = true\n")
    newheader.append("+++\n")

    #print("header", lines[0:i])
    #print("not header", lines[i+1:i+10])

    lines = newheader + lines[i:]
    return lines

def fixreadmore(lines):
    return map(lambda line: line.replace("<!--break-->", "<!--more-->"), lines)

# note, not robust. e.g. will fail if you have </code> in your code block
def fixhighlight(lines):
    out = []
    for i, line in enumerate(lines):
        # due to how processing works in hugo, CDATA sections would show up literally. we of course don't want that
        line = line.replace('<![CDATA[', '')
        line = line.replace(']]>', '')
        # quote lang arg because lang can be like html+php
        line = re.sub('<code lang="([a-zA-Z\+]+)">', '{{< highlight "\\1" "style=default" >}}', line)
        line = line.replace('<code>', '{{< highlight "c" "style=default" >}}')  # sorry i really don't think we can do better than this, pygments invoked via hugo needs a lang specified
        out.append(line.replace('</code>', '{{< /highlight >}}'))
    return out
  
def process_entry(entry):
    base = entry[8:]
    draft = False 
    if base[-4:] == ".txt":
        new = hugo + "/content/post/" +base[:-4] + ".html"
    elif ".txt" in base:  # .txt.draft, .txt.unpub, etc
        draft = True
        new = hugo + "/content/post/" + re.sub("\.txt.*", ".html", base)
    else:  # .draft, .unpub
        draft = True
        p = pathlib.PurePath(entry)
        new = hugo + "/content/post/" + p.with_suffix('.html').name

    print(base, "---->", new)
    f = open(entry, "r")
    lines = f.readlines()
    print("lines before", lines[:20])
    lines = fixhighlight(fixreadmore(fixheader(lines, draft)))
    print("lines after", lines[:20])
    f.close()
    f = open(new, "w")
    f.write(''.join(lines))
    f.close()

def process_page(page):
    base = page[6:]
    # for my case we can assume .txt extension
    new = hugo + "/content/" +base[:-4] + ".html"
    print(base, "---->", new)
    f = open(page, "r")
    lines = f.readlines()
    lines = fixheader(lines)
    f.close()
    f = open(new, "w")
    f.write("\n".join(lines))
    f.close()

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if i.startswith('entries/'):
            process_entry(i)
        elif i.startswith('pages/'):
            process_page(i)
        else:
            print("Don't know how to process", i)
else:

    entries = glob.glob('entries/*')
    for entry in entries:
        process_entry(entry)

    pages = glob.glob('pages/*')
    for page in pages:
        process_page(page)


        
