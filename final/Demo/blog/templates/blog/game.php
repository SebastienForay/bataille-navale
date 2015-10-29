<!DOCTYPE html>
<head>
	<title>Bataille navale</title>
	<meta charset="UTF-8"/>
</head>

<body>
	<h1> Résultat jeu de la bataille navale</h1>

<?php
	echo "allo";
	if(isset($_GET['game']){

		$string = file_get_contents("/games/game_" + $_GET['game'] + ".json");
		$json_a = json_decode($string, true);

		echo $json_a['myName'];
		echo $json_a['gameNbr'];
	}
?>

</body>