var mainView= "Your Friends";
var updateProcedure;


$(document).ready(function() {
	updateMainView();
	showPage();
	updateGroupList();
	setInterval(updateMainView, 3000);
	setInterval(updateGroupList, 3000);
	friendTable = $("#friendTable");
});

friendList = [];

function setMainView(target) {
	mainView = target.innerHTML;
	showPage(); //added this
	updateMainView();
}

function updateGroupList() {
	requestInfo("get", "user/groups", {}, function(groups) {
		var groupList = "<li onclick=\"setMainView(this)\" class=\"sidebar-brand group-link\">Your Friends</li>";
		for(var i=0; i<groups.length; i++) {
			var cur = groups[i];
			groupList += "<li onclick=\"setMainView(this)\" class=\"sidebar-brand group-link\">"+ cur.name +"</li>";
		}
		groupList+= "<li><a href=\"/plus\"><h1>+</h1></a></li>";
		$("#group_list").html(groupList);
	});
}


function updateMainView(){
	if (mainView === "Your Friends"){
		fillWithFriends();
	}

	else{
		fillWith();
		//fillWith mainView
	}

}

function fillWithFriends(){
	var friendTitle = document.getElementById("mainView");
	friendTitle.innerHTML=mainView;
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
function fillWith(){
	var friendTitle = document.getElementById("mainView");
		friendTitle.innerHTML=mainView;
		var statuses = requestInfo("get", "group", {"groupName":mainView}, function(members){
			fillGroup(members);
		});
}
function fillGroup(members){

var friendTable = document.getElementById("status_list");
	var fillString= "<tr><td>";
	//fillString = fillString+JSON.stringify(friends);
	//fillString = fillString+"</td></tr>"
	for(var i=0; i<members.length; i++) {
		fillString += "<tr>";
		//fillString += friends[i].name + "</td><td>";
		console.log('members[i].name is '+members[i].name);
		if(members[i].status === 1)
			fillString += "<td><h3><span class=\"label label-success\">"+members[i].name+"</span></h3></td>";
		else if(members[i].status === 0)
			fillString += "<td><h3><span class=\"label label-warning\">"+members[i].name+"</span></h3></td>";
		else
			fillString += "<td><h3><span class=\"label label-danger\">"+members[i].name+"</span></h3></td>";
		fillString +="<td class=\"table_status\"><h3>"+ members[i].blurb + "</h3></td></tr>";
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
	$.ajax(endpoint + "?" + parametersString, {
		method: method,
		success: function(response) {
			return success($.parseJSON(response));
		}
	});
}