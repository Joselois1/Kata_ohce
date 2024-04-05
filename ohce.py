import time

class Ohce:
    name = ""
    def __init__(self):
        pass

    def get_hora_actual(self):
        hora_actual = int(time.strftime("%H"))
        return hora_actual

    def start(self):  #Input de nombre comenzando con ohce
        while True:
            initial_input = input()
            if initial_input.startswith("ohce "):
                self.name = initial_input[5:] 
                hora_actual = self.get_hora_actual()
                if hora_actual >= 20 or hora_actual < 6:
                    print("¡Buenas noches {}!".format(self.name))
                elif hora_actual >= 6 and hora_actual < 12:
                    print("¡Buenos días {}!".format(self.name))
                else:
                    print("¡Buenas tardes {}!".format(self.name))
                break

    def reverse_string(self, text): #Revierte el string 
        text_rev = ""
        for char in text:
            text_rev = char + text_rev
        return text_rev

    def is_palindrome(self, text): #Entrega True or False si el texto es o no palindromo
        text_rev = self.reverse_string(text)
        return text.lower() == text_rev.lower()  

    def process_input(self, text): #Procesa los string despues de inicializar el nombre y sale del programa si el input es Stop!
        #text = text.lower()  
        if text == "Stop!":
            return "Adios {}!".format(self.name)
            
        elif self.is_palindrome(text):
            return "{} ¡Bonita palabra!".format(self.reverse_string(text))
        else:
            return self.reverse_string(text)


ohce = Ohce()
ohce.start()

while True:
    text = input()
    response = ohce.process_input(text)
    print(response)
    if response.startswith("Adios "): break





