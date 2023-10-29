<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $passwordConfirm = $_POST["password-confirm"];

    if ($username === "" || $password === "" || $passwordConfirm === "") {
        echo "Por favor, rellena todos los campos.<br>";
        echo '<form action="../vista/register.html" style="display: inline;"><button type="submit">Volver al formulario de registro</button></form>';
        exit();
    }

    $file = fopen('../model/usuarios.csv', 'r');
    $userExists = false;
    while (($data = fgetcsv($file)) !== false) {
        if ($data[0] === $username) {
            $userExists = true;
            break;
        }
    }
    fclose($file);

    if ($userExists) {
        echo "El usuario ya está registrado. Por favor, elige otro nombre de usuario.<br>";
        echo '<form action="../vista/register.html" style="display: inline;"><button type="submit">Volver al formulario de registro</button></form>';
    } elseif ($password === $passwordConfirm) {
        $data = array($username, $password);
        $file = fopen('../model/usuarios.csv', 'a');
        fputcsv($file, $data);
        fclose($file);
        echo "Registro exitoso. <br>";
        echo "Nombre de usuario: " . $username . "<br>";
        echo "Contraseña: " . $password . "<br>";
        echo "Redireccionando a la página principal en 3 segundos... <br>";
        echo '<script>setTimeout(function(){ window.location.href = "../vista/main_menu.html"; }, 3000);</script>';
    } else {
        echo "Las contraseñas no coinciden. Por favor, vuelve a intentarlo.<br>";
        echo '<form action="../vista/register.html" style="display: inline;"><button type="submit">Volver al formulario de registro</button></form>';
    }
}
?>
