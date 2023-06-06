<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <?php
    // Check if the form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve the entered username and password
        $username = $_POST["username"];
        $password = $_POST["password"];

        // Check if the credentials are correct
        if ($username == "test" && $password == "test") {
            // Display success message
            echo "<h2>Success: Welcome back $username!</h2>";
        } else {
            // Display error message
            echo "<h2>Error: Invalid username and password!</h2>";
        }
    }
    ?>
    <form method="POST" action="<?php echo $_SERVER["PHP_SELF"]; ?>">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
