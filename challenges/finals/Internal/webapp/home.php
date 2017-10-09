<?php
	session_start();
	if (isset($_SESSION['user'])) {
		echo "Welcome," . $_SESSION['user'];
	} else {
		header("Location: index.php?status=noauth");
	}
?>

<h1>Expect the flag to be here?</h1>
<h1>Well, this page is not done cos I have a test later :)</h1>
<h2>Apologies for any inconvinence caused</h2>
<footer>Copyright @exetr & @void 2017 <br> <a href="ftp.php?file=tnc.txt">Terms & Conditions</a> apply </footer>
