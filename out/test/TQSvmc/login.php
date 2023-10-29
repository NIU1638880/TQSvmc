<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    if ($username === "" || $password === "") {
        echo "Por favor, rellena todos los campos.<br>";
        echo '<form action="../vista/Login.html" style="display: inline;"><button type="submit">Volver al formulario de inicio de sesión</button></form>';
        exit();
    }
    $file = fopen('../model/usuarios.csv', 'r');
    $userExists = false;
    while (($data = fgetcsv($file)) !== false) {
        if ($data[0] === $username && $data[1] === $password) {
            $userExists = true;
            break;
        }
    }
    fclose($file);
    if ($userExists) {
        echo "Inicio de sesión exitoso. <br>";
        echo "Nombre de usuario: " . $username . "<br>";
        echo "Contraseña: " . $password . "<br>";
        echo "Redireccionando a la página principal en 3 segundos... <br>";
        echo '<script>setTimeout(function(){ window.location.href = "../vista/main_menu.html"; }, 3000);</script>';
    } else {
        echo "El usuario no existe o la contraseña es incorrecta. Por favor, vuelve a intentarlo.<br>";
        echo '<form action="../vista/Login.html" style="display: inline;"><button type="submit">Volver al formulario de inicio de sesión</button></form>';
    }
}
?>