# main.py

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
    