$(document).ready(function() {
    var userInfo = requestInfo('get','user', {}, function(userInfo){
        setStatus(userInfo);
    }); 
});

function setStatus(userInfo) {
    var status = userInfo.status;
   // console.log('status is : '+status);
    var blurb = userInfo.blurb;
    var output = document.getElementById('status');
    if(status == -1) output.className = "btn btn-danger";
    else if(status == 0) output.className = "btn btn-warning";
    else output.className = "btn btn-success";
    
    
    console.log("userinfo.status: "+userInfo.status+ " userinfo.blurb: "+userInfo.blurb);
    console.log("status: "+status+" blurb: "+blurb);
    var info = {"status":status,"blurb":blurb};
    var putUser = requestInfo('put','user',info, function(response) {
        console.log(response.error);
    }); 
}

function changeStatus() {
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