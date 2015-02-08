import webapp2
import os
#from controllers.home import RenderHome

from google.appengine.ext.webapp import template

#class RenderHome(webapp2.RequestHandler):
   # def get(self):
      
      #  self.response.out.write("templates/index.html")


app = webapp2.WSGIApplication([
        ('/','controllers.home.RenderHome'),       
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()