#!/usr/bin/env python
import sys
import Pyblosxom.pyblosxom
from flup.server.fcgi import WSGIServer

sys.path.insert(0, "__DEPLOYDIR__")
app = Pyblosxom.pyblosxom.PyBlosxomWSGIApp()
server = WSGIServer(app)

ret = server.run()
sys.exit(ret) 

