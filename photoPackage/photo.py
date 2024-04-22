# photo.py

from PIL import Image

def display_photo(photo_path):
    '''
    This function displays the photo we took at the decrypted location and a famous quote from the decrypted movie title.
    ''' 
    img = Image.open(photo_path)
    img.show()