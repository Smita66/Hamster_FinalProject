# photo.py

# Name: Aimee Madrigal, Rhodas Yemaneab, Smita Magar
# email: ignaciac@mail.uc.edu, yemanert@mail.uc.edu, diswamsa@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: Program produces the correct results by decrypting the the code provided with all the necessary Python modules documented properly, and correct project architecture. The results print the decrypted location, movie title, and the photo.   
# Brief Description of what this module does: This function displays the photo we took at the decrypted location and a famous quote from the decrypted movie title.
# Citations:  Stack overflow and chatgpt
# Anything else that's relevant: N/A

from PIL import Image

def display_photo(photo_path):
    '''
    This function displays the photo and famous movie quote taken at the decrypted location.
    ''' 
    img = Image.open(photo_path)
    img.show()