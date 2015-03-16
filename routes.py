import webapp2
import os


from google.appengine.ext.webapp import template


app = webapp2.WSGIApplication([
        ('/','controllers.friends.Friends'),
        ('/profile','controllers.profile.RenderProfile'),
        ('/edit', 'controllers.editFriends.RenderEdit'), 
        ('/user','controllers.user.User'), 
        ('/friends','controllers.friends.Friends'),
        ('/friend','controllers.friend.Friend'),  
        ('/group','controllers.group.Group'),  
        ('/group/user','controllers.group_user.User'),  
        ('/group/members','controllers.group_members.Members'),  
        ('/group/member','controllers.group_member.Member'),  
        ('/group/blurb','controllers.group_blurb.Blurb'),
        ('/test', 'controllers.test.Test')
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()
#user progile should have name, email, list of friends, status