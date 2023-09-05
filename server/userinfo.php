<?php
function mapKey($key) {
    $keyMap = [
        '1'  => 'userName',
        '2'  => 'userID',
        '3'  => 'stars',
        '4'  => 'demons',
        '6'  => 'ranking',
        '7'  => 'accountHighlight',
        '8'  => 'creatorpoints',
        '9'  => 'iconID',
        '10' => 'playerColor',
        '11' => 'playerColor2',
        '13' => 'secretCoins',
        '14' => 'iconType',
        '15' => 'special',
        '16' => 'accountID',
        '17' => 'usercoins',
        '18' => 'messageState',
        '19' => 'friendsState',
        '20' => 'youTube',
        '21' => 'accIcon',
        '22' => 'accShip',
        '23' => 'accBall',
        '24' => 'accBird',
        '25' => 'accDart',
        '26' => 'accRobot',
        '27' => 'accStreak',
        '28' => 'accGlow',
        '29' => 'isRegistered',
        '30' => 'globalRank',
        '31' => 'friendstate',
        '38' => 'messages',
        '39' => 'friendRequests',
        '40' => 'newFriends',
        '41' => 'NewFriendRequest',
        '42' => 'age',
        '43' => 'accSpider',
        '44' => 'twitter',
        '45' => 'twitch',
        '46' => 'diamonds',
        '48' => 'accExplosion',
        '49' => 'modlevel',
        '50' => 'commentHistoryState'
    ];

    return $keyMap[$key] ?? $key;
}

function robtop_data_parser2($data, $top = null) {
    $total = [];
    $segments = explode('|', $data);

    foreach ($segments as $segment) {
        $keyValuePairs = explode(':', $segment);
        $segmentData = [];
        for ($i = 0; $i < count($keyValuePairs); $i += 2) {
            $key = mapKey($keyValuePairs[$i]);
            $value = $keyValuePairs[$i + 1];
            $segmentData[$key] = $value;
        }
        $total[] = $segmentData;
    }

    if ($top !== null) {
        $total = array_slice($total, 0, $top);
    }

    return $total;
}


$url = "http://rugd.gofruit.space/00kz/db/getGJUserInfo20.php";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "Accept: application/json",
   "Content-Type: application/x-www-form-urlencoded",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);


$id = isset($_GET['id']) ? intval($_GET['id']) : null;


$resp = "accountID=$id&targetAccountID=$id";

curl_setopt($curl, CURLOPT_POSTFIELDS, $resp);

//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$data = curl_exec($curl);

if (curl_errno($ch)) {
    echo json_encode(["error" => "cURL Error: " . curl_error($ch)]);
} else {
    if ($data !== false) {
        $parsedData = robtop_data_parser2($data, $topCount);
        echo json_encode($parsedData);
    } else {
        echo json_encode(["error" => "Failed to fetch data from the URL."]);
    }
}

curl_close($ch);
?>

