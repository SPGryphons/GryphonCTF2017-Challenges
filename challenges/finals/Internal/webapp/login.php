<?php
	/*get variables*/
	$username = $_POST['username'];
	$password = $_POST['password'];
	
	/*database stuff*/
	$db = new SQLite3("./webapp.db");

	$sql = "SELECT * FROM users where username = '" . $username . "' and password = '" . $password . "' ";

	$results = $db->query($sql);
	$rowCtr = 0;
	while($row = $results->fetchArray(SQLITE3_NUM) ) {
		$rowCtr++;
	}

	session_start();
	if ($rowCtr != 0) {
		$_SESSION["user"] = $username;
		header("Location: home.php");
	} else {
		header("Location: index.php?status=fail");
	}

?>