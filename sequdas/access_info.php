<?php 
    require_once 'users/init.php';    
    function get_density($folder) {
        $path = '/sequdas_result_dir/'.$folder.'/'.$folder.'_density.txt';
        if (file_exists($path)){
             $lines = file($path);
             $my_arr = array();
                foreach ($lines as $line_num => $line) {
                    array_push($my_arr, $line);
                }
            return $my_arr;
        }
        else{
            $my_arr = array();
            array_push($my_arr, "N/A");
            return $my_arr;
        }
    }
	$arrVal = array();
	$db = DB::getInstance(); 
	$sql='SELECT * FROM status_table';
	$query_miseq = $db->query($sql);
	$djresults=$query_miseq->results();
	$i=1;
	foreach ($djresults as $qq) {
     	$name = array(
                        'num' => $i,
                        'bccdc_id'=>$qq->bccdc_id,
                        'source'=> $qq->source,
                        'folder'=> $qq->folder,
                        'start_time'=> $qq->start_time,
                        'end_time'=> $qq->end_time,
                        'status'=> $qq->status,
                        'sample'=> $qq->sample,
                        'density' => get_density($qq->folder)
                    );      


   		array_push($arrVal, $name); 
		$i++;   
	}
    echo  json_encode($arrVal);	
?>   


