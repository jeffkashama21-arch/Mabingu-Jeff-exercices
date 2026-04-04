def lambda_handler(event, context):
  
    nom = event.get("nom", "utilisateur")

    message = f"Bonjour {nom}, bienvenue dans AWS Lambda"

    return {
        "statusCode": 200,
        "body": message
    }
