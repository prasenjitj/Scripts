<?php
header('Content-Type: text/html; charset=UTF-8');
$file ="";
if ($_FILES["file1"]) {
	
	if (($_FILES["file1"]["type"]=="text/csv")||($_FILES["file1"]["type"]=="text/tab-separated-values")) {
		
		$arr = array();
		$check = array();
		$final = array();
		$row = 0;
		$num = 0;
		if (($handle = fopen($_FILES["file1"]["tmp_name"], "r")) !== FALSE) {
		    while (($data = fgetcsv($handle, 1000, "\t")) !== FALSE) {
			$num = count($data);
			$arr[$row] = array();
			for ($c=0; $c < $num; $c++) {
			    //$arr[$row][$c] = $data[$c];
			    $arr[$row][$c] = html_entity_decode($data[$c],ENT_COMPAT|ENT_HTML401,'UTF-8');
			}
			$row++;
		    }
		    fclose($handle);
		}

		$con=mysqli_connect("localhost","root","abc123","Keybag");
		
		// Check connection
		if (mysqli_connect_errno()) {
		  echo "Failed to connect to MySQL: " . mysqli_connect_error();
		}
		


		$keycount = 0;
		$keys = 10; //key to be changed
		$keys_id ="";
		for ($i=1;$i<$row;$i++) {
			$search = "";
			for($j=0;$j<3;$j++) {
				$search .= " " . $arr[$i][$j];
			}
			$keycount++;
			if($keycount==81) 
				$keycount = 1;
			if($keycount==1) {
				$keys++;

				$result = mysqli_query($con,"SELECT * FROM  `Keys` WHERE `id` = ".$keys);
				while($row121 = mysqli_fetch_array($result)) {
				  $keys_id = $row121['Key'];
				}
				//$keys_id = "AIzaSyBlU4hsYnl6oSvrKw8ZKiTrRmZzBUBANWs";
			}
			$search = "https://www.googleapis.com/customsearch/v1?key=".$keys_id."&cx=009241977094486741223:3agszpaq5sy&prettyPrint=true&q=" . str_replace(" ","+",trim($search));
			//$search = $keys_id;
			$arr[$i][5] = $search;
		}

		
		mysqli_close($con);
		$num++;

		for ($i=1;$i<$row;$i++) {

			$data = file_get_contents ($arr[$i][5]);
			$json = json_decode($data, true);
			$checck = 0;
			foreach ($json as $key => $value) {
				if($key=="items") {
					foreach ($value as $kei => $val) {
						$checck = 0;
						$checkname=0;
						foreach ($val as $keis => $vals) {	
							if($keis=="title"){
								if((preg_match('/^.*('.trim($arr[$i][0]).').*\(/i', $vals))&&(!empty($arr[$i][0]))){
									$checck++;
									$checkname=1;
								} else if($arr[$i][3]){
									$pieces_alias = explode("$#$", $arr[$i][3]);
									for ($kk=0;$kk<count($pieces_alias);$kk++){
										if(preg_match('/^.*('.trim($pieces_alias[$kk]).').*\(/i', $vals)){
											$checck++;
											$checkname=1;
											break;
										}
									}

								}
								if(preg_match('/^.*('.trim($arr[$i][2]).')\)/i', $vals)){
									$checck++;
								}
							} else if ($keis=="link"){
								$arr[$i][6] = $vals;

							} else if ($keis=="snippet") {
								$pieces = explode(",", $arr[$i][1]);
								for ($kk=0;$kk<count($pieces);$kk++){
									if(preg_match('/.*irected by '.trim($pieces[$kk]).'/i', $vals)){	
										if(!empty($pieces[$kk])) {
											$checck++;
											break;
										}
									}
								}
								
//----------------------------------
								if($checkname==0){
									if((preg_match('/.*Also Known As: '.trim($arr[$i][0]).'/i', $vals))&&(!empty($arr[$i][0]))) {
										$checck++;
									} else if($arr[$i][3]){
										$pieces_alias = explode("$#$", $arr[$i][3]);
										for ($kk=0;$kk<count($pieces_alias);$kk++){
											if(preg_match('/.*Also Known As: '.trim($pieces[$kk]).'/i', $vals)){
												$checck++;
												$checkname = 1;
												break;
											}
										}

									}
								}
//==================================

							}
						}
						if($checck!=3) {
							$arr[$i][6] = "";
						} else {
							break;
						}
					}
				}
				if($checck==3) {
					break;
				}
			}
		}
		header('Content-type: text/csv');
		header('Content-Disposition: attachment; filename="id.tsv"');
		for ($i=0;$i<$row;$i++) {
			for($j=0;$j<7;$j++) {
				if ($j==5)
					continue;
				if (($j==6)&&($i==0))
					echo "IMDB URL\t";
				else
					echo $arr[$i][$j]."\t";

			}
			echo "\n";
		}

/*	
		echo "<table border='1'>";
		for ($i=0;$i<$row;$i++) {
			echo "<tr>";
			for($j=0;$j<7;$j++) {
				echo "<td>".$arr[$i][$j]."</td>";

			}
			echo "</tr>";
		}
		echo "</table>";
*/
	}

}
?>
