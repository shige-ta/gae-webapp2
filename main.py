 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2
import logging

class HelloWebapp2(webapp2.RequestHandler):

    def get(self):
        self.response.write('Hello, webapp2!')

    def post(self):
        logging.debug(self.request)

app = webapp2.WSGIApplication([
    ('/post/', HelloWebapp2),
], debug=True)
