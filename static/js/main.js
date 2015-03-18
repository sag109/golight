var mainView= "Your Friends";
var updateProcedure;


$(document).ready(function() {
	friendUpdate = setInterval(getFriends, 3000);
	friendTable = $("#friendTable");
});

friendList = [];

function updateMainView(){
	if (mainView === "Your Friends"){
		fillWithFriends();
	}

	else{
		fillWith(mainView);
	}

}

function fillWithFriends(){
	var friendTitle = document.getElementById("mainView");
	friendTitle.innerHTML=mainView;
	var friendTable = document.getElementById("status_list");
	var fillString;
	var statuses = requestInfo("get", "friends", {}, function(friends){
		fillFriends(friends);
	});

}
function fillFriends(friends){
	var friendTable = document.getElementById("status_list");
	var fillString= "<tr><td>";
	//fillString = fillString+JSON.stringify(friends);
	//fillString = fillString+"</td></tr>"
	for(var i=0; i<friends.length; i++) {
		fillString += "<tr>";
		//fillString += friends[i].name + "</td><td>";
		if(friends[i].status === 1)
			fillString += "<td><h3><span class=\"label label-success\">"+friends[i].name+"</span></h3></td>";
		else if(friends[i].status === 0)
			fillString += "<td><h3><span class=\"label label-warning\">"+friends[i].name+"</span></h3></td>";
		else
			fillString += "<td><h3><span class=\"label label-danger\">"+friends[i].name+"</span></h3></td>";
		fillString +="<td class=\"table_status\"><h3>"+ friends[i].message + "</h3></td></tr>";
	}
	friendTable.innerHTML=fillString;
}

function getFriends() {
	var friends = requestInfo("get", "friends", {}, function(friends) {
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