import wave
# read wave audio file

# def read_wave(audio):
#     song = wave.open(audio, mode='rb')
#     byte_frames = bytearray(list(song.readframes(song.getnframes())))
#     return byte_frames

def encoding (file_nm, string):

    # Read frames and convert to byte array
    song = wave.open(file_nm, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) * '#'
    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))

    # Replacing LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open('song_embedded.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()


def decoding(en_file_nm):
    song = wave.open("song_embedded.wav", mode='rb')


    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    string = "".join(chr(
        int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]

    return decoded
    song.close()


def main ():
    while True:
        print("--- SELECT AN OPTION TO PERFORM AUDIO STEGANOGRAPHY ---")
        print("1.Hide a secret message in an audio file \n2.Reveal the secret message from the audio")
        print("Enter any other key to exit")
        choice = input("Enter your key here: ")
        if (choice == 1):
            file_nm = input("Enter the name of your audio-file of choice, with extension: ")
            secret = input("Enter your secret message: ")

            encoding(file_nm, secret)

            print("[INFO] YOUR MESSAGE HAS BEEN RECORDED.")
            print("[INFO] Your encoded audio is saved as 'song_embedded.wav'.")

        elif (choice == 2):
            en_file_nm = input("Enter the name of your encoded audio-file, with extension: ")
            secret = decoding(en_file_nm)
            # Print the extracted text
            print("[INFO] Your secret message has been decoded successfully.")
            print(" ")
            print("Your secret message is: "+secret)
        
        else:
            print ("Exiting...")
            break


