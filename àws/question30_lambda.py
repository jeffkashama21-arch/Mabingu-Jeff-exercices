# Fonction lambda

def lambda_handler(event, context):
  
    nom = event.get("nom", "utilisateur")

    message = f"Bonjour {nom}, bienvenue dans AWS Lambda"

    return {
        "statusCode": 200,
        "body": message
    }


# • montrer un exemple d’événement JSON de test


{
  "nom": "Jeff"
}




# • montrer le résultat attendu


{
  "statusCode": 200,
  "body": "Bonjour Jeff, bienvenue dans AWS Lambda"
}
