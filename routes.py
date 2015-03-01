import webapp2
import os


from google.appengine.ext.webapp import template


app = webapp2.WSGIApplication(
        ('/','controllers.main.Main'), 
        ('/user','controllers.user.User'), 
        ('/friends','controllers.friends.Friends'),
        ('/friend','controllers.friend.Friend'),  
        ('/group','controllers.group.Group'),  
        ('/group/user','controllers.group.User'),  
        ('/group/members','controllers.group.Members'),  
        ('/group/member','controllers.group.Member'),  
        ('/group/blurb','controllers.editFriends.RenderEdit'),  
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()
#user progile should have name, email, list of friends, status