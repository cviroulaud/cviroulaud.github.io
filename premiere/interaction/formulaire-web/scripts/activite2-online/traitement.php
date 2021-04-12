<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="custom.css">
  </head>
  <body>
    <div id="conteneur">
    <h1>Avec la méthode GET</h1>
    <h2>Bienvenue <?php echo htmlspecialchars($_GET['nom']);?></h2>
    <h1>Avec la méthode POST</h1>
    <h2>Bienvenue <?php echo htmlspecialchars($_POST['nom']);?></h2>
    </div>
  </body>
</html>
