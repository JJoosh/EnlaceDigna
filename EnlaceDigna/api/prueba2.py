import requests
import json

# Define los parámetros de la solicitud
url = "https://graph.facebook.com/v18.0/243693825501955/messages"
access_token = "EABPlBU5h77QBO1IvYQlZCmj1ubv5AcZA5iCcT3iLq3wm61sPTChqbfaIOvIjpoVbmjZC5AxZBqTUNGnAMuQP18JfeCRWVM2vEVPJEnkrvu2wZB1RXQuwceRzYozs0JRd7x7vuTYXXM4YXoR3PHDJqyt0Wkb0rpJXmVUn1O8vAxc49tJgyFYc31CbGPwuyPn4SZAynbKzJN36HSVQoWOZCYZD"
from_phone_number_id = "243693825501955"  # Reemplaza con tu ID de número de teléfono
recipient_wa_id = "+529991723856"  # Reemplaza con el ID de WhatsApp del destinatario


data = {
    

  "messaging_product": "whatsapp",
  "to": "529991723856",
  "type": "template",
  "template": {
    "name": "enviar_info",
    "language": {
      "code": "es_MX"
    },
    "components": [
      {
        "type": "header",
        "parameters": [
          {
            
            "type": "image",
            "image": {
              "link": "https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/Screenshot-8.png"
            }
          }
        ]
      },
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": "Arturo"
          }
        ]
      }
    ]
  }



}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
