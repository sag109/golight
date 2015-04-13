var mainView= "Your Friends";
var updateProcedure;


$(document).ready(function() {
	//setInterval(fillWithFriends(), 3000);
	fillWithFriends();
});

function setMainView(target) {
	mainView = target.innerHTML;
	showPage(); //added this
	updateMainView();
}

function updateGroupList() {
	requestInfo("get", "user/groups", {}, function(groups) {
		var groupList = "<li onclick=\"setMainView(this)\" class=\"sidebar-brand group-link\">Your Friends</li>";
		//groupList += "<li class=\"group-link\">Your Groups</li>";
		for(var i=0; i<groups.length; i++) {
			var cur = groups[i];
			groupList += "<li onclick=\"setMainView(this)\" class=\"sidebar-brand group-link\">"+ cur.name +"</li>";
		}
		groupList+= "<li><a href=\"/plus\"><h1>+</h1></a></li>";
		$("#group_list").html(groupList);
	});
}

function getStatusBar(){
	var str = "";

	str+='<div class="row">';
	str+='<div class="col-xs-3 col-sm-2 col-md-2 col-lg-2">';
	str+='<div class="form-inline">';
	str+='<div class="dropdown">';
	str+='<button class="btn btn-default dropdown-toggle" type="button" id="status_dropdown" data-toggle="dropdown">Your Status<span class="caret"></span></button>';
	str+='<ul class="dropdown-menu" role="menu" id="status_dropdown" aria-labelledby="menu">';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-success" id="suc" tabindex="0" onclick="changeStatus(this)">Available</a></li>';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-warning" id="war" tabindex="0" onclick="changeStatus(this)">Tentative</a></li>';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-danger"  id="dan" tabindex="0" onclick="changeStatus(this)">Busy</a></li>';
	str+='</ul>';
	str+='</div>';
	str+='</div>';
	str+='</div>';
	str+='<div class="col-xs-5 col-sm-4 col-md-4 col-lg-2">';
	str+='<input id="user_blurb" type="text" class="form-control" placeholder="Your blurb">';
	str+='</div>';
	str+='<div class="col-xs-2 col-sm-2 col-md-2 col-lg-1">';
	str+='<button class="btn btn-default" type="button" id="set_blurb" onclick="changeBlurb()">Set blurb</button>';
	str+='</div>';
	str+='</div>';

	return str;
}

function fillWithFriends(){
	var statuses = requestInfo("get", "friends", {}, function(friends){
		fillFriends(friends);
	});

}
function fillFriends(friends){
	console.log('filling with friends');
	var friendTable = document.getElementById("myfriendspb");
	var fillString= getStatusBar();
	for(var i=0; i<friends.length; i++) {
		fillString += "<div class='row'>";
		if(friends[i].status === 1)
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-success\">"+friends[i].name+"</span></h4></div>";
		else if(friends[i].status === 0)
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-warning\">"+friends[i].name+"</span></h4></div>";
		else
			fillString += "<div class='col-cs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-danger\">"+friends[i].name+"</span></h4></div>";
		fillString +="<div class='col-xs-7 col-sm-5 col-md-4 col-lg-4'><h4>"+ friends[i].message + "</h4></div>";
		fillString +="</div>";
	}
	friendTable.innerHTML=fillString;
}
function fillWith(){
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
		//console.log('members[i].name is '+members[i].name);
		if(members[i].status === 1)
			fillString += "<td><h3><span class=\"label label-success\">"+members[i].email+"</span></h3></td>";
		else if(members[i].status === 0)
			fillString += "<td><h3><span class=\"label label-warning\">"+members[i].email+"</span></h3></td>";
		else
			fillString += "<td><h3><span class=\"label label-danger\">"+members[i].email+"</span></h3></td>";
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
