<?php

if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $mailFrom = $_POST['email'];
    $message = $_POST['message'];

    $mailTo = "liangalan101@outlook.com";
    $headers = "From: ".$mailFrom;
    $txt = "You have received an e-mail from: ".$name.".\n\n".$message;

    mail($mailTo, $txt, $headers);
    header("Location: q_n_a.html?mailsend");
}
?>