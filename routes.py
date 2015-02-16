import webapp2
import os


from google.appengine.ext.webapp import template


app = webapp2.WSGIApplication([
        ('/friends','controllers.friends.RenderFriends'), 
        ('/login','controllers.login.RenderLogin'),
        ('/','controllers.friends.RenderFriends'),  
        ('/profile','controllers.profile.RenderProfile'),  
        ('/edit','controllers.editFriends.RenderEdit'),  
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()
#user progile should have name, email, list of friends, status