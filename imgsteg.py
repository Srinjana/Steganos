from stegano import lsb
secret = lsb.hide('./images/flores.jpg', 'hello world')
secret.save('./images/encoded_image.jpg')
lsb.reveal('./images/encoded_image.jpg')

