var mainView= "Your Friends";
var updateProcedure;


$(document).ready(function() {
	setInterval(function () {
    	updateGroupList();
	}, 10000);
	showPage();
	LogoutLink();
	updateGroupList();
});

//puts a logout link in the top right corner of screen
function LogoutLink(){
	requestInfo("get", "logout", {}, function(link) {
		$('#logout_link').attr("href",link.url);
	});
}
function setMainView(target) {
	mainView = target.innerHTML;
}

function updateGroupList() {

    	console.log('updating grouplist');
	requestInfo("get", "user/groups", {}, function(groups) {
		var groupList = "";

		groupList += '<div class="panel-group" id="groupaccordion">';		

		groupList += '<div class="panel panel-default">';
		groupList += '<div class="panel-heading text-center" data-toggle="collapse" data-parent="#accordion" data-target="#myfriends">';
		groupList += '<h4 class="panel-title">';
		groupList += '<a data-toggle="collapse" data-parent="#groupaccordion" href="#myfriends" onClick="setMainView(this)">My Friends</a>';
		groupList += '</h4>';
		groupList += '</div>';
		groupList += '<div id="myfriends" class="panel-collapse collapse">';
		groupList += '<div class="panel-body" id="myfriendspb">';
		groupList += '</div>';
		groupList += '</div>';
		groupList += '</div>';

		for(var i=0; i<groups.length; i++) {
			var cur = groups[i];
			groupList += '<div class="panel panel-default">';
			groupList += '<div class="panel-heading text-center" data-toggle="collapse" data-parent="#accordion" data-target="#group'+i+'">'; ///
			groupList += '<h4 class="panel-title">';
			groupList += '<a data-toggle="collapse" data-parent="#groupaccordion" href="#group'+i+'" onClick="setMainView(this)">';
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

		groupList += '</groupaccordion>';

		//console.log(groupList);
		$("#groups").html(groupList);
		fillWithFriends();
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

function getStatusBar(groupName){
	var str = "";
	if( typeof groupName == 'undefined')
		groupName = 'friend';
	//console.log('groupName is '+groupName);
	groupName.split(' ').join('_'); //change spaces to underscores because fuck ID naming convention

	str+='<div class="row">';
	str+='<div class="col-xs-12 col-sm-2 col-md-2 col-lg-2">';
	str+='<div class="form-inline">';
	str+='<div class="dropdown">';
	str+='<button class="btn btn-default dropdown-toggle" type="button" id="'+groupName+'_dropdown" data-toggle="dropdown">Your Status<span class="caret"></span></button>';
	str+='<ul class="dropdown-menu" role="menu" id="'+groupName+'_dropdown" aria-labelledby="menu">';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-success" id="suc" tabindex="0" onclick="changeStatus(this,&quot;'+groupName+'&quot)">Available</a></li>';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-warning" id="war" tabindex="0" onclick="changeStatus(this,&quot;'+groupName+'&quot)">Tentative</a></li>';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-danger"  id="dan" tabindex="0" onclick="changeStatus(this,&quot;'+groupName+'&quot)">Busy</a></li>';
	str+='</ul>';
	str+='</div>';
	str+='</div>';
	str+='</div>';
	str+='<div class="col-xs-5 col-sm-4 col-md-4 col-lg-2">';
	str+='<input id="'+groupName+'_blurb" type="text" class="form-control" placeholder="Your blurb">';
	str+='</div>';
	str+='<div class="col-xs-2 col-sm-2 col-md-2 col-lg-1">';
	str+='<button class="btn btn-default" type="button" id="set_'+groupName+'_blurb" onclick="changeBlurb(this,&quot;'+groupName+'&quot)">Set blurb</button>';
	str+='</div>';
	str+='</div>';
	//console.log('calling showPage: '+groupName);
	showPage(groupName);
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
			fillString += "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-success\">"+friends[i].name+"</span></h4></div>";
		else if(friends[i].status === 0)
			fillString += "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-warning\">"+friends[i].name+"</span></h4></div>";
		else
			fillString += "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-danger\">"+friends[i].name+"</span></h4></div>";
		fillString +="<div class='col-xs-12 col-sm-5 col-md-4 col-lg-4'><h4>"+ friends[i].message + "</h4></div>";
		fillString +="</div>";
	}
	friendpanel.innerHTML=fillString;
}
function fillWith(groupid, groupname){
		var str;
		var statuses = requestInfo("get", "group", {"groupName":groupname}, function(members){
			var grouppanel = document.getElementById(groupid);
			grouppanel.innerHTML= getStatusBar(groupname) + fillGroup(members);
		});
}
function fillGroup(members){

	var fillString= "";
	for(var i=0; i<members.length; i++) {
		fillString += "<div class='row'>";
		if(members[i].status === 1)
			fillString += "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-success\">"+members[i].email+"</span></h4></div>";
		else if(members[i].status === 0)
			fillString += "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-warning\">"+members[i].email+"</span></h4></div>";
		else
			fillString += "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'><h4><span class=\"label label-danger\">"+members[i].email+"</span></h4></div>";
		fillString +="<div class='col-xs-12 col-sm-5 col-md-4 col-lg-4'><h4>"+ members[i].blurb + "</h4></div>";
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
