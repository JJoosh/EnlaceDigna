import os
import urllib.request
from twilio.rest import Client

url = ['https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/Screenshot-8.png', 
     'https://saluddignaultra.s3.us-east-2.amazonaws.com/ultrasonidos/Screenshot+from+2024-03-22+11-33-19.png']
def descargar(urls):
    contador=0
    for url in urls:
            
            
            parts = url.split('/')
            nombre_archivo = parts[-1]
            urllib.request.urlretrieve(url, nombre_archivo)
            
            send_archivo('9991723856', url, contador)
            print(contador)
            contador=contador+1
            os.remove(nombre_archivo)
            

def send_archivo(telefono, url, contador):
    account_sid = 'AC7e929a8080463ba6deb0f70eb5bb8cd3'
    auth_token = '997a82291ef84acc64d4a4b4a26ccf5f'
    print(contador, 'olaa')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',  # Este es el número de Twilio que configuraste para WhatsApp
    to='whatsapp:+521'+telefono, 
    media_url=url 
    )

    if contador==0:
         
         client=Client(account_sid, auth_token)
         message=client.messages.create(
              body='Hola Arturo!, estos son los resultados de tu ultrasonido que te realizaste el dia Martes',
              from_='whatsapp:+14155238886',  # Este es el número de Twilio que configuraste para WhatsApp
              to='whatsapp:+521'+telefono, 
         )

    

descargar(url)

