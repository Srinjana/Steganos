# Steganography 
---
According to Google, <b>Steganography</b> is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. The word steganography comes from Greek _steganographia_ , which combines the words steganós _(στεγανός)_, meaning "covered or concealed", and -graphia _(γραφή)_ meaning "writing".
Unlike cryptography, which conceals the contents of a secret message, steganography conceals the very fact that a message is communicated. Although steganography differs from cryptography, there are many analogies between the two, and some authors classify steganography as a form of cryptography since hidden communication is a type of secret message.

## Steganography VS Cryptography:

Up until now, cryptography has always had its ultimate role in protecting the secrecy between the sender and the intended receiver. However, nowadays steganography techniques are used increasingly besides cryptography to add more protective layers to the hidden data. The advantage of using steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which encryption is illegal.

### Types of Steganography

<img src="https://miro.medium.com/max/3000/0*0PvWnJdRtDMkh8JS" width="700" height="400">

## In this project we use *LSB Steganograhy* to Perform Image, Video and Audio Steganography.

We can describe a digital image as a finite set of digital values, called pixels. Pixels are the smallest individual element of an image, holding values that represent the brightness of a given color at any specific point. So we can think of an image as a matrix (or a two-dimensional array) of pixels which contains a fixed number of rows and columns.
Least Significant Bit (LSB) is a technique in which the last bit of each pixel is modified and replaced with the secret message’s data bit.

Each pixel contains three values which are Red, Green, Blue, these values range from 0 to 255, in other words, they are 8-bit values. Let’s take an example of how this technique works, suppose you want to hide the message *“hi”* into a 4x4 image which has the following pixel values:

`
[(225, 12, 99), (155, 2, 50), (99, 51, 15), (15, 55, 22),(155, 61, 87), (63, 30, 17), (1, 55, 19), (99, 81, 66),(219, 77, 91), (69, 39, 50), (18, 200, 33), (25, 54, 190)]
`

Using the ASCII Table, we can convert the secret message into decimal values and then into binary: 0110100 0110101.Now, we iterate over the pixel values one by one, after converting them to binary, we replace each least significant bit with that message bits sequentially _(e.g 225 is 11100001, we replace the last bit, the bit in the right (1) with the first data bit (0) and so on). This will only modify the pixel values by *+1 or -1* which is not noticeable at all. The resulting pixel values after performing LSBS is as shown below:

`
[(224, 13, 99),(154, 3, 50),(98, 50, 15),(15, 54, 23),(154, 61, 87),(63, 30, 17),(1, 55, 19),(99, 81, 66),(219, 77, 91),(69, 39, 50),(18, 200, 33),(25, 54, 190)]
`

<img src="https://3.bp.blogspot.com/-Y2mozhtViLQ/WnIwaQdEKfI/AAAAAAAAKGs/Z78gfWuI1bMfDeyNcCf0uBsS7Ttr6LQdgCLcBGAs/s1600/encode.png" width="700" height="300">

## Results:
* ### Image Steganography
   Here is a comparison of the *Input Image* and *Encoded Output Image* -
   
<img src="https://raw.githubusercontent.com/Srinjana/Steganos/main/static/download.png" width="300" height="300">   <img src="https://raw.githubusercontent.com/Srinjana/Steganos/main/static/trial.png" width="300" height="300"> 

The encoded Text was : `hello world`
  

* ### Video Steganography
 This is the one which gave me some trouble. The input video is first broken into Frames and the Secret message is split and hidden in the individual frames. the frames are again sown together to form a video file with almost no noticable changes and the Audio to the video-file remains unaltered. I used the video `./static/seal.mp4` as input audio and encoded the text `Hakuna Matata` which worked successfully, but significantly increased the video size. 
 
 
* ### Audio Steganography
I used an Audio made by a friend for this purpose. [Check it out](https://soundcloud.com/agnibesh-mukherjee/myfirstlofimp3). Encrypting Text inside an audio file degrades it overall quality and thus the output audio at `./static/lofi.wav` has some unwanted noise, But still isn't that apparent.

The encoded text was of a fairly significant sign = ` Our agent has been compromised`, but still didn't make the audio file unintelligible.


## References:
Find out more about how I approached the problems here ⬇ ⬇ ⬇

* [Video Steganography in Python](https://betterprogramming.pub/a-guide-to-video-steganography-using-python-4f010b32a5b7)

* [Image Steganography in Python](https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372)

* [Audio Steganography in Python](https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3)

#### TBD: Add GUI to the whole prject and make it more interactive.
