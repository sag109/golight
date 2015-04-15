var weekday = 0;
var time = 0;
var scheduledStatus = 0;

function setScheduleDay(day){
	weekday = day;
}
function setScheduleTime(t){
	time = t;
}
function setScheduleStatus(status){
	scheduledStatus = status;
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