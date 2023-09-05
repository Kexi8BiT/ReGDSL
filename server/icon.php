<?php
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    
    // Формируем URL для запроса к удаленному серверу
    $url = "http://217.18.62.111/userinfo.php?id=" . $id;
    
    // Выполняем GET запрос
    $response = file_get_contents($url);
    
    if ($response !== false) {
        // Декодируем JSON ответ
        $data = json_decode($response, true);
        
        if (is_array($data) && !empty($data)) {
            // Оставляем только нужные параметры
            $filteredData = array(
                "userName" => $data[0]["userName"],
                "playerColor" => $data[0]["playerColor"],
                "playerColor2" => $data[0]["playerColor2"],
                "iconType" => $data[0]["iconType"],
                "accIcon" => $data[0]["accIcon"],
                "accShip" => $data[0]["accShip"],
                "accBall" => $data[0]["accBall"],
                "accBird" => $data[0]["accBird"],
                "accDart" => $data[0]["accDart"],
                "accRobot" => $data[0]["accRobot"],
                "accSpider" => $data[0]["accSpider"]
            );
            
            // Выводим отфильтрованные данные в формате JSON
            header('Content-Type: application/json');
            echo json_encode($filteredData);
        } else {
            echo "Invalid response data format.";
        }
    } else {
        echo "Failed to fetch data from the remote server.";
    }
} else {
    echo "Missing 'id' parameter.";
}
?>
