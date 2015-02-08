import webapp2
import os


from google.appengine.ext.webapp import template


app = webapp2.WSGIApplication([
        ('/','controllers.home.RenderHome'),       
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()