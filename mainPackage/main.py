# main.py

# Name: Aimee Madrigal, Rhodas Yemaneab, Smita Magar
# email: ignaciac@mail.uc.edu, yemanert@mail.uc.edu, diswamsa@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: Program produces the correct results by decrypting the the code provided with all the necessary Python modules documented properly, and correct project architecture. The results print the decrypted location, movie title, and the photo.   
# Brief Description of what this module does: This module imports the code from the movie, location and photo modules. It lets us decrypt the code and prints the decrypted location, movie title, and the photo
# Citations:  Stack overflow and chatgpt
# Anything else that's relevant: N/A

from locationPackage.location import *
from moviePackage.movie import *
from photoPackage.photo import *
   
# Location
if __name__ == "__main__":
    encrypted_location_data = [
        "7480",
        "28894",
        "8018",
        "46342",
        "42061",
        "103568",
        "346",
        "13068",
        "23887",
        "21407"
    ]
    english_file_path = 'UCEnglish.txt'
    
    decrypted_location = decrypt_location(encrypted_location_data, english_file_path)
    print(f"The decrypted location is: {decrypted_location}")
   
    
# Movie Title
from cryptography.fernet import Fernet

if __name__ == "__main__":
    encrypted_message_file = "TeamsAndEncryptedMessagesForDistribution - 001.json"
    decryption_key = 'r0J5NgEGqsxufa0af1zLpy8DaNhQ9C9ur6PBWqialy4='
    fernet_key = Fernet(decryption_key)
    
    decrypted_movie = movie_title(fernet_key, encrypted_message_file)
    print(f"The movie title is:", decrypted_movie)
   
      
# Photo
if __name__ == "__main__":
    photo_path = "FightClubPhoto.jpg"
    display_photo(photo_path)
    