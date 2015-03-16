import webapp2

from google.appengine.ext.webapp import template

class Test(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('templates/test.html', {}))
