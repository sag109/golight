var mainView= "Your Friends";
var updateProcedure;


$(document).ready(function() {
	//setInterval(fillWithFriends(), 3000);
	fillWithFriends();
	updateGroupList();
});

function setMainView(target) {
	mainView = target.innerHTML;
	showPage(); //added this
	updateMainView();
}

function updateGroupList() {

	requestInfo("get", "user/groups", {}, function(groups) {
		var groupList = "";
		for(var i=0; i<groups.length; i++) {
			var cur = groups[i];
			groupList += '<div class="panel panel-default">';
				groupList += '<div class="panel-heading">';
					groupList += '<h4 class="panel-title">';
					groupList += '<a data-toggle="collapse" data-parent="#groupaccordion" href="#group'+i+'">';
					groupList += cur.name;
					groupList += '</a>';
					groupList += '</h4>';
				groupList += '</div>';
				groupList += '<div id="group'+i+'" class="panel-collapse collapse">';
					groupList += '<div class="panel-body" id="group'+i+'pb">';
					groupList += '</div>';
				groupList += '</div>';
			groupList += '</div>';
		}
		$("#othergroups").html(groupList);

		fillGroupPanels();
	});
}

function fillGroupPanels(){
	requestInfo("get", "user/groups", {}, function(groups) {
		var groupList = "";
		for(var i=0; i<groups.length; i++) {
			var cur = groups[i];
			fillWith("group"+i+"pb", cur.name);
		}
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
	var friendpanel = document.getElementById("myfriendspb");
	var fillString= getStatusBar();
	for(var i=0; i<friends.length; i++) {
		fillString += "<div class='row'>";
		if(friends[i].status === 1)
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-success\">"+friends[i].name+"</span></h4></div>";
		else if(friends[i].status === 0)
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-warning\">"+friends[i].name+"</span></h4></div>";
		else
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-danger\">"+friends[i].name+"</span></h4></div>";
		fillString +="<div class='col-xs-7 col-sm-5 col-md-4 col-lg-4'><h4>"+ friends[i].message + "</h4></div>";
		fillString +="</div>";
	}
	friendpanel.innerHTML=fillString;
}
function fillWith(groupid, groupname){
		var str;
		var statuses = requestInfo("get", "group", {"groupName":groupname}, function(members){
			var grouppanel = document.getElementById(groupid);
			grouppanel.innerHTML=fillGroup(members);
		});
}
function fillGroup(members){

	var fillString= "";
	for(var i=0; i<members.length; i++) {
		fillString += "<div class='row'>";
		if(members[i].status === 1)
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-success\">"+members[i].email+"</span></h4></div>";
		else if(members[i].status === 0)
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-warning\">"+members[i].email+"</span></h4></div>";
		else
			fillString += "<div class='col-xs-5 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-danger\">"+members[i].email+"</span></h4></div>";
		fillString +="<div class='col-xs-7 col-sm-5 col-md-4 col-lg-4'><h4>"+ members[i].blurb + "</h4></div>";
		fillString +="</div>";
	}
	return fillString;
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
