from rest_framework.response import Response
import requests


def getURL():
    url = "https://graph.facebook.com/v19.0/243693825501955/messages"
    return url


def getToken():
    access_token = "EABPlBU5h77QBO2pRFScsPtMcaDR8zqvHaRPxmM0mvztmNcjAXTO0BvjNLFrbwZCNDd3gGLR8W0gZA2csWL5byget9hI2WrqBZCJzpRBIH4SbIrdSNDOH50uUWPQiaG6OsopRs5feMoSrTSC0iex8Ecto0qQLM9V11uvfTxBFkM9cnrInZAOZCrMfPUkH5vM6K"
    return access_token



def enviarMessage_errorToken(telefono):
    print(telefono)
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to":  telefono,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "Hubo un error al procesar su token, por favor escribalo de nuevo, recuerda que este chat solo recibe tokens validos!"
        }
    }
    headers = {
        "Authorization": f"Bearer {getToken()}",
        "Content-Type": "application/json"
    }
    response = requests.post(getURL(), headers=headers, json=data)

    if response.status_code == 200:
        print('Mensaje enviado correctamente')
    else:
        print('Error al enviar el mensaje:', response.text)

    return Response({"message": "Mensaje enviado correctamente" if response.status_code == 200 else f"Error al enviar el mensaje: {response.text}"})


def enviar_img(telefono, urls, nombre, fecha):
    for url in urls:
        print('enviando url: ' ,url)
        data = {
        "messaging_product": "whatsapp",
  "to": telefono,
  "type": "template",
  "template": {
    "name": "envio_resultados",
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
              "link": url
            }
          }
        ]
      },
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": nombre
          },
          {
              "type": "text",
              "text": fecha
          }
        ]
      },
      
    ]
  }
        

        }
        
        headers = {
            "Authorization": f"Bearer {getToken()}",
            "Content-Type": "application/json"
        }
        response = requests.post(getURL(), headers=headers, json=data)

        if response.status_code != 200:
            print(f'Error al enviar la imagen desde {url}: {response.text}')
            

    return Response({"message": "Todas las imágenes fueron enviadas correctamente"})




def enviar_videos(telefono, urls):
    for url in urls:
        print('enviar_videos:', url)
        data = {
        "messaging_product": "whatsapp",
  "to": "telefono",
  "type": "template",
  "template": {
    "name": "",
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
              "link": "https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/token_ticket.jpeg"
            }
          }
        ]
      },
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": "nombre"
          }
        ]
      },
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": "fecha"
          }
        ]
      }
    ]
  }

    }

        headers = {
            "Authorization": f"Bearer {getToken()}",
            "Content-Type": "application/json"
        }
        response = requests.post(getURL(), headers=headers, json=data)

        if response.status_code != 200:
            print(f'Error al enviar el video desde {url}: {response.text}')
        else:
            print('bien video')    

    return Response({"message": "Todos los videos fueron enviados correctamente"})


def enviar_mensaje(telefono, nombre, apellido, urlsv, urlsi, tipoultra, fecha):
    print(telefono)

    #AQUI ENVIARA EL MENSAJE PRINCIPAL QUE INICIARA EL ENVIO DE RESULTADOS
    data={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": telefono,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "Hola " + nombre +" " +apellido+ ", en los siguientes minutos estaran llegando los resultados de ultrasonido"
        }
    }
    headers = {
        "Authorization": f"Bearer {getToken()}",
        "Content-Type": "application/json"
    }
    response = requests.post(getURL(), headers=headers, json=data)
    
    enviar_videos(telefono, urlsv )
    enviar_img(telefono, urlsi, tipoultra, fecha)
    if response.status_code == 200:
        print('bien')
        return Response({"message": "Mensaje enviado correctamente"})
    else:
        print('Mal')

        return Response({"error": f"Error al enviar el mensaje: {response.text}"}, status=response.status_code)


    



def message_pedirToken(telefono, nombre):
    # Define los datos del cuerpo de la solicitud
    data = {
        "messaging_product": "whatsapp",
  "to": telefono,
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
              "link": "https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/token_ticket.jpeg"
            }
          }
        ]
      },
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": nombre
          }
        ]
      }
    ]
  }

    }

    # Define los encabezados de la solicitud
    headers = {
        "Authorization": f"Bearer {getToken()}",
        "Content-Type": "application/json"
    }

    
    response = requests.post(getURL(), headers=headers, json=data)

    # Maneja la respuesta de requests y devuelve una respuesta adecuada para Django REST Framework
    if response.status_code == 200:
        print('Se envio el mensaje')
        
    else:
        print(response.status_code)