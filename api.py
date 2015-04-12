import webapp2

app = webapp2.WSGIApplication([
        ('/api2/status', 'api2.status.Status'),
        ('/api2/settings', 'api2.settings.NameSettings'),
        ('/api2/friends/<friend_key>', 'api2.friends.Friends'),
        ('/api2/friends/requests/<friend_key>', 'api2.friends.FriendRequests'),
        ('/api2/friends', 'api2.friends.FriendsList'),
        ('/api2/groups', 'api2.groups.GroupsList'),
        ('/api2/groups/<group_key>/members', 'api2.groups.MemberList'),
        ('/api2/groups/<group_key>/status', 'api2.groups.GroupStatus'),
        ('/api2/groups/<group_key>/description', 'api2.groups.GroupDescription'),
        ('/api2/groups/<group_key>/admins', 'api2.groups.AdminList'),
        ('/api2/groups/<group_key>/admins/<user_id>', 'api2.groups.Admins')
    ], debug=True)

def main():
    app.RUN()

if __name__ == "__main__":
    main()
