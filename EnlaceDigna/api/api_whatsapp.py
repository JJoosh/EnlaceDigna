from rest_framework.response import Response
import requests


def getURL():
    url = "https://graph.facebook.com/v19.0/243693825501955/messages"
    return url


def getToken():
    access_token = "EABPlBU5h77QBOZBW8A6WzXIZCDscLr5jdtph8bEetNMUFLfRBJ1MANPxZBZB9WM0z3iojbYcy6k0z4BAF9lwnAmjvi6C8S6dildlSafuqy2V7jrcJjQNhZBZAA4ZAMwPE6vgzNcCU4py71sMbpiahKMYp7fYLCUZBKOjyep2gbnVTFsxJqUySGAqEhj7MrT4D73QPOujZCNlO0tKfQB8y5y8ZD"
    return access_token



def enviarMessage_errorToken(telefono):
    print(telefono)
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": telefono,
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


def enviar_img(telefono, urls):
    for url in urls:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": telefono,
            "type": "image",
            "image": {
                "link": url
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
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": telefono,
            "type": "video",
            "video": {
                "link": url
            }
        }
        headers = {
            "Authorization": f"Bearer {getToken()}",
            "Content-Type": "application/json"
        }
        response = requests.post(getURL(), headers=headers, json=data)

        if response.status_code != 200:
            print(f'Error al enviar el video desde {url}: {response.text}')
            

    return Response({"message": "Todos los videos fueron enviados correctamente"})


def enviar_mensaje(telefono, nombre, apellido):
    print(telefono)

    #AQUI ENVIARA EL MENSAJE PRINCIPAL QUE INICIARA EL ENVIO DE RESULTADOS
    data={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": telefono,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "Hola " + nombre +" " +apellido+ " estos son los resultados de tu ultrasonido"
        }
    }
    headers = {
        "Authorization": f"Bearer {getToken()}",
        "Content-Type": "application/json"
    }
    response = requests.post(getURL(), headers=headers, json=data)
    urlsi=['https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/Screenshot-6.png', 'https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/WhatsApp+Image+2024-03-25+at+6.05.53+PM.jpeg', 'https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/abrahamfake.jpeg']
    urlsv=['https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/ace-mlgfsgw2-ldku4o1d_UD3b6KYh+(1).mp4']
    enviar_videos(telefono, urlsv )
    enviar_img(telefono, urlsi)
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
            "name": "pedir_confirmacion",
            "language": {
                "code": "es_MX",
                "policy": "deterministic"
            },
            "components":[{
                "type": "body",
                "parameters": [
                    {
                    "type": "text",
                    "text": nombre
                    }]
            }]
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
        return Response({"message": "Mensaje enviado correctamente"})
        
    else:
        return Response({"error": f"Error al enviar el mensaje: {response.text}"}, status=response.status_code)