#location.py

# Name: Aimee Madrigal, Rhodas Yemaneab, Smita Magar
# email: ignaciac@mail.uc.edu, yemanert@mail.uc.edu, diswamsa@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: Program produces the correct results by decrypting the the code provided with all the necessary Python modules documented properly, and correct project architecture. The results print the decrypted location, movie title, and the photo.   
# Brief Description of what this module does: This module decrypts and returns the hidden location.
# Citations:  Stack overflow and chatgpt
# Anything else that's relevant: N/A

def decrypt_location(encrypted_location_data, english_file_path):
    '''
    This function decrypts the location data for team Hamster.
    '''
    with open(english_file_path, 'r', encoding='utf-8') as file:
        english_lines = file.readlines()
    decrypted_location = ''
    for index in encrypted_location_data:
        decrypted_location += english_lines[int(index)].strip()
    return decrypted_location

