var weekday = 0;
var time = 0;
var scheduledStatus = 0;

function setScheduleDay(day,gname){
	weekday = day;
	$('#'+gname+'_schedule_day').html(''+getDay(day)+' <span class="caret"></span>');
}

function getDay(numDay){
	if(numDay == 0)
		return 'Sunday';
	else if(numDay == 1)
		return 'Monday';
	else if(numDay == 2)
		return 'Tuesday';
	else if(numDay == 3)
		return 'Wednesday';
	else if(numDay == 4)
		return 'Thursday';
	else if(numDay == 5)
		return 'Friday';
	else if(numDay == 6)
		return 'Saturday';
}

function setScheduleTime(t,gname){
	time = t;
	$('#'+gname+'_schedule_time').html(''+t+':00 <span class="caret"></span>');
}
function setScheduleStatus(status,gname){
	scheduledStatus = status;
	var st;
	if(status === -1) st = 'btn btn-danger';
	else if(status === 0) st = 'btn btn-warning';
	else st = 'btn btn-success';
	$('#'+gname+'_schedule_status').attr('class',st);
}

function getStatusAt(day, hour, success) {
	requestInfo('get', 'user/schedule', {
		day: day,
		hour: hour
	}, success);
}
function SCHEDULESTATUS(groupName){

	if(groupName == 'friend')
	{
		setStatusAt(scheduledStatus, "Status scheduled by GoLight", weekday, time, reportChange(groupName));
	}
	else
	{
		scheduleStatusInGroup(groupName,scheduledStatus, "Status scheduled by GoLight", weekday, time, reportChange(groupName));
	}
}
function reportChange(groupName){
	var responseElement = document.getElementById("scheduleResponse"+groupName);
	console.log(groupName);
	responseElement.innerHTML = "<h4>Status scheduled!</h4>";
	alert(response);
}
function setStatusAt(status, blurb, day, hour, success) {
	requestInfo('put', 'user/schedule', {
		day: day,
		hour: hour,
		status: status,
		blurb: blurb
	}, success);
}

function userScheduleInGroup(groupName, day, hour, success) {
	requestInfo('get', 'group/user/schedule', {
		groupName: groupName,
		day: day,
		hour: hour,
	}, success);
}

function scheduleStatusInGroup(groupName, day, hour, status, blurb, success) {
	requestInfo('get', 'group/user/schedule', {
		groupName: groupName,
		day: day,
		hour: hour,
		status: status,
		blurb: blurb,
	}, success);
}

function clearSchedule(success) {
	requestInfo('delete', 'user/schedule', {}, success);
}

function clearScheduleInGroup(groupName, success) {
	requestInfo('delete', 'group/user/schedule', {groupName: groupName}, success);
}

function getGroupSchedule(groupName, day, hour, success) {
	requestInfo('get', 'group/schedule', {
		groupName: groupName,
		day: day,
		hour: hour
	}, success);
}