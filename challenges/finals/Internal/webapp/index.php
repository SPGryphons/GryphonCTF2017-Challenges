<html>
	<form action="login.php" method=post>
	<input type="text" name="username" placeholder="Username"><br>
	<input type="password" name="password" placeholder="Password"><br>
	<input type="submit" name="submit" value="Submit">
	</form>
</html>
<?php
	if($_GET['status']=="fail") {
		echo "<script>window.alert('Invalid Credntials');</script>";
	} else if($_GET['status']=="noauth") {
		echo "<script>window.alert('Please Login');</script>";
	}
?>