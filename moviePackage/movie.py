#movie.py

# Name: Aimee Madrigal, Rhodas Yemaneab, Smita Magar
# email: ignaciac@mail.uc.edu, yemanert@mail.uc.edu, diswamsa@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: Program produces the correct results by decrypting the the code provided with all the necessary Python modules documented properly, and correct project architecture. The results print the decrypted location, movie title, and the photo.   
# Brief Description of what this module does: This module decrypts the movie title and returns Fight Club.
# Citations:  Stack overflow and chatgpt
# Anything else that's relevant: N/A

import json



def movie_title(fernet_key, encrypted_message_file):
    '''
    This function decrypts the movie title for team Hamster.
    '''
    with open(encrypted_message_file, 'r') as file:
        encrypted_data = json.load(file)["Hamster"][0]
    decrypted_message = fernet_key.decrypt(encrypted_data.encode())
    return decrypted_message.decode()

