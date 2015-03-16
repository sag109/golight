function putGroup(){
    //alert('got here');
    var groupNameIn = document.getElementById('put_group_name');
    //alert('did something');
    if(groupNameIn){
        var groupName = groupNameIn.value;
        var blurb = document.getElementById('put_blurb').value;
       // alert('groupName is ' + escape(groupName));
        var xmlHttp = createXmlHttp();
        xmlHttp.onreadystatechange = function() {
            if(xmlHttp.readyState==4 && xmlHttp.status==200){
                document.getElementById('put_group_name').value=""; 
                document.getElementById('put_blurb').value="";
                alert(xmlHttp.responseText);
           //     alert("I state changed");
            }
            else if(request.readyState==4){
                alert("something went wrong");
            }
        };
        
        var paramString = 'submit_type=Update&group_name=' + escape(groupName);
        paramString = paramString + '&blurb=' +escape(blurb);
        //send all parameters
        xmlHttp.open("POST", '/group', true); // true is for async communication
        
        xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlHttp.send(paramString);
     //   alert("doing stuff here now?");
    }
}

function addGroup(){
    //alert('got here');
    var groupNameIn = document.getElementById('add_group_name');
    //alert('did something');
    if(groupNameIn){
        var groupName = groupNameIn.value;
        var blurb = document.getElementById('add_blurb').value;
       // alert('groupName is ' + escape(groupName));
        var xmlHttp = createXmlHttp();
        xmlHttp.onreadystatechange = function() {
            if(xmlHttp.readyState==4 && xmlHttp.status==200){
                //check here for the response...
                document.getElementById('add_group_name').value="";
                document.getElementById('add_blurb').value=""; 
                alert(xmlHttp.responseText);
           //     alert("I state changed");
            }
            else if(request.readyState==4){
                alert("something went wrong");
            }
        };
        
        var paramString = 'submit_type=Add&group_name=' + escape(groupName);
        paramString = paramString + '&blurb=' +escape(blurb);
        //send all parameters
        xmlHttp.open("POST", '/group', true); // true is for async communication
        
        xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlHttp.send(paramString);
     //   alert("doing stuff here now?");
    }
}

function deleteGroup(){
    //alert('got here');
    var groupNameIn = document.getElementById('delete_group_name');
    //alert('did something');
    if(groupNameIn){
        var groupName = groupNameIn.value;
        var blurb = document.getElementById('delete_blurb').value;
       // alert('groupName is ' + escape(groupName));
        var xmlHttp = createXmlHttp();
        xmlHttp.onreadystatechange = function() {
            if(xmlHttp.readyState==4 && xmlHttp.status==200){
                document.getElementById('delete_group_name').value="";
                document.getElementById('delete_blurb').value=""; 
                alert(xmlHttp.responseText);
           //     alert("I state changed");
            }
            else if(request.readyState==4){
                alert("something went wrong");
            }
        };
        
        var paramString = 'submit_type=Delete&group_name=' + escape(groupName);
        paramString = paramString + '&blurb=' +escape(blurb);
        //send all parameters
        xmlHttp.open("POST", '/group', true); // true is for async communication
        
        xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlHttp.send(paramString);
     //   alert("doing stuff here now?");
    }
}
function createXmlHttp() {
  var xmlhttp;
  if (window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
  } else {
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
  }
  if (!(xmlhttp)) {
    alert("Your browser does not support AJAX!");
  }
  return xmlhttp;
}
