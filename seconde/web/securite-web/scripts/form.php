<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="custom.css">
  </head>
  <body>
    <div id="conteneur">
    <h1>Bienvenue <?php echo htmlspecialchars($_POST['name']);?></h1>
    <p>Ce site ne semble pas très sécurisé!</p>
    </div>
  </body>
</html>
