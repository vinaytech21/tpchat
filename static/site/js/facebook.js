	$( document ).ready(function() {
		$('#logoutBtn').hide();
		$('#userDetails').hide();
	});

	function fbAsyncInit() {
		FB.init({
			appId      : '1636596989926220',
			status     : true, // check login status
			cookie     : true, // enable cookies to allow the server to access the session
			xfbml      : true  // parse XFBML
		});
	}
	function logIn() {
	  	FB.login(
	        function(response) {
				if (response.status== 'connected') {
					FB.api('/me', function(response) {
				    	console.log(response);
				      	console.log('Good to see you, ' + response.name + '.');
				      	$('#loginBtn').hide();
				      	$('#logoutBtn').show();
						$('#userDetails').show();
						$('#userInfo').html(response.name + '<br>' + response.location.name);
				    });

				    FB.api("/me/picture?width=200&redirect=0&type=normal&height=200", function (response) {
				      	if (response && !response.error) {
				        	/* handle the result */
				        	console.log('PIC ::', response);
				        	$('#userPic').attr('src', response.data.url);
				      	}
				    });
				}
			}
		);
	}

	function logOut() {
		FB.logout(function(response) {
			console.log('logout :: ', response);
			//Removing access token form localStorage.
			$('#loginBtn').show();
			$('#logoutBtn').hide();
			$('#userDetails').hide();
		});
	}

	fbAsyncInit();
	  

