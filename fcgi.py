#!/usr/bin/env python2
import sys
import Pyblosxom.pyblosxom
from flup.server.fcgi import WSGIServer

sys.path.insert(0, "__DEPLOYDIR__")
app = Pyblosxom.pyblosxom.PyblosxomWSGIApp()
server = WSGIServer(app)

ret = server.run()
sys.exit(ret) 

