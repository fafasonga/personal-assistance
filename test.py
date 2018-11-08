import os
from gtts import gTTS
from langdetect import detect






# text = ""
# with open("sample_fr.txt", "r") as file:
#     for line in file:
#         text = text + line
#
# speech = gTTS(text, lang=detect(text))
# speech.save("sample.mp3")
# os.system("mpg321 sample.mp3")


# # plain_text = 'Murakaza neza, amakuru yanyu'
# # plain_text = "Salut, comment allez-vous"
# plain_text = "Nous allons très bien merci"
# # plain_text = "turaho turakomeye"
# print(detect(plain_text))
# tts = gTTS(text=plain_text, lang=detect(plain_text))  # Kinya better to use lang='id'
# tts.save("kiny.mp3")
# os.system("mpg321 kiny.mp3")
