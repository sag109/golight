$(document).ready(function() {
    showPage();
});

function showPage(){
    if(mainView === 'Your Friends'){
        var userInfo = requestInfo('get','user', {}, function(userInfo){
            showStatus(userInfo.status,userInfo.blurb);
        });
    }
    else {
       var userInfo = requestInfo('get','group/user', {}, function(userInfo){
            showStatus(userInfo.status,userInfo.blurb);
        }); 
    }
}

function showStatus(st,bl){
    var cls = getStatusClass(st);
    $('#status_dropdown').attr('class',cls);
    $('#user_blurb').attr('placeholder',bl);
}

function setGlobalStatus(st,bl) {
    console.log("trying put/user");
    if(bl === "" || bl.length > 50) bl = " "; //needs to happen in the server.. doesnt it?

    var info = {status:st,blurb:bl}; //make info 
    var putUser = requestInfo('put','user',info, function(userInfo){ //put info
        console.log("success: "+userInfo.success);
        console.log("error : "+userInfo.error);
        $('#user_blurb').attr('placeholder', bl);
        $('#user_blurb').html('');
    });
}

function setGroupStatus(st,bl) {
    console.log("trying put/group_user");
    if(bl === "" || bl.length > 50) bl = " "; //needs to happen in the server.. doesn't it?
    var info = {status:parseInt(st),blurb:bl,groupName:mainView}; //make info 
    var putUser = requestInfo('put','group/user',info, function(userInfo){ //put info
        console.log("success: "+userInfo.success);
        console.log("error : "+userInfo.error);
        $('#user_blurb').attr('placeholder', bl);
        $('#user_blurb').html('');
    });
}

//returns status of current page as -1,0, or 1 
function getStatus(){
    var status = $('#status_dropdown').attr('class');
    if(status === 'btn btn-success') return 1;
    else if(status === 'btn btn-warning') return 0;
    else return -1;
}

function getStatusClass(st){
    if(st == 1) return 'btn btn-success';
    else if(st == 0) return 'btn btn-warning';
    else return 'btn btn-danger';
}

function changeBlurb(){
    var blurb = $('#user_blurb').val();
    var st = getStatus();
    console.log("blurb to set is "+blurb);

    if(mainView === 'Your Friends')
        setGlobalStatus(st,blurb);
    else
        setGroupStatus(st,blurb);
}

function changeStatus(e) {
    var cls = e.className; //class of button -- color of status that has been selected
    $('#status_dropdown').attr('class',cls); //replace class for dropdown top button
    var st = getStatus();
    var blurb = $('#user_blurb').attr('placeholder');

    if(mainView === 'Your Friends')
        setGlobalStatus(st,blurb);
    else
        setGroupStatus(st,blurb); 
}