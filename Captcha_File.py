# Import The following Module
from captcha.image import ImageCaptcha

# Create an image instance of the given size
image = ImageCaptcha(width = 280,height = 90)

# Image Captcha Text
captcha_text = "Heloo12345 "

# generate the image of the given text
data = image.generate(captcha_text)

# write the image on the given file and save it
image.write(captcha_text, "CAPTCHA.png")