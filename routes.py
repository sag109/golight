import webapp2
import os


from google.appengine.ext.webapp import template


app = webapp2.WSGIApplication([
        #('/','controllers.home.RenderHome'), Kept until we clarify main v. home
        ('/','controllers.main.RenderMain'), 
        ('/friends','controllers.friends.RenderFriends'), 
        ('/login','controllers.login.RenderLogin'),      
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()
#user progile should have name, email, list of friends, status