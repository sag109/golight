	$(document).ready(function() {
            var userInfo = requestInfo('get','user', {}, function(userInfo){
                $('#username').html("Your username: "+userInfo.name);
            }); 
        });

        function editUsername() {
            var newName = $('#new_username').val();
            var response = requestInfo('put','user',{'name':newName}, function(response){
                $('#username').html("Your username: "+newName);
                console.log(response.error);	
            })
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
