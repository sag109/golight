$(document).ready(function() {
	friendUpdate = setInterval(getFriends, 3000);
	friendTable = $("#friendTable");
});

friendList = [];

function getFriends() {
	friends = requestInfo("get", "friends", {}, function(friends) {
		setFriends(friends);
	});
}

function setFriend(friend) {
	if(friendInTable(friend)) {
		updateFriend(friend);
	} else {
		addFriend(friend);
	}
}

function updateFriend(friend) {
	for(var i=0; i<friendTable.length; i++) {
		if(friendTable[i].email === friend.email) {
			friendTable[i] = friend;
			break;
		}
	}
}

function friendInTable(friend) {
	for(var i=0; i<friendTable.length; i++) {
		if(friendTable[i].email === friend.email) {
			return true;
		}
	}
	return false;
}

function setFriends(friends) {
	for(var i=0; i<friends.length; i++) {
		setFriend(friends[i]);
	}
}

function requestInfo(method, endpoint, parameters, success) {
	parametersString = $.param(parameters);
	$.ajax(endpoint + "?" + parameters, {
		method: method,
		success: function(response) {
			return success($.parseJSON(response));
		}
	});
}