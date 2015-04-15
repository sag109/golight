var allNonFriendUsers;
var allGroups;
var globalGroupName;

$(document).ready(function() {
    //get friends and groups
    getFriends();
        getGroups();
    setInterval(function () {
        getFriends();
        getGroups();
    }, 60000);

});

function listAll(){
    var resultsElement = document.getElementById("searchResults");
    var fillFromFriends = fill();
    var fillFromGroup = fillGroups();
    resultsElement.innerHTML = "<div class=\"col-lg-6\">"+
    "<div class=\"panel panel-default\">"+
    "<!-- Default panel contents -->"+
    "<div class=\"panel-heading\">Friends</div>"+

    "<!-- Table -->"+
    "<table class=\"table table\">"+
    fillFromFriends+
    "</table>"+
    "</div><br>"+
    "</div><div class=\"col-lg-6\">"+
    "<div class=\"panel panel-default\">"+
    "<!-- Default panel contents -->"+
    "<div class=\"panel-heading\">Groups - click a group to join</div>"+

    "<!-- Table -->"+
    "<table class=\"table table\">"+
    fillFromGroup+
    "</table>"+
    "</div>"+
    "</div>";
    
}
function getFriends(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4) {
        allNonFriendUsers = JSON.parse(xmlHttp.responseText);
    }
}

    xmlHttp.open("GET", "/search/friends", true); // true is for async communication
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send();
    //console.log("getFriends");

}

function getGroups(){

    console.log('getting groups...');
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4) {
        allGroups = JSON.parse(xmlHttp.responseText);
        console.log('allGroups is '+allGroups);
    }
}

    xmlHttp.open("GET", "/search/groups", true); // true is for async communication
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send();
    //console.log("getGroups");
}
function fill(){
    var count=0;
    var resultsElement = document.getElementById("searchResults");
    var searchText = document.getElementById("searchText").value;
    var noText = false;
    if(!searchText)
        noText = true;
    else
        searchText = searchText.toLowerCase()

    var fillString="";

if( typeof(allNonFriendUsers) !== 'undefined') {
    for(var i=0; i<allNonFriendUsers.length; i++){
        //console.log(info[i].email.indexOf());
        var email = allNonFriendUsers[i].email.toLowerCase();
        var name = allNonFriendUsers[i].name.toLowerCase();
        //console.log("email is "+email);
        //console.log("name is "+name);
        //console.log("searchText is "+searchText);
        if(count>10)
        {
            break;
        }
        if((email.indexOf(searchText)>-1) || (name.indexOf(searchText)>-1)|| noText)
        {
            count++;
            fillString += "<div><div><span class=\"glyphicon glyphicon-user\" ";
            fillString += "aria-hidden=\"true\"></span>&nbsp&nbsp<span id='"+allNonFriendUsers[i].email+"' onclick='addSearchedFriend(this);' class=\"group-name-hover\">";
            fillString += allNonFriendUsers[i].name+"</div><div id='"+allNonFriendUsers[i].email+"-response'></span></div></div>";//should only be one type of data        
            
        }
    }
}
    //fillString+= "</ul>";
    return fillString;

    //console.log("why no work? "+ fillString);
    //resultsElement.innerHTML = fillString;
}

function fillGroups(){
    var count = 0;
    var resultsElement = document.getElementById("searchResults");
    var searchText = document.getElementById("searchText").value;
    var noText = false;
    if(!searchText)
        noText = true;
    else
        searchText = searchText.toLowerCase();
    var fillString = "";
    if(typeof(allGroups) !== 'undefined') {
        for(var i=0; i<allGroups.length; i++){
            if(count>10)
            {
                break;
            }
            if(allGroups[i].name.toLowerCase().indexOf(searchText)>-1 || noText)
            {
                count++;
                fillString += "<div class=\"row\"><div class=\"col-lg-5\"><span class=\"glyphicon glyphicon-th-list\" aria-hidden=\"true\"></span>&nbsp&nbsp";
                fillString += "<span class=\"group-name-hover\" id=\"group"+i+"\" onclick=\"joinGroupBar(this)\">"+allGroups[i].name+"</span></div><div class=\"col-lg-5\">"+allGroups[i].blurb;
            	fillString += "</div><br><div class=\"col-lg-6\" id=\""+allGroups[i].name+"\"></div></div><br>";//should only be one type of data        

            }
        }
        //console.log("on "+ info[i].email);
    }
    //fillString+= "</ul>";
    return fillString;
    //console.log("why no work? "+ fillString);
    //resultsElement.innerHTML = fillString;
}

function joinGroupBar(groupElement){

    var count =0;
    var groupName = groupElement.innerHTML;
    var joinElement = document.getElementById(groupName);
    //globalGroupName = groupName;
    var searchText = document.getElementById("searchText").value;
    var noText = false;
    if(!searchText)
        noText = true;
    else
        searchText = searchText.toLowerCase();
    
    for(var i = 0; i<allGroups.length; i++)
    {
        if(count>10)
        {
            break;
        }
        if(allGroups[i].name.toLowerCase().indexOf(searchText)>-1 || noText)
        {
            document.getElementById(allGroups[i].name).innerHTML= "";
            count++;
        }
    }
    var barText = "<span class=\"col-lg-12\"><span class=\"input-group\"><input type=\"text\" id=\"join_blurb\" class=\"form-control\" placeholder=\"Set blurb in group\" aria-describedby=\"basic-addon1\">";
        barText += "<span class=\"input-group-btn\"><button onclick=\"joinGroupWithBlurb(&quot ";
        barText += groupName+"&quot);\" class=\"btn btn-default\" type=\"button\">Join</button></span></span></span>";
    joinElement.innerHTML =barText;

    console.log(barText);
}

function joinGroupWithBlurb(groupName){
    console.log("called joinGroupWithBlurb");
    var name = groupName.substring(1);
    console.log("name is "+name);
    var status =0;//doesn't matter anyway
    var blurb = document.getElementById("join_blurb").value;
    console.log("blurb is "+blurb);
    console.log(document.getElementById("join_blurb").innerHTML);
    if(!!blurb)
    {
        console.log("why nnot making request");
        var info = {"groupName":name,"status":status,"blurb":blurb};
        var createGroup = requestInfo('post','group/user',info, function(response) {
            if(response.success === false){
                //document.getElementById('message').innerHTML = response.error;
                
                var neat = document.getElementById(name);
                
                neat.innerHTML = response.error;
            }
            else
            {
                console.log("successfullll");

                var neat = document.getElementById(name);
                
                neat.innerHTML = "Joined";
                // document.getElementById('message').innerHTML = "You joined the group!";
            }
            
        }); 
    }
    else
        document.getElementById(name).innerHTML= "Enter a blurb first";
}

function addSearchedFriend(friendElement){

    console.log("adding friends");
    var friendEmail = friendElement.id;
    var info = {"email":friendEmail};
    var putUser = requestInfo('post','friend',info, function(response) {
        var responseElement = document.getElementById(friendEmail+"-response");
        if(response.success === false){
            //document.getElementById('message').innerHTML = response.error;
            responseElement.innerHTML=response.error;
            console.log(response.error);
        }
        else{
            responseElement.innerHTML="Friend added";
            console.log("successful");
            //document.getElementById('message').innerHTML = "";
        }
    }); 
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

