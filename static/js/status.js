$(document).ready(function() {
    var userInfo = requestInfo('get','user', {}, function(userInfo){
        setStatus(userInfo.status,userInfo.blurb);
    }); 
});

function setStatus(st,bl) {
    var output = $('#user_blurb').val();
    if(st == -1) $('#output').attr('id', 'btn btn-danger');
    else if(st == 0) $('#output').attr('id', 'btn btn-warning');
    else $('#output').attr('id', 'btn btn-success');
    
    console.log("trying put/user");
    if(bl === "" || bl.length > 50) bl = " "; //needs to happen in the server.. doesnt it?
    var info = {status:st,blurb:bl}; //make info 
    var putUser = requestInfo('put','user',info, function(userInfo){ //put info
        console.log("result: "+userInfo.success);
        console.log("error : "+userInfo.error);
        $('#user_blurb').attr('placeholder', bl);
        $('#user_blurb').html('');
    });
}


function changeBlurb() {
    var blurb = $('#user_blurb').val();
    var st = getStatus();
    console.log("blurb to set is "+blurb);
    setStatus(st,blurb);
}

//returns status as -1,0, or 1 
function getStatus(){
    var status = $('#status_dropdown').attr('class');
    if(status === 'btn btn-success') return 1;
    else if(status === 'btn btn-warning') return 0;
    else return -1;
}

function changeStatus(e) {
    var cls = e.className; //class of button -- color of status that has been selected
    
    $('#status_dropdown').attr('class',cls); //replace class for dropdown top button
    status = e.id;
    var st = 0;
    if(status === 'suc') st = 1;
    else if(status === 'war') st = 0;
    else st = -1;
    var blurb = $('#user_blurb').attr('placeholder');
    
    if(blurb === "" || blurb.length > 50) blurb = " "; //needs to happen in the server.. doesnt it?
    
    setStatus(st,blurb);
}