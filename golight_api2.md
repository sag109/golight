# Golight API 2
## Let's get REST-ish
All requests and responses in JSON format. Prefix all URI with /api2/.

## Status
* __GET__ /status
  * Returns the user's current status.
  * Params:
    * time: an object with two fields, day (an int 0-6, 0 being Sunday) and hour (an int 0-23) representing the time 
    which your request is for. If empty, the time returned is now.

* __PUT__ /status
  * Updates the user's status.
  * Params:
    * status: -1, 0, or 1 corresponding to unavailable, tentative, and available respectively. If not present, no change
    is made.
    * blurb: A message, max 50 chars. If not present, no change is made.
    * time: an object with two fields, day (an int 0-6, 0 being Sunday) and hour (an int 0-23) representing the time 
    which your request is for. If empty, the time returned is now.

## Settings
* __PUT__ /settings/name
  * Updates the user's name.
  * Params:
    * name: a nonempty name, max 20 chars, to set yourself as.

## Friend Management
* __GET__ /friends/requests/KEY
  * Gets a dict of the friend requests with messages.

* __DELETE__ /friends/KEY
  * Removes this person from the user's friends list.
  
* __POST__ /friends/requests/KEY
  * Send a request to the user corresponding to the key, or become friends if you have a request from them.
  * Params:
    * message: A message, max 50 chars, to send with the request. If not present, no message is included.

* __DELETE__ /friends/requests/KEY
  * Reject a request from the user corresponding to the key.

* __GET__ /friends
  * Returns a list of the user's friends and their statuses.
  * Params:
    * time: an object with two fields, day (an int 0-6, 0 being Sunday) and hour (an int 0-23) representing the time 
    which your request is for. If empty, the time returned is now.

## Group Management
* __GET__ /groups
  * Gets a list of the groups the user is in.

* __GET__ /groups/KEY/members
  * Gets a list of the members of a group, and a table of their availabilities for the group.

* __PUT__ /groups/KEY/status
  * Sets the user's status in the group.
  * Params:
    * status: -1, 0, or 1 corresponding to unavailable, tentative, and available respectively. If not present, no change
    is made.
    * blurb: A message, max 50 chars. If not present, no change is made.
    * time: an object with two fields, day (an int 0-6, 0 being Sunday) and hour (an int 0-23) representing the time 
    which your request is for. If empty, the time returned is now.

* __POST__ /groups
  * Make a new group, with the user as the admin.
  * Params:
    * name: (Required) A nonempty name of the group, less than 20 chars.
    * description: A description for the group, less than 50 chars.
    * public: A boolean, should the group be publicly joinable? Presumed false.

* __PUT__ /groups/KEY/description
  * Update the description for a group. Can only be done by an admin.
  * Params:
    * description: What to set the description to.

* __GET__ /groups/KEY/admins
  * Returns a list of the admins for the groups.

* __POST__ /groups/GROUPKEY/admins/USERKEY
  * Adds another member as an admin of a group, can only be done by an admin.

* __DELETE__ /groups/GROUPKEY/admins/USERKEY
  * Removes an admin from a group. Can only be done by an admin. Users can delete themselves, but only if there are
  other admins remaining.