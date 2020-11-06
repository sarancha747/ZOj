	$("body").children().each(function () {
   	 $(this).html( $(this).html().replace(/This password is too short. It must contain at least 8 characters./g,"Пароль занадто короткий, він має містити щонайменше 8 символів.") );
});
		$("body").children().each(function () {
   	 $(this).html( $(this).html().replace(/This password is too common./g,"Пароль занадто простий.") );
});
				$("body").children().each(function () {
   	 $(this).html( $(this).html().replace(/This password is entirely numeric./g,"Пароль не має бути повністю числовим.") );
});
							$("body").children().each(function () {
   	 $(this).html( $(this).html().replace(/The password is too similar to the username/g,"Пароль дуже подібний на ім'я користувача.") );
});