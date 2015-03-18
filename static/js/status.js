$(document).ready(function() {
    var userInfo = requestInfo('get','user', {}, function(userInfo){
        setStatus(userInfo);
    }); 
});

function setStatus(userInfo) {
    //alert('setting status');
    var st = userInfo.status;
   // console.log('status is : '+status);
    var bl = userInfo.blurb;
    var output = document.getElementById('status');
    if(st == -1) output.className = "btn btn-danger";
    else if(st == 0) output.className = "btn btn-warning";
    else output.className = "btn btn-success";
    
    console.log("trying put/user");
    if(bl === "") bl = " ";
    
    var info = {status:st,blurb:bl}; //make info 
    var putUser = requestInfo('put','user',info, function(userInfo){ //put info
        console.log("result: "+userInfo.success);
        console.log("error : "+userInfo.error);
    }); 
    
}

function changeStatus() {
    //alert('changing status');
    var userInfo = requestInfo('get','user', {}, function(userInfo){
        var status = userInfo.status;
        console.log('old status is '+status);
        status = status + 1;
        if(status == 2) status = -1;
        
        userInfo.status = status;
        console.log('new status is '+userInfo.status);
        userInfo.blurb = document.getElementById('user_blurb').value;
        
        setStatus(userInfo);
    });
}