<?php
	$file = $_GET["file"];

	if (substr($file, -4) == '.txt') {
		
		$path = "/var/www/html/ftp/";
		//chech for possibilities of null bytes
		$pos1 = strpos($file, "\\0");
		$pos2 = strpos($file, chr(0));
		$pos3 = strpos($file, "%0");
		if ($pos1 !== false) {
			$path .= substr($file, 0, $pos1);
		} else if ($pos2 !== false) {
			$path .= substr($file, 0, $pos2);
		} else if ($pos3 !== false) {
			$path .= substr($file, 0, $pos3);
		} else {
			$path .= $file;
		}

		echo $path;

		include($path);

	} else {
?>
	<h1>ERROR!: Only .txt files are allowed</h1>
<?php
	}
?>
