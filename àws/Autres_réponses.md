• Expliquer le rôle de lambda_handler

   Lambda handler a pour rôle : de recevoir les données d’entrée (event), d' accéder
   au contexte d’exécution (context), de traiter la logique du programme et de
   retourner une réponse.


• montrer un exemple d’événement JSON de test.

  Exemple :

                 {
  "nom": "Jeff"
}



• montrer le résultat attendu.

   résultats attendu : 


            {
  "statusCode": 200,
  "body": "Bonjour Jeff, bienvenue dans AWS Lambda"
}


expliquer brièvement dans quels cas une fonction Lambda est utile.

   Une fonction Lambda est utile en ce que : Applications sans serveur c'est-à-dire
   pas besoin de gérer un serveur, AWS exécute le code automatiquement. Créer
   des petites fonctions indépendantes. Et il y a payement seulement quand la
   fonction s’exécute.


