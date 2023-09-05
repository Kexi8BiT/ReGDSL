<?php
// Создаем ассоциативный массив с данными
$data = array(
    "avatar" => "https://cdn.discordapp.com/attachments/1079603737506611270/1145705706876579850/browser_8PcJHbbiRb.gif",
    "description" => "Доступности на win7 не будет, кто на ней вообще сидит?",
    "topic" => "Я пошутил"
);

// Устанавливаем заголовок ответа как JSON
header('Content-Type: application/json');

// Преобразуем массив в JSON и выводим его
echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
