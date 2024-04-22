#location.py

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

