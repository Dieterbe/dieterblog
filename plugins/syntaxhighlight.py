# vim: tabstop=4 shiftwidth=4 expandtab
"""
Preformatter which uses pygments to highlight source code syntax
In your entries, you can do <code>...</code> if you want things to get
highligted.
Depends on pygments, lxml, beautiful-soup
"""
__author__ = 'Dieter Plaetinck <dieter@plaetinck.be>'
__version__ = "0.1"
__url__ = "http://pyblosxom.sourceforge.net/"
__description__ = "Preformatter which uses pygments to highlight source code syntax."
PREFORMATTER_ID = 'syntaxhighlight'

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers import get_lexer_by_name
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
    # TODO: automatically pick lexer based on lang attribute or guess otherwise
    # TODO: when the code contains > or & etc, those must be displayed correctly, not their entity references
    output = highlight(etree.tostring(code), get_lexer_by_name('python'), HtmlFormatter())
    # NOTE: emitting the styles like this doesn't feel right
    # if you have multiple entries with source code -> redundant style tags
    # plus, all this style info doesn't really belong in the html
    output = '<style>' + HtmlFormatter().get_style_defs('.highlight') + '</style>' + output
    #TODO: remove the actual <code> </code> tags
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
        return 1
    return 0
