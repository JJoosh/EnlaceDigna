import SimpleITK as sitk
import cv2
import os

# Cargar el archivo DICOM
image = sitk.ReadImage('https://saluddignaultra.s3.us-east-2.amazonaws.com/00000001.dcm')

# Obtener dimensiones
size = image.GetSize()
num_dimensions = image.GetDimension()

if num_dimensions == 4:
    width, height, depth, num_frames = size
elif num_dimensions == 3:
    width, height, num_frames = size
    depth = 1
else:
    raise ValueError("La imagen debe tener 3 o 4 dimensiones")

# Crear una carpeta para guardar los frames
output_folder = 'ruta/a/la/carpeta/de/salida'
os.makedirs(output_folder, exist_ok=True)

# Iterar sobre los frames y guardarlos como imágenes
for i in range(num_frames):
    if num_dimensions == 4:
        image_slice = image[:,:,:,i]
    else:
        image_slice = image[:,:,i]

    image_array = sitk.GetArrayFromImage(image_slice)
    
    # Convertir el frame a formato BGR (orden de color de OpenCV)
    image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    
    # Guardar el frame como una imagen
    output_path = os.path.join(output_folder, f'frame_{i:04d}.png')
    cv2.imwrite(output_path, image_bgr)

# Crear el escritor de video
video_file = 'video_output.avi'
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Codec Motion JPEG
fps = 10  # Ajusta los fps según tus necesidades
video_writer = cv2.VideoWriter(video_file, fourcc, fps, (width, height), isColor=True)

# Leer las imágenes guardadas y escribirlas en el video
for i in range(num_frames):
    frame_path = os.path.join(output_folder, f'frame_{i:04d}.png')
    frame = cv2.imread(frame_path, cv2.IMREAD_UNCHANGED)
    video_writer.write(frame)

# Liberar el escritor de video
video_writer.release()