import re

def sanitize_filename(filename):
    """
    Sanitiza el nombre del archivo para eliminar caracteres no seguros y restringir
    a un conjunto conocido y seguro de caracteres.

    Args:
    - filename (str): El nombre original del archivo.

    Returns:
    - str: El nombre del archivo sanitizado.
    """
    # Elimina caracteres que no sean letras, números, guiones, o guiones bajos
    sanitized = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
    # Opcional: limita la longitud del nombre del archivo a un máximo razonable, por ejemplo, 255 caracteres
    return sanitized[:255]
