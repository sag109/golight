function showPage(gname){
    if(gname === 'friend'){
        var userInfo = requestInfo('get','user', {}, function(userInfo){
            showStatus(userInfo.status,userInfo.blurb,gname);
        });
    }
    else {
       var userInfo = requestInfo('get','group/user', {'groupName':gname}, function(userInfo){
            showStatus(userInfo.status,userInfo.blurb,gname);
        });
    }
}

function showStatus(st,bl,gname){
    var cls = getStatusClass(st);
    $('#'+gname+'_dropdown').attr('class',cls);
    $('#'+gname+'_blurb').attr('placeholder',bl);
}

function setStatus(st,bl,gname){
    if(bl === "" || bl.length > 50) bl = " "; //needs to happen in the server.. doesn't it?
    if(gname === 'friend'){
        var info = {status:st,blurb:bl}; //make info 
        console.log('trying put/user');
        var putUser = requestInfo('put','user',info, function(userInfo){ //put info
            //console.log("success: "+userInfo.success);
            //console.log("error : "+userInfo.error);
            $('#friend_blurb').attr('placeholder', bl);
            $('#friend_blurb').val('');
            showStatus(st,bl,gname);
        });
    }
    else{
        var info = {status:parseInt(st),blurb:bl,groupName:gname}; //make info 
        var putUser = requestInfo('put','group/user',info, function(userInfo){ //put info
            //console.log("success: "+userInfo.success);
            //console.log("error : "+userInfo.error);
            $('#'+gname+'_blurb').attr('placeholder', bl);
            $('#'+gname+'_blurb').val('');
            showStatus(st,bl,gname);
    });
    }
    
}

//returns status of current page as -1,0, or 1 
function getStatus(groupName){
    var status = $('#'+groupName+'_dropdown').attr('class');
    if(status === 'btn btn-success') return 1;
    else if(status === 'btn btn-warning') return 0;
    else return -1;
}

function getStatusClass(st){
    if(st == 1) return 'btn btn-success';
    else if(st == 0) return 'btn btn-warning';
    else return 'btn btn-danger';
}

function changeBlurb(e,groupName){
    var blurb = $('#'+groupName+'_blurb').val();
    var st = getStatus(groupName);
    console.log("blurb to set is "+blurb);
    setStatus(st,blurb,groupName);
}

function changeStatus(e,groupName) {
    var cls = e.className; //class of button -- color of status that has been selected
    $('#'+groupName+'_dropdown').attr('class',cls); //replace class for dropdown top button
    var st = getStatus(groupName);

    console.log ('st is '+st);
    var blurb = $('#'+groupName+'_blurb').attr('placeholder');
    setStatus(st,blurb,groupName);
}
