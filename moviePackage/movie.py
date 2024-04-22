#movie.py

import json



def movie_title(fernet_key, encrypted_message_file):
    '''
    This function decrypts the movie title for team Hamster.
    '''
    with open(encrypted_message_file, 'r') as file:
        encrypted_data = json.load(file)["Hamster"][0]
    decrypted_message = fernet_key.decrypt(encrypted_data.encode())
    return decrypted_message.decode()

