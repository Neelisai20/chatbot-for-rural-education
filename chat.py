# """import random
# import json

# import torch

# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# with open('intents.json', 'r') as json_data:
#     intents = json.load(json_data)

# FILE = "data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# bot_name = "Study-Buddy"
# print("Let's chat! (type 'quit' to exit)")
# while True:
#     # sentence = "do you use credit cards?"
#     sentence = input("You: ")
#     if sentence == "quit":
#         break

#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         print(f"{bot_name}: I do not understand...") """


# """import random
# import json
# import torch
# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize
# from googletrans import Translator  # Import the Translator class from googletrans library

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# with open('intents.json', 'r') as json_data:
#     intents = json.load(json_data)

# FILE = "data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# bot_name = "Study-Buddy"
# translator = Translator()  # Create an instance of the Translator class

# def translate_text(text, target_language='en'):
#     # Use the translate method to translate the text to the target language
#     translated_text = translator.translate(text, dest=target_language).text
#     return translated_text

# def get_chatbot_response(user_input):
#     # Your existing chatbot logic remains unchanged
#     sentence = tokenize(user_input)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 # Translate the response back to the user's language
#                 return translate_text(random.choice(intent['responses']), target_language='en')  # Assuming English is the target language
#     else:
#         return translate_text("I do not understand...", target_language='en')  # Assuming English is the target language

# print("Let's chat! (type 'quit' to exit)")
# while True:
#     user_input = input("You: ")
#     if user_input == "quit":
#         break

#     # Detect the language of the user's input
#     user_language = translator.detect(user_input).lang

#     # Translate user input to English for processing
#     translated_input = translate_text(user_input, target_language='en')

#     # Get the chatbot response and translate it back to the user's language
#     chatbot_response = get_chatbot_response(translated_input)
#     translated_response = translate_text(chatbot_response, target_language=user_language)

#     print(f"{bot_name}: {translated_response}")"""
# '''before GUI'''
# '''import random
# import json
# import torch
# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize
# from googletrans import Translator  # Import the Translator class from googletrans library
# import speech_recognition as sr

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# with open('intents.json', 'r') as json_data:
#     intents = json.load(json_data)

# FILE = "data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# bot_name = "Study-Buddy"
# translator = Translator()  # Create an instance of the Translator class
# recognizer = sr.Recognizer()

# def translate_text(text, target_language='en'):
#     # Use the translate method to translate the text to the target language
#     translated_text = translator.translate(text, dest=target_language).text
#     return translated_text

# def get_chatbot_response(user_input):
#     # Your existing chatbot logic remains unchanged
#     sentence = tokenize(user_input)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 # Translate the response back to the user's language
#                 return translate_text(random.choice(intent['responses']), target_language='en')  # Assuming English is the target language
#     else:
#         return translate_text("I do not understand...", target_language='en')  # Assuming English is the target language

# def get_text_input():
#     return input("You: ")

# def get_voice_input():
#     print("Listening... Speak now.")
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     print("Processing...")

#     try:
#         user_input = recognizer.recognize_google(audio)
#         print("Voice Input:", user_input)
#         return user_input
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand your voice.")
#         return ""
#     except sr.RequestError as e:
#         print(f"Error with the voice recognition service; {e}")
#         return ""

# print("Let's chat! (type 'quit' to exit)")
# while True:
#     print("Choose input method:")
#     print("1. Text")
#     print("2. Voice")
#     choice = input("Enter your choice (1 or 2): ")

#     if choice == '1':
#         user_input = get_text_input()
#     elif choice == '2':
#         user_input = get_voice_input()
#     else:
#         print("Invalid choice. Please enter 1 or 2.")
#         continue

#     if user_input.lower() == "quit":
#         break

#     # Detect the language of the user's input
#     user_language = translator.detect(user_input).lang

#     # Translate user input to English for processing
#     translated_input = translate_text(user_input, target_language='en')

#     # Get the chatbot response and translate it back to the user's language
#     chatbot_response = get_chatbot_response(translated_input)
#     translated_response = translate_text(chatbot_response, target_language=user_language)

#     print(f"{bot_name}: {translated_response}")'''





# import tkinter as tk
# from tkinter import ttk
# import threading
# import queue
# import random
# import json
# import torch
# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize
# from googletrans import Translator
# import speech_recognition as sr

# class ChatbotGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chatbot GUI")

#         self.initialize_chatbot()

#         self.create_widgets()

#     def initialize_chatbot(self):
#         with open('intents.json', 'r') as json_data:
#             self.intents = json.load(json_data)

#         FILE = "data.pth"
#         data = torch.load(FILE)

#         input_size = data["input_size"]
#         hidden_size = data["hidden_size"]
#         output_size = data["output_size"]
#         self.all_words = data['all_words']
#         self.tags = data['tags']
#         model_state = data["model_state"]

#         self.model = NeuralNet(input_size, hidden_size, output_size)
#         self.model.load_state_dict(model_state)
#         self.model.eval()

#         self.bot_name = "Study-Buddy"
#         self.translator = Translator()
#         self.recognizer = sr.Recognizer()
#         self.listening = False
#         self.queue = queue.Queue()

#     def create_widgets(self):
#         # Increase the width and height of the Text widget
#         self.output_text = tk.Text(self.root, wrap="word", width=60, height=15, state="disabled")
#         self.output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#         # Increase the width of the Entry widget
#         self.input_entry = tk.Entry(self.root, width=60)
#         self.input_entry.grid(row=1, column=0, padx=10, pady=10)

#         # Increase the width of the Button widgets
#         self.send_button = tk.Button(self.root, text="Send", command=self.send_message, width=20)
#         self.send_button.grid(row=1, column=1, padx=10, pady=10)

#         self.voice_button = tk.Button(self.root, text="Hold to Speak", command=self.toggle_voice_input, width=40)
#         self.voice_button.grid(row=2, column=0, columnspan=2, pady=10)

#         # Bind mouse press and release events to the toggle_voice_input function
#         self.voice_button.bind("<ButtonPress-1>", lambda event: self.toggle_voice_input(event, start=True))
#         self.voice_button.bind("<ButtonRelease-1>", lambda event: self.toggle_voice_input(event, start=False))

#         self.root.after(100, self.check_queue)

#     def send_message(self):
#         user_input = self.input_entry.get()
#         self.input_entry.delete(0, "end")

#         if user_input.lower() == "quit":
#             self.root.destroy()

#         user_language = self.translator.detect(user_input).lang
#         translated_input = self.translate_text(user_input, target_language='en')

#         chatbot_response = self.get_chatbot_response(translated_input)
#         user_language = self.translator.detect(user_input).lang
#         translated_response = self.translate_text(chatbot_response, target_language=user_language)

#         self.display_message(f"You: {user_input}")
#         self.display_message(f"{self.bot_name}: {translated_response}")

#     def toggle_voice_input(self, event=None, start=True):
#         if start:
#             self.voice_button.config(text="Listening...", state=tk.DISABLED)
#             self.listening = True
#             threading.Thread(target=self.process_voice_input).start()
#         else:
#             self.voice_button.config(text="Hold to Speak", state=tk.NORMAL)
#             self.listening = False

#     def process_voice_input(self):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             audio = self.recognizer.listen(source)

#         try:
#             user_input = self.recognizer.recognize_google(audio)
#             translated_input = self.translate_text(user_input, target_language='en')

#             chatbot_response = self.get_chatbot_response(translated_input)
#             user_language = self.translator.detect(user_input).lang
#             translated_response = self.translate_text(chatbot_response, target_language=user_language)

#             self.display_message(f"Voice Input: {user_input}")
#             self.display_message(f"{self.bot_name}: {translated_response}")

#         except sr.UnknownValueError:
#             self.display_message("Sorry, I could not understand your voice.")
#         except sr.RequestError as e:
#             self.display_message(f"Error with the voice recognition service; {e}")        # existing code ...

#     def display_message(self, message):
#         self.output_text.config(state="normal")
#         self.output_text.insert("end", f"{message}\n")
#         self.output_text.see("end")
#         self.output_text.config(state="disabled")

#     def translate_text(self, text, target_language='en'):
#         translated_text = self.translator.translate(text, dest=target_language).text
#         return translated_text

#     def get_chatbot_response(self, user_input):
#         sentence = tokenize(user_input)
#         X = bag_of_words(sentence, self.all_words)
#         X = X.reshape(1, X.shape[0])
#         X = torch.from_numpy(X)

#         output = self.model(X)
#         _, predicted = torch.max(output, dim=1)

#         tag = self.tags[predicted.item()]

#         probs = torch.softmax(output, dim=1)
#         prob = probs[0][predicted.item()]
#         if prob.item() > 0.75:
#             for intent in self.intents['intents']:
#                 if tag == intent["tag"]:
#                     return random.choice(intent['responses'])
#         else:
#             return "I do not understand..."

#     def check_queue(self):
#         try:
#             message = self.queue.get_nowait()
#             self.display_message(message)
#         except queue.Empty:
#             pass

#         self.root.after(100, self.check_queue)

# if __name__ == "__main__":
#     root = tk.Tk()
#     chatbot_gui = ChatbotGUI(root)
#     root.mainloop()
# import streamlit as st
# import random
# import json
# import torch
# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize
# from googletrans import Translator
# import speech_recognition as sr

# class Chatbot:
#     def __init__(self):
#         self.initialize_chatbot()

#     def initialize_chatbot(self):
#         with open('intents.json', 'r') as json_data:
#             self.intents = json.load(json_data)

#         FILE = "data.pth"
#         data = torch.load(FILE, weights_only=True)  # Set weights_only=True

#         input_size = data["input_size"]
#         hidden_size = data["hidden_size"]
#         output_size = data["output_size"]
#         self.all_words = data['all_words']
#         self.tags = data['tags']
#         model_state = data["model_state"]

#         self.model = NeuralNet(input_size, hidden_size, output_size)
#         self.model.load_state_dict(model_state)
#         self.model.eval()

#         self.bot_name = "Study-Buddy"
#         self.translator = Translator()
#         self.recognizer = sr.Recognizer()

#     def get_chatbot_response(self, user_input):
#         sentence = tokenize(user_input)
#         X = bag_of_words(sentence, self.all_words)
#         X = X.reshape(1, X.shape[0])
#         X = torch.from_numpy(X)

#         output = self.model(X)
#         _, predicted = torch.max(output, dim=1)

#         tag = self.tags[predicted.item()]

#         probs = torch.softmax(output, dim=1)
#         prob = probs[0][predicted.item()]
#         if prob.item() > 0.75:
#             for intent in self.intents['intents']:
#                 if tag == intent["tag"]:
#                     return random.choice(intent['responses'])
#         else:
#             return "I do not understand..."

#     def translate_text(self, text, target_language='en'):
#         if text and self.translator.detect(text).lang != target_language:
#             return self.translator.translate(text, dest=target_language).text
#         return text

#     def handle_input(self, user_input, is_voice=False):
#         if is_voice:
#             user_input = self.process_voice_input()

#         if user_input:
#             user_language = self.translator.detect(user_input).lang
#             translated_input = self.translate_text(user_input, target_language='en')
#             chatbot_response = self.get_chatbot_response(translated_input)
#             translated_response = self.translate_text(chatbot_response, target_language=user_language)
#             return translated_response
#         return "Sorry, I didn't catch that."

#     def process_voice_input(self):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             st.write("Listening... Please speak now.")
#             audio = self.recognizer.listen(source)

#         try:
#             return self.recognizer.recognize_google(audio)
#         except sr.UnknownValueError:
#             return "Sorry, I could not understand your voice."
#         except sr.RequestError as e:
#             return f"Error with the voice recognition service; {e}"

# chatbot = Chatbot()

# st.title("CHATBOT TO ASSIST RURAL EDUCATION")
# st.write("Ask me anything!")

# user_input = st.text_input("You:", "")

# if st.button("Send") and user_input:
#     response = chatbot.handle_input(user_input)
#     st.write(f"{chatbot.bot_name}: {response}")

# if st.button("🎙️"):
#     response = chatbot.handle_input("", is_voice=True)
#     st.write(f"{chatbot.bot_name}: {response}")

import streamlit as st
import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from googletrans import Translator
import speech_recognition as sr

class Chatbot:
    def __init__(self):
        self.initialize_chatbot()

    def initialize_chatbot(self):
        with open('intents.json', 'r') as json_data:
            self.intents = json.load(json_data)

        FILE = "data.pth"
        data = torch.load(FILE, weights_only=True)  # Set weights_only=True

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        self.all_words = data['all_words']
        self.tags = data['tags']
        model_state = data["model_state"]

        self.model = NeuralNet(input_size, hidden_size, output_size)
        self.model.load_state_dict(model_state)
        self.model.eval()

        self.bot_name = "Study-Buddy"
        self.translator = Translator()
        self.recognizer = sr.Recognizer()

    def get_chatbot_response(self, user_input):
        sentence = tokenize(user_input)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in self.intents['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])
        else:
            return "I do not understand..."

    def translate_text(self, text, target_language='en'):
        if text and self.translator.detect(text).lang != target_language:
            return self.translator.translate(text, dest=target_language).text
        return text

    def handle_input(self, user_input, is_voice=False):
        if is_voice:
            user_input = self.process_voice_input()

        if user_input:
            user_language = self.translator.detect(user_input).lang
            translated_input = self.translate_text(user_input, target_language='en')
            chatbot_response = self.get_chatbot_response(translated_input)
            translated_response = self.translate_text(chatbot_response, target_language=user_language)
            return translated_response
        return "Sorry, I didn't catch that."

    def process_voice_input(self):
        with sr.Microphone() as source:
            st.write("Adjusting for ambient noise, please wait...")
            self.recognizer.adjust_for_ambient_noise(source)
            st.write("Listening... Please speak now.")
            audio = self.recognizer.listen(source)

        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I could not understand your voice."
        except sr.RequestError as e:
            return f"Error with the voice recognition service; {e}"

chatbot = Chatbot()

st.title("CHATBOT TO ASSIST RURAL EDUCATION")
st.write("Ask me anything!")

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    response = chatbot.handle_input(user_input)
    st.write(f"{chatbot.bot_name}: {response}")

# Since Streamlit doesn't support direct microphone input in web environments, this may not work in Streamlit Cloud.
if st.button("🎤"):
    response = chatbot.handle_input("", is_voice=True)
    st.write(f"{chatbot.bot_name}: {response}")
