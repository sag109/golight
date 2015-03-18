import webapp2
import os


from google.appengine.ext.webapp import template


app = webapp2.WSGIApplication([
        ('/','controllers.main.Main'),
        ('/profile','controllers.profile.RenderProfile'),
        ('/edit', 'controllers.editFriends.RenderEdit'), 
        ('/user','controllers.user.User'), 
        ('/user/groups','controllers.user_groups.Groups'),
        ('/friends','controllers.friends.Friends'),
        ('/friend','controllers.friend.Friend'),  
        ('/group','controllers.group.Group'),  
        ('/group/user','controllers.group_user.User'),  
        ('/group/members','controllers.group_members.Members'),  
        ('/group/member','controllers.group_member.Member'),  
        ('/group/blurb','controllers.group_blurb.Blurb'),
        ('/group/add', 'controllers.add_create.Create'),
        ('/test', 'controllers.test.Test')
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()