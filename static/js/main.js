var mainView= "My Friends";
var updateProcedure;
var currentGroup= "qxz7";


$(document).ready(function() {
	setInterval(function () {
    	updateGroupList();
	}, 20000);
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
	if(mainView === currentGroup)
    {
        currentGroup = "qxz7";
    }
    else
    {
        currentGroup = mainView;
    }
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

		if(!(currentGroup === "qxz7"))//no group open
        {
        	if(currentGroup === "My Friends")
        	{
        		document.getElementById("myfriends").className = "panel-collapse collapse in";
        	}
        	else
        	{
        		console.log("is a group");
            	var gName = "";
            	for(var i = 0; i< groups.length; i++){
                	gName = groups[i].name;
                	if(gName === currentGroup)
                	{
                		console.log("opening");
	                    document.getElementById("group"+i).className = "panel-collapse collapse in";
                	}
	            }
        	}
            //is 
        }

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
	str+='<div class="col-xs-7 col-sm-4 col-md-4 col-lg-2">';
	str+='<input id="'+groupName+'_blurb" type="text" class="form-control" placeholder="Your blurb">';
	str+='</div>';
	str+='<div class="col-xs-4 col-sm-2 col-md-2 col-lg-1">';
	str+='<button class="btn btn-default" type="button" id="set_'+groupName+'_blurb" onclick="changeBlurb(this,&quot;'+groupName+'&quot)">Set blurb</button>';
	str+='</div>';
	str+='</div>';
	//console.log('calling showPage: '+groupName);
	showPage(groupName);
	return str;
}

function getScheduleBar(groupName){
	var str = "";
	if( typeof groupName == 'undefined')
		groupName = 'friend';
	//console.log('groupName is '+groupName);
	groupName.split(' ').join('_'); //change spaces to underscores because fuck ID naming convention

	str+='<div class="row">';
	str+='<div div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"><h4>Set your schedule</h4></div>';
	
	//day
	str+='<div class="col-xs-6 col-sm-2 col-md-2 col-lg-2">';
	str+='<div class="form-inline">';
	str+='<div class="dropdown">';
	str+='<button class="btn btn-default dropdown-toggle" type="button" id="'+groupName+'_schedule_day" data-toggle="dropdown">Day<span class="caret"></span></button>';
	str+='<ul class="dropdown-menu" role="menu" id="'+groupName+'_schedule_day" aria-labelledby="menu">';
	str+='<li role="presentation"><a role="menuitem" id="day_0" tabindex="0" onclick="setScheduleDay(0,&quot;'+groupName+'&quot);" >Sunday</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="day_1" tabindex="0" onclick="setScheduleDay(1,&quot;'+groupName+'&quot);">Monday</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="day_2" tabindex="0" onclick="setScheduleDay(2,&quot;'+groupName+'&quot);">Tuesday</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="day_3" tabindex="0" onclick="setScheduleDay(3,&quot;'+groupName+'&quot);">Wednesday</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="day_4" tabindex="0" onclick="setScheduleDay(4,&quot;'+groupName+'&quot);">Thursday</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="day_5" tabindex="0" onclick="setScheduleDay(5,&quot;'+groupName+'&quot);">Friday</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="day_6" tabindex="0" onclick="setScheduleDay(6,&quot;'+groupName+'&quot);">Saturday</a></li>';
	str+='</ul>';
	str+='</div>';
	str+='</div>';
	str+='</div>';
	//time
	str+='<div class="col-xs-6 col-sm-2 col-md-2 col-lg-2 ">';
	str+='<div class="form-inline">';
	str+='<div class="dropdown">';
	str+='<button class="btn btn-default dropdown-toggle" type="button" id="'+groupName+'_schedule_time" data-toggle="dropdown">Time<span class="caret"></span></button>';
	str+='<ul class="dropdown-menu" role="menu" id="'+groupName+'_schedule_time" aria-labelledby="menu">';
	str+='<li role="presentation"><a role="menuitem" id="time_0" tabindex="0" onclick="setScheduleTime(0,&quot;'+groupName+'&quot)">0:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_1" tabindex="0" onclick="setScheduleTime(1,&quot;'+groupName+'&quot)">1:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_2" tabindex="0" onclick="setScheduleTime(2,&quot;'+groupName+'&quot)">2:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_3" tabindex="0" onclick="setScheduleTime(3,&quot;'+groupName+'&quot)">3:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_4" tabindex="0" onclick="setScheduleTime(4,&quot;'+groupName+'&quot)">4:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_5" tabindex="0" onclick="setScheduleTime(5,&quot;'+groupName+'&quot)">5:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_6" tabindex="0" onclick="setScheduleTime(6,&quot;'+groupName+'&quot)">6:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_7" tabindex="0" onclick="setScheduleTime(7,&quot;'+groupName+'&quot)">7:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_8" tabindex="0" onclick="setScheduleTime(8,&quot;'+groupName+'&quot)">8:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_9" tabindex="0" onclick="setScheduleTime(9,&quot;'+groupName+'&quot)">9:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_10" tabindex="0" onclick="setScheduleTime(10,&quot;'+groupName+'&quot)">10:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_11" tabindex="0" onclick="setScheduleTime(11,&quot;'+groupName+'&quot)">11:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_12" tabindex="0" onclick="setScheduleTime(12,&quot;'+groupName+'&quot)">12:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_13" tabindex="0" onclick="setScheduleTime(13,&quot;'+groupName+'&quot)">13:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_14" tabindex="0" onclick="setScheduleTime(14,&quot;'+groupName+'&quot)">14:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_15" tabindex="0" onclick="setScheduleTime(15,&quot;'+groupName+'&quot)">15:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_16" tabindex="0" onclick="setScheduleTime(16,&quot;'+groupName+'&quot)">16:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_17" tabindex="0" onclick="setScheduleTime(17,&quot;'+groupName+'&quot)">17:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_18" tabindex="0" onclick="setScheduleTime(18,&quot;'+groupName+'&quot)">18:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_19" tabindex="0" onclick="setScheduleTime(19,&quot;'+groupName+'&quot)">19:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_20" tabindex="0" onclick="setScheduleTime(20,&quot;'+groupName+'&quot)">20:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_21" tabindex="0" onclick="setScheduleTime(21,&quot;'+groupName+'&quot)">21:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_22" tabindex="0" onclick="setScheduleTime(22,&quot;'+groupName+'&quot)">22:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_23" tabindex="0" onclick="setScheduleTime(23,&quot;'+groupName+'&quot)">23:00</a></li>';
	str+='<li role="presentation"><a role="menuitem" id="time_24" tabindex="0" onclick="setScheduleTime(24,&quot;'+groupName+'&quot)">24:00</a></li>';
	str+='</ul>';
	str+='</div>';
	str+='</div>';
	str+='</div>';
	//status
	str+='<div class="col-xs-6 col-sm-2 col-md-2 col-lg-2">';
	str+='<div class="form-inline">';
	str+='<div class="dropdown">';
	str+='<button class="btn btn-default dropdown-toggle" type="button" id="'+groupName+'_schedule_status" data-toggle="dropdown">Your Status<span class="caret"></span></button>';
	str+='<ul class="dropdown-menu" role="menu" id="'+groupName+'_schedule_status" aria-labelledby="menu">';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-success" id="suc" tabindex="0" onclick="setScheduleStatus(1,&quot;'+groupName+'&quot)">Available</a></li>';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-warning" id="war" tabindex="0" onclick="setScheduleStatus(0,&quot;'+groupName+'&quot)">Tentative</a></li>';
	str+='<li role="presentation"><a role="menuitem" class="btn btn-danger"  id="dan" tabindex="0" onclick="setScheduleStatus(-1,&quot;'+groupName+'&quot)">Busy</a></li>';
	str+='</ul>';
	str+='</div>';
	str+='</div>';
	str+='</div>';
	str+='<div class="col-xs-6 col-sm-2 col-md-2 col-lg-2">';
	str+='<button class="btn btn-default" type="button" id="set_'+groupName+'_blurb" onclick="SCHEDULESTATUS(&quot;'+groupName+'&quot)">Set Schedule</button>';
	str+='</div>';
	str+='<span id="scheduleResponse'+groupName+'" class="col-xs-6 col-sm-2 col-md-2 col-lg-2"></span>';
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
	fillString += getScheduleBar();
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
			grouppanel.innerHTML= getStatusBar(groupname) + getScheduleBar(groupname) + fillGroup(members);
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
