# Importation des modules nécessaires
import tkinter as tk
import pygame
from tkinter import messagebox
import speech_recognition as sr
import threading
from PIL import Image, ImageTk


pygame.init()
audio_play = []

pygame.mixer.init()

def play_audio(file):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    except Exception as e:
        print("Erreur lors de la lecture audio :", e)

def execute_audio_sequence():
    for audio_file in audio_play:
        play_audio(audio_file)
        # Wait for audio to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

def stop_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    audio_play.clear() 



def vol(text):
    try:
        audio_play.append(f"evol{text}.mp3")
    except Exception as e:
        print("Une erreur s'est produite :", e)


def vol20_99(text):
    x = int(text[0]) * 10
    if text[1] != "0":
        vol(text[1])
        audio_play.append("evolou.mp3")
    vol(str(x))

def vol0_99(text):
    x=int(text)
    if x<20:
        if x<10:
           vol(text[1])
        else:vol(text)
    else:
        x = int(text[0]) * 10
        if text[1] != "0":
           vol(text[1])
           audio_play.append("evolou.mp3")
        vol(str(x))

def vol1OO_999(text):
    x = int(text[0]) * 100
    if x != 0:
        vol(str(x))
        if text[1:] != "00":
            audio_play.append("evolou.mp3")
            vol0_99(text[1:])
    else:vol0_99(text[1:])
    
    

def vol1OO0_9999(text):
    x = int(text[0]) * 1000
    vol(str(x))
    if text[1:] != "000":
        audio_play.append("evolou.mp3")
        vol1OO_999(text[-3:])

def vol10OO0_999999(text):
    volume(text[:-3])
    audio_play.append("evol1000.mp3")
    if text[-3:] != "000":
        audio_play.append("evolou.mp3")
        volume(text[-3:])

def vol1000OO0_999999999(text):
    volume(text[:-6])
    audio_play.append("evolM.mp3")
    if text[-6:] != "000000":
        audio_play.append("evolou.mp3")
        volume(text[-6:])

def vol1000OO0000_999999999999(text):
    volume(text[:-9])
    audio_play.append("evolMilliar.mp3")
    if text[-9:] != "000000000":
        audio_play.append("evolou.mp3")
        volume(text[-9:])

def volume(text):
    x=int(text)
    if x < 10:
        vol(str(x))
    elif x < 100:
        vol0_99(str(x))
    elif x < 1000:
        vol1OO_999(str(x))
    elif x < 10000:
        vol1OO0_9999(str(x))
    elif x< 1000000:
        vol10OO0_999999(str(x))
    elif x< 1000000000:
        vol1000OO0_999999999(str(x))
    elif x< 1000000000000:
        vol1000OO0000_999999999999(str(x))

def vol_Operation(text):
    try:
        if text == "+":
            audio_play.append("evol+.mp3")
        elif text == "-":
            audio_play.append("evol-.mp3")
        elif text == "*":
            audio_play.append("evolx.mp3")
        elif text == "/":
            audio_play.append("evol%.mp3")
        elif text == "=":
            audio_play.append("evol=.mp3")
        elif text == ")":
            audio_play.append("evol).mp3")
        elif text == "(":
            audio_play.append("evol(.mp3")
        elif text == "\u00b2":
            audio_play.append("evoloss.mp3")
        elif text == "\u221a":
            audio_play.append("evolj.mp3")
        elif text == "E":
            audio_play.append("evolE.mp3")
    except Exception as e:
        print("Une erreur s'est produite :", e)

def volumeF(text):
    if text[0]=='-':
        audio_play.append("evol-.mp3")
        text=text[1:]
    if "." in text:
        x = text.split(".")
        if int(x[1])==0:
            volume(x[0])
        else:
            volume(x[0])
            audio_play.append("evolF.mp3")
            var=x[1][:9]
            i=0
            while var[i]=="0":
                audio_play.append("evol0.mp3")
                i+=1
            volume(var[i:])
    else:
        volume(text)


# Utiliser un verrou pour synchroniser l'exécution des threads
lock = threading.Lock()
def execute_thread(target, args):
    with lock:
        target(*args)

def vol_table(current, result):
    audio_sequence = []

    # Analyser la séquence pour déterminer l'ordre audio
    for element in current:
        if element in "*/+-() \u221a \u00b2":
            audio_sequence.append((vol_Operation, (element,)))
        else:
            audio_sequence.append((volumeF, (element,)))

    # Ajouter l'audio pour le résultat
    audio_sequence.append((vol_Operation, ("=",)))
    if 'E' not in result: 
        audio_sequence.append((volumeF, (result,)))
    else:
        x=result.split('E')
        x[1].replace('+','')
        audio_sequence.append((volumeF, (x[0],)))
        audio_sequence.append((vol_Operation, ("E",)))
        audio_sequence.append((volumeF, (x[1],)))
    # Démarrer et attendre les threads dans l'ordre spécifié
    for target, args in audio_sequence:
        execute_thread(target, args)



def format_scientifique(chaine):
    nombre=float(chaine)
    # Vérifier si le nombre peut être représenté en notation scientifique
    if (isinstance(nombre, (int, float))and  nombre>1000000000) or (isinstance(nombre, (int, float))and nombre>0 and nombre<0.0001):
        # Utiliser le format {:.2e} pour la notation scientifique avec 2 décimales
        chaine = "{:.2E}".format(nombre)
    
    elif (isinstance(nombre, (int, float))and  nombre<-1000000000) or (isinstance(nombre, (int, float))and nombre<0 and nombre>-0.0001):
        # Utiliser le format {:.2e} pour la notation scientifique avec 2 décimales
        chaine = "{:.2E}".format(nombre)
        
    
    return chaine


################################################################################################



# Définition des styles de police pour l'interface
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

# Définition des couleurs utilisées dans l'interface
couleur_symbole = "#0B243B"    
couleur_chiffre = "#0A1B2A"      
couleur_egal = "#16324e"
couleur_ecran = "#1f3f5e"           
couleur_label_ap = "#A9BCF5"

# Classe principale de la calculatrice
class Calculatrice:
   
    
    def on_closing(self):
       if messagebox.askokcancel("Quit", "Do you want to quit?"):
          self.window.destroy()
          stop_music()
    
    
          
    def __init__(self):
        # Création de la fenêtre principale
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.window.geometry("700x700")
        self.window.resizable(0, 0)
        self.window.title("Calculatrice")
        
        # Ajout d'une icône pour la fenêtre principale
        try:
            self.window.iconbitmap("logo.ico")
        except tk.TclError as e:
            print(f"Error loading icon: {e}")
        
        # Initialisation des variables pour les expressions
        self.total_expression = ""
        self.current_expression = ""
        self.ma_liste = []
        self.running = True

        
        # Création du cadre pour afficher les expressions
        self.display_frame = self.create_display_frame()
        
        # Création des étiquettes pour afficher les expressions
        self.total_label, self.label = self.create_display_labels()
        
        # Définition des boutons pour les chiffres et les opérations
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1),
            ')': (5, 2), '(' :(5,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.liste={"**0.5":"\u221a","**2":"\u00b2"}
        
        # Création du cadre pour les boutons
        self.buttons_frame = self.create_buttons_frame()

        # Configuration des lignes et des colonnes pour les boutons
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        
        # Création des boutons pour les chiffres et les opérations
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        
        # Liaison des touches du clavier aux fonctions correspondantes
        self.bind_keys()

    # Méthode pour lier certaines touches du clavier aux fonctions de la calculatrice
    def bind_keys(self):
        # Touche Entrée pour évaluer l'expression
        self.window.bind("<Return>", lambda event: self.evaluate())
        
        # Liaison des touches des chiffres aux méthodes pour les ajouter à l'expression en cours
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        # Liaison des touches des opérations aux méthodes pour les ajouter à l'expression en cours
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    # Méthode pour créer les boutons spéciaux (Clear, Equals, Square, Square Root)
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_backspace_button()

        self.image_path_1 = "image.png"
        self.image_path_2 = "image1.png"
        self.current_image_path = self.image_path_1  # Chemin de l'image actuelle à afficher
        self.original_image_path = None  # Chemin de l'image d'origine à conserver
        self.is_recording = False
        self.create_recorde_button()
        self.create_square_button()
        self.create_sqrt_button()

    # Méthode pour créer les étiquettes d'affichage des expressions
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=couleur_ecran ,
                               fg=couleur_label_ap, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=couleur_ecran ,
                         fg=couleur_label_ap, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    # Méthode pour créer le cadre d'affichage des expressions
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=couleur_ecran )
        frame.pack(expand=True, fill="both")
        return frame

    # Méthode pour ajouter un chiffre ou un point à l'expression en cours
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # Méthode pour créer les boutons pour les chiffres et les points
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=couleur_chiffre, fg=couleur_label_ap, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit:self.append_operator(x) if x=="(" or x==")" else self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # Méthode pour ajouter un opérateur à l'expression en cours
    def append_operator(self, operator):
        droit = 0
        operators = "+*/-()"
        if self.total_expression and len(self.total_expression) > 0:
            last_char = self.total_expression[-1]
            if last_char not in operators:
                droit = 1
        if droit==0:
                self.current_expression += operator
                self.total_expression += self.current_expression
        else:
            self.current_expression += operator
            self.total_expression = self.current_expression

        self.current_expression = ""    
        self.update_total_label()
        self.update_label()

    # Méthode pour créer les boutons pour les opérations
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=couleur_symbole, fg=couleur_label_ap, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # Méthode pour effacer l'expression en cours et l'expression totale
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.ma_liste=[]
        #self.pause_thread()
        self.update_label()
        self.update_total_label()
        stop_music()
        

    # Méthode pour créer le bouton "Clear"
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=couleur_symbole, fg=couleur_label_ap, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
    
    # Méthode pour calculer le carré de l'expression en cours
    def square(self):
        #self.current_expression = str(eval(f"{self.current_expression}**2"))
        if self.current_expression!="":
           self.current_expression = (f"{self.current_expression}\u00b2")
           self.update_label()
           if  self.total_expression[-1] not in "*+-/":
               self.total_expression=self.current_expression
        else:
            self.total_expression = (f"{self.total_expression}\u00b2")
            self.update_total_label()

        

    # Méthode pour créer le bouton "Square"
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=couleur_symbole, fg=couleur_label_ap, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # Méthode pour calculer la racine carrée de l'expression en cours
    def sqrt(self):
        #self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.current_expression=f"\u221a{self.current_expression}"
        self.update_label()
        if  self.total_expression[-1] not in "*+-/":
            self.total_expression=self.current_expression


    # Méthode pour créer le bouton "Square Root"
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=couleur_symbole, fg=couleur_label_ap, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # Méthode pour évaluer l'expression totale

    def evaluate(self):
        stop_music()
        global audio_play
        if self.total_expression=="":
            self.total_expression += self.current_expression
        elif self.total_expression[-1]in "+-/*)":
            self.total_expression += self.current_expression
        self.update_total_label()
        
        try:
            self.current_expression = str(eval(self.update_expression_pourCalculer()))
            
            
        except Exception as e:
            self.current_expression = "Error"
        finally:
            if self.current_expression != "Error":
                self.current_expression=format_scientifique(self.current_expression)
            y=self.current_expression
            self.update_label()
            self.tokenize_expression()
            x=self.ma_liste 
                
            # Clear previous audio play list
            if y != "Error":
                audio_play = []
                threading.Thread(target=vol_table,args=(x,y)).start()
                threading.Thread(target=execute_audio_sequence).start()
             

    def tokenize_expression(self):
        tokens = []
        current_token = ''

    # Parcourir chaque caractère dans l'expression
        for char in self.total_expression:
            if (char.isdigit() and char!="\u00b2")or char=='.':  # Si le caractère est un chiffre, l'ajouter au token en cours
                current_token += char
            else:
                if current_token:  # Si un token est en cours de construction, l'ajouter à la liste de tokens
                    tokens.append(current_token)
                    current_token = ''  # Réinitialiser le token en cours

                # Ajouter l'opérateur comme un token séparé
                tokens.append(char)

    # Ajouter le dernier token à la liste s'il existe
        if current_token:
            tokens.append(current_token)

        self.ma_liste=tokens 

    # Méthode pour évaluer l'expression totale
    def backspace(self):
        if self.current_expression!="":
            self.current_expression=""
            self.label.config(text="")
        else:
            current = self.total_expression
            self.total_expression=self.total_expression[:-1]
            self.total_label.config(text=current[:-1])

    # Méthode pour créer le bouton "Equals" pour évaluer l'expression
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=couleur_egal, fg=couleur_label_ap, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    
    # Méthode pour créer le bouton "backspace" pour suprimer dernier caractére
    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text='⌫', bg=couleur_egal, fg=couleur_label_ap, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.backspace)
        button.grid(row=5, column=4, sticky=tk.NSEW)
    
    
    def record(self):
        stop_music()

        # Créer un thread pour exécuter la fonction recorde
        if self.is_recording:
            print("Enregistrement déjà en cours. Mettre en pause...")
            # Mettre ici le code pour mettre en pause l'enregistrement si nécessaire
            return
        else:
           self.is_recording = True
           self.thread = threading.Thread(target=self.recorde_and_get_text)
           self.thread.start()

           
           

        

    def recorde_and_get_text(self):
        # Initialiser l'enregistreur vocal
        recognizer = sr.Recognizer()
        self.total_expression="...بدأ التسجيل الصوتي"
        self.update_total_label()
        while self.running:
            # Enregistrer le son à partir du microphone
            with sr.Microphone() as source:
                print("Dites quelque chose...")
                audio = recognizer.listen(source)
    
                # Convertir le son en texte en utilisant Google Speech Recognition
                try:
                    print("Google Speech Recognition pense que vous avez dit :")
                    text = recognizer.recognize_google(audio, language="ar-AR")
                    self.is_recording = False
                    print(text)
    
                    # Stocker le texte enregistré dans un attribut de l'instance pour y accéder plus tard si nécessaire
                    self.total_expression = text
                    # Filtrer les caractères du texte enregistré (par exemple, supprimer la ponctuation, les caractères spéciaux, etc.)
                    # Remarque : Vous devez implémenter la méthode filtrer_caracteres() en fonction de vos besoins
                    self.filtrer_caracteres()
            
                    # Évaluer le texte enregistré (par exemple, analyser le texte pour extraire des informations pertinentes)
                    # Remarque : Vous devez implémenter la méthode evaluate() en fonction de vos besoins
                    self.evaluate()
    
                
                except sr.RequestError as e:
                    print("Impossible de recevoir la réponse de Google Speech Recognition ; {0}".format(e))
                    self.total_expression="تعدر إرسال التسجيل الصوتي، تأكد من أنك متصل بالإنترنت"
                    self.update_total_label()
                except sr.UnknownValueError:
                    print("Google Speech Recognition n'a pas pu comprendre l'audio.")
                    self.total_expression="تعذر على البرنامج فهم الصوت."
                    self.update_total_label()
                finally:
                    self.is_recording = False
                    break
    
    def pause_thread(self):
        self.running = False
        self.thread.join()

    def filtrer_caracteres(self):
        replacements = {
        "جذر": "\u221a",   # square root symbol √
        "افتح القوس": "(",
        "افتح القوسين": "(",
        "افتح القوس": "(",
        "افتح": "(",
        "افتحي القوس": "(",
        "افتحي القوسين": "(",
        "افتحي": "(",
        "اغلقي القوس": ")",
        "اغلق القوس": ")",
        "اغلاق القوس": ")",
        "اغلاق القوسين": ")",
        "اغلاق": ")",
        "اغلق": ")",
        "اغلقي": ")",
        "غلق": ")",
        "اس اثنان": "\u00b2",
        "اس 2": "\u00b2"  # superscript 2
    }
        for key, value in replacements.items():
            self.total_expression = self.total_expression.replace(key, value)

        caracteres_valides = "0123456789+-x/()\u221a\u00b2"  # Définir les caractères valides
        texte_filtre = ''.join(c for c in self.total_expression if c in caracteres_valides)
        texte_filtre=texte_filtre.replace("x","*")
        self.total_expression = texte_filtre

    # Méthode pour créer le bouton "recorde"
    
    


    
    
    def create_recorde_buttonn(self):
        from PIL import Image, ImageTk
        try:
            # Charger l'image à utiliser pour le bouton
            image = Image.open("image.png")

            # Redimensionner l'image à la nouvelle taille souhaitée avec interpolation
            new_width = 100
            new_height = 50
            resized_image = image.resize((new_width, new_height), Image.BICUBIC)

            # Convertir l'image redimensionnée en format compatible avec Tkinter
            button_image = ImageTk.PhotoImage(resized_image)
        except FileNotFoundError:
            print("Fichier image non trouvé. Vérifiez le chemin spécifié.")

        # Créer le bouton avec l'image redimensionnée comme arrière-plan
        button = tk.Button(self.buttons_frame, text='', bg=couleur_egal, fg=couleur_label_ap, font=('Arial', 12),
                           borderwidth=0, image=button_image, compound=tk.CENTER, command=self.record)
        button.grid(row=5, column=3, sticky=tk.NSEW)

        # Gardez une référence à l'image pour éviter la collecte des déchets
        button.image = button_image




    

    def create_recorde_button(self):
        try:
            # Charger l'image à utiliser pour le bouton
            image = Image.open(self.image_path_1)

            # Redimensionner l'image à la nouvelle taille souhaitée avec interpolation
            new_width = 100
            new_height = 50
            resized_image = image.resize((new_width, new_height), Image.BICUBIC)

            # Convertir l'image redimensionnée en format compatible avec Tkinter
            self.button_image = ImageTk.PhotoImage(resized_image)
        except FileNotFoundError:
            print("Fichier image non trouvé. Vérifiez le chemin spécifié.")
            return

        # Créer le bouton avec l'image redimensionnée comme arrière-plan
        self.button = tk.Button(self.buttons_frame, text='',  bg=couleur_egal, fg=couleur_label_ap, font=('Arial', 12),
                                borderwidth=0, image=self.button_image, compound=tk.CENTER,
                                command=self.record)
        self.button.grid(row=5, column=3, sticky=tk.NSEW)

        # Conserver une référence à l'image pour éviter la collecte des déchets
        self.button.image = self.button_image

        # Lier les événements de clic du bouton aux fonctions correspondantes
        self.button.bind("<ButtonPress-1>", self.on_button_press)
        self.button.bind("<ButtonRelease-1>", self.on_button_release)


    def on_button_press(self, event):
        # Événement déclenché lorsque le bouton est enfoncé
        self.original_image = self.current_image_path  # Conserver l'image d'origine
        self.change_image(self.image_path_2)  # Changer l'image lors de l'enfoncement du bouton

    def on_button_release(self, event):
        # Événement déclenché lorsque le bouton est relâché
        self.change_image(self.original_image)  # Restaurer l'image d'origine

    def change_image(self, new_image_path):
        # Méthode pour changer l'image affichée sur le bouton
        try:
            image = Image.open(new_image_path)
            new_width = 100
            new_height = 50
            resized_image = image.resize((new_width, new_height), Image.BICUBIC)
            new_button_image = ImageTk.PhotoImage(resized_image)

            # Mettre à jour l'image du bouton
            self.button.configure(image=new_button_image)
            self.button.image = new_button_image  # Mettre à jour la référence à l'image

            # Mettre à jour le chemin de l'image actuelle
            self.current_image_path = new_image_path
        except FileNotFoundError:
            print(f"Fichier image {new_image_path} non trouvé. Vérifiez le chemin spécifié.")




    # Méthode pour créer le cadre des boutons
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Méthode pour mettre à jour l'étiquette d'affichage de l'expression totale
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_expression_pourCalculer(self):
        expression = self.total_expression
        import re

        def rearrange_expression(expression):
            # Utilisation d'expressions régulières pour identifier les motifs dans l'expression
            pattern = r'√(?:\d+|\([^)]+\))'
            
            # Fonction de remplacement pour la réorganisation
            def repl(match):
                matched = match.group(0)
                if matched.startswith('√('):
                    return matched.replace('√(', '(') + '√'
                else:
                    return matched[1:] + '√'
            
            # Utilisation de re.sub pour remplacer les correspondances par les nouvelles valeurs
            rearranged_expression = re.sub(pattern, repl, expression)
            return rearranged_expression
        expression=rearrange_expression(expression)
        for operator, symbol in self.liste.items():
            expression = expression.replace(symbol, f'{operator}')
        return expression
    # Méthode pour mettre à jour l'étiquette d'affichage de l'expression en cours
    def update_label(self):
        self.label.config(text=self.current_expression[:12])
        if self.current_expression=="Error":
            self.current_expression=""
            self.total_expression=""
            self.update_total_label()

    # Méthode pour lancer la boucle principale de l'interface graphique
    def run(self):
        self.window.mainloop()

# Point d'entrée du programme
if __name__ == "__main__":
    calc = Calculatrice()
    calc.run()
    print(calc.ma_liste)
    

