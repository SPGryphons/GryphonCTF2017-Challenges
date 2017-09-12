<?php
if($_POST["submit"] == "Submit") {
	$varQuantity = $_POST["quantity"];
	$message = "broken";
	if($varQuantity == 20) {
		$message="GCTF{T1m3_t0_up53ll_on_c4r0us311_h3h3h3}";
	} else {
		$message="You have purchased ".$varQuantity." tickets";
	}
	echo $message;
}
?>