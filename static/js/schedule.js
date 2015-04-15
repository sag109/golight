function getStatusAt(day, hour, success) {
	requestInfo('get', 'user/schedule', {
		day: day,
		hour: hour
	}, success);
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