# vim: tabstop=4 shiftwidth=4 expandtab
"""
Preformatter which uses pygments to highlight source code syntax
In your entries, you can highlight code by wrapping it in 'code' tags.
You can specify a language by using making the 'lang' attribute a lexer
shortname. See http://pygments.org/docs/lexers/
Otherwise, the most appropriate lexer will be guessed.

Examples:
* Within CDATA tags, you can literally put the source code (recommended)

<code><![CDATA[
your_source_code(<somevariable>); /* here */
echo ("<html><tag foo='bar'>");
]]></code>

* Otherwise, you need to replace html entities by their references
  (use this when you have (short) source code, without html entities)

<code lang="html">&lt;html&gt;</code>


Depends on pygments, lxml, beautiful-soup
"""
__author__ = 'Dieter Plaetinck <dieter@plaetinck.be>'
__version__ = "0.1"
__url__ = "http://pyblosxom.sourceforge.net/"
__description__ = "Preformatter which uses pygments to highlight source code syntax."
PREFORMATTER_ID = 'syntaxhighlight'

from pygments import highlight
from pygments.lexers import PythonLexer, get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
from lxml import etree
from lxml.html.soupparser import fromstring

def cb_start(args):
    request = args["request"]

def cb_preformat(args):
    """
    Preformat callback chain looks for this.

    @param args: a dict with 'parser' string and a list 'story'
    @type args: dict
    """
    if args['parser'] == PREFORMATTER_ID:
        return parse(''.join(args['story']))

def parse(text):
    """
    Find code and highlight it

    @param text: A text for conversion
    @type text: string
    """
    tree = fromstring(text)
    code = tree.xpath('//code')
    for el in code:
        highlightcallback (el)

    result = etree.tostring(tree)
    return result

def highlightcallback (code):
    try:
        lexer = get_lexer_by_name(code.attrib['lang'])
    except Exception, e:
        lexer = guess_lexer(etree.tostring(code))
    output = code.text_content() # same as `etree.tostring(code, method='text')` afaict
    output = highlight(output, lexer, HtmlFormatter())
    # NOTE: emitting the styles like this doesn't feel right
    # if you have multiple entries with source code -> redundant style tags
    # plus, all this style info doesn't really belong in the html
    output = '<style>' + HtmlFormatter().get_style_defs('.highlight') + '</style>' + output
    newElement = fromstring(output)
    code.clear()
    code.append(newElement)

def verify_installation(request):
    try:
        import lxml
        import pygments
        import lxml.html.soupparser
    except Exception, e:
        print "Missing dependencies: %s" % str(e)
        return 0
    return 1
