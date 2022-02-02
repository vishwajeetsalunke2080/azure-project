
from calendar import c
from datetime import datetime
import os
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Button, Tk, messagebox, ttk
from tkinter import *
from tkinter import *
import webbrowser

from matplotlib.pyplot import text

class design:
    def translate():
        
        import requests, uuid, json
        subscription_key = "<your subscription id here>"
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "centralus"
        path = '/translate'
        constructed_url = endpoint + path
        src=source_lang.current()
        source = gtts[src]
        params = {
            'api-version': '3.0',
            'to': source
        }

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': user_input_textbox.get('1.0',END)
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        output = response[0]['translations'][0]['text']
        user_output_textbox.delete(1.0,END)
        user_output_textbox.insert(1.0,""+output) 

    def open_file():
        try:
            file = askopenfilename(defaultextension=".txt", 
                              filetypes=[("Text Documents",".txt")])  
            if file == "":   
                file = None
            else: 
                root.title("Microsoft Translate - "+os.path.basename(file)) 
                user_input_textbox.delete(1.0,END)   
                file = open(file,"r") 
                user_input_textbox.insert(1.0,file.read())   
                file.close()
        except Exception as e:
            messagebox.showerror("Error!",e)
    def save_file():
        try:
            file = asksaveasfilename(defaultextension=".*", 
                              filetypes=[("Text Document",".txt"),("All Files",".*")])  
         
            root.title("Microsoft Translate") 
            inp=user_input_textbox.get(1.0,END)   
            op=user_output_textbox.get(1.0,END)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M %p")
            L=["\n",dt_string+"\n","Text to be translated","\n\t"+inp,"Translation","\n\t"+op]
            file = open(file,"a",encoding='utf-8') 
            file.writelines(L)
            file.close()

        except Exception as e:
            messagebox.showerror("Error!",e)
    def speak_output():
        import os
        from googletrans import Translator
        from gtts import gTTS
        from playsound import playsound
        try:
            translator=Translator()
            a=user_output_textbox.get(1.0,END)
            x=translator.detect(a)
            dest = x.lang
            myobj = gTTS(text=a, lang=dest, slow=False)
            myobj.save("welcome.mp3")
            playsound("welcome.mp3")
            os.remove('welcome.mp3')
        except Exception as e:
            messagebox.showerror("Error!",e)

    def speak_input():
        import os
        from googletrans import Translator
        from gtts import gTTS
        from playsound import playsound
        try:
            translator=Translator()
            a = user_input_textbox.get(1.0,END)
            x=translator.detect(a)
            dest= x.lang
            myobj = gTTS(text=a, lang=dest, slow=False)
            myobj.save("welcome.mp3")
            playsound("welcome.mp3")
            os.remove('welcome.mp3')
            
        except Exception as e:
            messagebox.showerror("Error!",e)
    def swap():
        init = user_output_textbox.get(1.0,END)
        dest = user_input_textbox.get(1.0,END)
        user_input_textbox.insert(1.0,init)
        user_output_textbox.insert(1.0,dest)
    
    def support():
        webbrowser.open_new_tab("mailto:salunkevishwajeet577@gmail.com")
    def social():
        webbrowser.open_new_tab("https://www.instagram.com/vishwajeet_salunke/")
    

  

root = Tk()
root.iconphoto(False,PhotoImage(file='microsoft.png'))
root.geometry('780x250')
root.title('Microsoft Translator')

menubar = Menu(root)
file = Menu(menubar,tearoff=0)
help = Menu(menubar,tearoff=0)     

menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="Help",menu=help)

file.add_command(label="open",command=design.open_file)
file.add_command(label="save",command=design.save_file)
file.add_separator()
file.add_command(label="exit",command=root.destroy)

help.add_command(label="Contact",command=design.support)
help.add_command(label="Follow",command=design.social)

root.config(menu=menubar)

user_input_textbox = Text(root,width=50,height=5,font=('calbri',10))
user_input_textbox.grid(row=1,column=0,padx=10,pady=3)

user_output_textbox = Text(root,width=50,height=5,font=('calbri',10))
user_output_textbox.grid(row=1,column=1,padx=20,pady=3)

user_input_textbox.insert('1.0',"Enter Text...")
user_output_textbox.insert('1.0',"Translation...")

translate_button = Button(root,text='Translate',command=design.translate)
translate_button.place(x=390,y=170)

image_swp = PhotoImage(file='swapico.png')
swap_btn = Button(root,text="swap",image=image_swp,command=design.swap)
swap_btn.place(x=330,y=170)

myico = PhotoImage(file='speaker.png')
speaker_1 = Button(root,text="speak",image=myico,command=design.speak_input)
speaker_1.grid(row=4,column=0,sticky=W,padx=10)

speaker_2 = Button(root,text="speak",image=myico,command=design.speak_output)
speaker_2.grid(row=4,column=1,sticky=E,padx=20,pady=20)

n = tkinter.StringVar()
source_lang = ttk.Combobox(root,width=15,text=n)
source_lang['values']=('Afrikaans', 'Arabic', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Welsh',
                        'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Finnish', 'French',
                        'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian',
                        'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Malayalam',
                        'Marathi', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala',
                        'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai',
                        'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese')
source_lang.grid(column=0,row=0,sticky=W,padx=10,pady=20)
source_lang.set("Hindi")
gtts = ['af', 'ar', 'bn', 'bs', 'ca', 'cs', 'cy', 'da',
        'de', 'el', 'en', 'eo', 'es', 'et', 'fi', 'fr', 'gu', 'hi',
        'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'km', 'kn',
        'ko', 'la', 'lv', 'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pl',
        'pt', 'ro', 'ru', 'si', 'sk', 'sq', 'sr', 'su', 'sv', 'sw',
        'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi']
    
    


root.mainloop()
        
        
   
    

