from rest_framework.response import Response
import requests
from .verificaciones import verificarNumeroParaCorreo
from .verificaciones import verificar_DevolverLista
from .verificaciones import ObtenerToken, ObtenerURL_Opcion, separarURL
from ..models import EstadoUsuario

def getURL():
    url = "https://graph.facebook.com/v19.0/243693825501955/messages"
    return url


def getToken():
    access_token = "EABPlBU5h77QBO2pRFScsPtMcaDR8zqvHaRPxmM0mvztmNcjAXTO0BvjNLFrbwZCNDd3gGLR8W0gZA2csWL5byget9hI2WrqBZCJzpRBIH4SbIrdSNDOH50uUWPQiaG6OsopRs5feMoSrTSC0iex8Ecto0qQLM9V11uvfTxBFkM9cnrInZAOZCrMfPUkH5vM6K"
    return access_token

def enviarMessage_errorToken(telefono):
    print(telefono)
    data={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": telefono,
        "type": "text",
        "text": {
            "preview_url": False,
           "body": "Lamentablemente no pude reconocer tu mensaje 😞  Por favor escribe el numero para poder comunicarme contigo:\n"
              +"1-🏥 Recordar comandos y obtener informacion de contacto de Salud Digna.\n"
              +"2-📷 Obtener la url de tu galeria personal.\n"
              +"3-📱 Verificacion para cambiar tu numero de telefono.\n"
              +"4-🔑 Obten tu token unico.\n"
              +"5-📋 Historial para ver tus ultrasonidos en forma de lista.\n"
              

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
            "text": nombre +" 🌟"
          },
          {
              "type": "text",
              "text": fecha + " 📅"
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


def enviar_galeriaResultados(telefono):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": '52'+telefono[2:],
        "type": "text",
        "text": {
            "preview_url": True,
            "body": "Recuerda que puedes ingresar a tu galeria para consultar todos tus resultados anteriores de ultrasonido. 🔍 Ingresa con tu token para acceder a la información. ¡Estoy aquí para ayudarte😊!\nhttps://www.salud-digna.org/"
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
        print('Error al enviar el mensaje galeria:', response.text)

    return Response({"message": "Mensaje enviado correctamente" if response.status_code == 200 else f"Error al enviar el mensaje: {response.text}"})


def enviar_galeria(telefono):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": '52'+telefono,
        "type": "text",
        "text": {
            "preview_url": True,
            "body": "Hola!😊 puedes ingresar a tu galeria para consultar todos tus resultados anteriores de ultrasonido. 🔍 Ingresa con tu token para acceder a la información. ¡Estoy aquí para ayudarte!\nhttps://www.salud-digna.org/"
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
        print('Error al enviar el mensaje galeria:', response.text)

    return Response({"message": "Mensaje enviado correctamente" if response.status_code == 200 else f"Error al enviar el mensaje: {response.text}"})

def enviar_videos(telefono, urls, nombre, fecha):
    for url in urls:
        print(telefono)
        print('enviar_videos:', url)
        data = {
        "messaging_product": "whatsapp",
  "to": telefono,
  "type": "template",
  "template": {
    "name": "envio_resultados_videos",
    "language": {
      "code": "es_MX"
    },
    "components": [
      {
        "type": "header",
        "parameters": [
          {
            "type": "video",
            "video": {
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
            "text": nombre +" 🌟"
          },
          {
              "type": "text",
              "text": fecha + " 📅"
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
            print(f'Error al enviar el video desde {url}: {response.text}')
        else:
            print('bien video')    

    return Response({"message": "Todos los videos fueron enviados correctamente"})


def enviar_mensaje(telefono, nombre, apellido, urlsv, urlsi, tipoultra, fecha):
    print(telefono)

    data={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": telefono,
        "type": "text",
        "text": {
            "preview_url": False,
           "body": "¡Hola " + nombre +" " +apellido+ "! 😊 En los próximos minutos estarán llegando los resultados de ultrasonido. 📩"
        }
    }
    headers = {
        "Authorization": f"Bearer {getToken()}",
        "Content-Type": "application/json"
    }
    response = requests.post(getURL(), headers=headers, json=data)
    
    enviar_videos(telefono, urlsv, tipoultra, fecha )
    enviar_img(telefono, urlsi, tipoultra, fecha)
    enviar_galeriaResultados(telefono)

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
        print(response.text)


def message_ayuda(numero):
    data={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": numero,
        "type": "text",
        "text": {
            "preview_url": False,
           "body": "¡Hola! Soy EnlaceDigna y estoy aquí para ayudarte. 😊 Por favor escribe el numero para poder comunicarme contigo:\n"

                 "1-🏥 Recordar comandos y obtener informacion de contacto de Salud Digna.\n"
                  +"2-📷 Obtener la url de tu galeria personal.\n"
                  +"3-📱 Verificacion para cambiar tu numero de telefono.\n"
                  +"4-🔑 Obten tu token unico.\n"
                  +"5-📋 Historial para ver tus ultrasonidos en forma de lista.\n"
                  

        }
    }

    headers = {
        "Authorization": f"Bearer {getToken()}",
        "Content-Type": "application/json"
    }

    
    response = requests.post(getURL(), headers=headers, json=data)

    data={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": numero,
        "type": "text",
        "text": {
            "preview_url": True,
           "body": "Para ponerte en contacto con Salud Digna, puedes llamar al siguiente número: 📞 9992121921 o visitar su página web: 🌐 https://www.salud-digna.org/"

        }
    }

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



def enviar_pedirNumero(telefono):
    data={
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52'+telefono,
          "type": "text",
          "text": {
              "preview_url": False,
            "body": "¡Hola! ¿Podrías escribir el número anterior, por favor? 😊"

          }
      }

    headers = {
          "Authorization": f"Bearer {getToken()}",
          "Content-Type": "application/json"
      }

      
    response = requests.post(getURL(), headers=headers, json=data)

      # Maneja la respuesta de requests y devuelve una respuesta adecuada para Django REST Framework
    if response.status_code == 200:
          print('Se envio el mensaje')
          
    else:
          print(response.text)


def enviar_cambioNumero(numero,telefono):
    
    verificacion=verificarNumeroParaCorreo(numero)
    if verificacion==True:
      data={
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52'+telefono,
          "type": "text",
          "text": {
              "preview_url": False,
            "body": "¡Excelente! Hemos encontrado tu número anterior. Pronto recibirás una confirmación por correo para que puedas actualizarlo. 📧 ¡Gracias por tu atención!"

          }
      }

      headers = {
          "Authorization": f"Bearer {getToken()}",
          "Content-Type": "application/json"
      }

      
      response = requests.post(getURL(), headers=headers, json=data)

      # Maneja la respuesta de requests y devuelve una respuesta adecuada para Django REST Framework
      if response.status_code == 200:
          print('Se envio el mensaje')
          
      else:
          print(response.text)

    else:
        data={
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52'+telefono,
          "type": "text",
          "text": {
              "preview_url": False,
            "body": "Lo siento mucho, parece que no pudimos encontrar tu número. Te pido que lo revises y nos lo envíes de nuevo, por favor. ¡Gracias por tu comprensión! 🙏"

          }
      }

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


    
  

def enviarLista(numero):
    data = verificar_DevolverLista(numero)
    try:
      # Convierte la lista de tuplas en una cadena de texto formateada
      lista_formateada = "\n".join([f" {item[0]} Tipo de ultrasonido: {item[1]}, Fecha de ultrasonido: {item[2]}" for item in data])

      # Define el cuerpo del mensaje incluyendo la lista formateada
      body_message = f"¡Hola! 😊 Aquí tienes la lista de todos tus ultrasonidos. Recuerda que puedes pedir el envío de tus ultrasonidos nuevamente escribiendo el número correspondiente. 📝: \n{lista_formateada}"

      # Define los datos del mensaje
      message_data = {
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52' + numero,
          "type": "text",
          "text": {
              "preview_url": False,
              "body": body_message
          }
      }

      headers = {
          "Authorization": f"Bearer {getToken()}",
          "Content-Type": "application/json"
      }
      response = requests.post(getURL(), headers=headers, json=message_data)

      

    except:
        estado_usuario, created = EstadoUsuario.objects.get_or_create(telefono="521"+numero)
        estado_usuario.opcion_seleccionada = None
        estado_usuario.save()
        message_data = {
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52' + numero,
          "type": "text",
          "text": {
              "preview_url": False,
              "body": '¡Hola! 😊 Lamento decirte que no encontré ningún ultrasonido relacionado con este número. 😕\nPuedes comunicarte al número 9991929211 para obtener más información. 📞'
          }
      }

        headers = {
          "Authorization": f"Bearer {getToken()}",
          "Content-Type": "application/json"
      }
        
        
        response = requests.post(getURL(), headers=headers, json=message_data)
        if response.status_code == 200:
          print('Se envió el mensaje')
        else:
          print(response.text)



def enviar_gracias(telefono):
    
    data={
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52'+telefono,
          "type": "text",
          "text": {
              "preview_url": False,
            "body": "¡De nada! Es un placer poder ayudarte. Espero que hayas quedado satisfecho con mi servicio. 😊 ¡No dudes en contactarme si necesitas algo más!"

          }
      }

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



def enviarToken_conNumero(numero):
    

    id=ObtenerToken(numero)
    data={
          "messaging_product": "whatsapp",    
          "recipient_type": "individual",
          "to": '52'+numero,
          "type": "text",
          "text": {
              "preview_url": False,
            "body": "¡Hola! 😊 ¡Aquí está tu ID: "+ str(id)+"! 🎉 Recuerda que con esto puedes acceder a tu galería. Si quieres ver tu galería, simplemente escribe 2 . ¡Disfruta! 📸 "

          }
      }

    headers = {
          "Authorization": f"Bearer {getToken()}",
          "Content-Type": "application/json"
      }

      
    response = requests.post(getURL(), headers=headers, json=data)

    if response.status_code == 200:
          print('Se envio el mensaje')
          
    else:
          print(response.status_code)





def enviarUltra_deLista(telefono, mensaje):
    
    try:
      urls, fecha, nombre=ObtenerURL_Opcion(mensaje)
      print('URL: ', urls, 'Fecha: ' , fecha, 'Nombre: ', nombre )
      
      urlImg, urlVideo = separarURL(urls)
      data={
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": '52'+telefono,
            "type": "text",
            "text": {
                "preview_url": False,
              "body": "¡Estupendo! Has seleccionado el ultrasonido " + mensaje + " 😊. ¡Pronto recibirás tus resultados de nuevo! 🎉"

            }
        }

      headers = {
            "Authorization": f"Bearer {getToken()}",
            "Content-Type": "application/json"
        }

      
      response = requests.post(getURL(), headers=headers, json=data)
      enviar_img('52'+telefono, urlImg, nombre, str(fecha) )
      enviar_videos('52'+telefono, urlVideo,nombre, str(fecha) )
        # Maneja la respuesta de requests y devuelve una respuesta adecuada para Django REST Framework
      if response.status_code == 200:
            print('Se envio el mensaje')
            
      else:
            print(response.status_code)
    except:
         data={
             "messaging_product": "whatsapp",    
             "recipient_type": "individual",
             "to": '52'+telefono,
             "type": "text",
             "text": {
                 "preview_url": False,
               "body": "¡Ups! Parece que no pude encontrar la opción que seleccionaste. Por favor, inténtalo de nuevo para solicitar tu ultrasonido. 🔄"

             }
         }

         headers = {
             "Authorization": f"Bearer {getToken()}",
             "Content-Type": "application/json"
         }
         response = requests.post(getURL(), headers=headers, json=data)