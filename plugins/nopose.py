"""
'No pose' Plugin.  Prevents folks impersonating you on your blog,
though you can use this to prevent any kind of author/email/url filtering

Requires: The "comments" plugin.

This plugin prevents anyone adding a comment through the web interface using
your name, email, or URL.
You can use regular expressions to finetune the matching.
I didn't see how you can make the regex itself case insensitive, so the code takes care of it,
which implies all your strings will be matched case insensitively.
Here's an example of what I put in my config.py:
py['np_author'] = "dieter_be|dieter@be|dieterbe|dieter.*plaetinck"
py['np_email'] = "dieter@plaetinck.be"
py['np_url'] = "dieter.plaetinck.be|plaetinck.be"
"""

__author__ = "Dieter Plaetinck"
__version__ = "0.1"

def verify_installation(request):
    config = request.getConfiguration()

    enabledchecks = 0
    for i in ('author', 'email', 'url'):
        i = "np_"+i
        if i in config:
            enabledchecks+=1
        else:
            print "missing optional property: '%s'" % i
    if not enabledchecks:
        print "Error: you must enable at least one paramater to be useful"
        return 0

    return 1

def cb_comment_reject(args):
    """
    Verifies that the commenter did not try to impersonate you.

    @param args: a dict containing: pyblosxom request, comment dict
    @type config: C{dict}
    @return: True if the comment should be rejected, False otherwise
    @rtype: C{bool}
    """
    request = args['request']
    form = request.getForm()
    data = request.getData()
    config = request.getConfiguration()
    import re
    for param in ('author', 'email', 'url'):
        try:
            submitted = form[param].value
	    regex = config["np_"+param]
            if re.search(regex, submitted, flags=re.IGNORECASE):
                return True
        except KeyError:
            pass
    return False
