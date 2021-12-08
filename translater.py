from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

root = Tk()
root.title("Google_translater")
root.geometry('1040x350')
language = googletrans.LANGUAGES
#print(language)
language_= list(language.values())
lang1= language.keys()

#labelchange definició
def labelchange():
    c=combobox1.get()
    c1=combobox2.get()
    label1.configure(text= c)
    label2.configure(text= c1)
    root.after(1000, labelchange)


#translate definíció
def translate():
    global language
    global words
    global language
    global c2
    global e
    try:
        text_= text1.get(1.0,END)
        c2= combobox1.get()
        c3= combobox2.get()
        if (text_):
            words= textblob.TextBlob(text_)
            lan= words.detect_language()
            for i, n in language.items():
                if (n == c3):
                    lan_=i
            words = words.translate(from_lang= lan, to = str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror('googletrans', 'please try again')


#comboboxes

combobox1 = ttk.Combobox(root, values =language_, font= 'times 10 bold ', state= 'r')
combobox1.place(x=140, y= 20)
combobox1.set('english')

combobox2 = ttk.Combobox(root, values =language_, font= 'times 10 bold ', state= 'r')
combobox2.place(x=785, y= 20)
combobox2.set('english')

#labels
label1= Label(root, text= 'english', font= 'segoe 30 bold', bg="grey", width= 18, bd = 5, relief=GROOVE )
label1.place(x=0, y= 50)

label2= Label(root, text= 'english', font= 'segoe 30 bold', bg="grey", width= 18, bd = 5, relief=GROOVE )
label2.place(x=600, y= 50)

#frames
frame1 =Frame(root, bg='black' , bd =5)
frame1.place(x= 14, y = 118, width = 410, height = 210)

frame2 =Frame(root, bg='black' , bd =5)
frame2.place(x= 600, y = 118, width = 410, height = 210)

#textboxes
text1 = Text(frame1, font = 'times 20 bold ', bg= 'white', relief = GROOVE, wrap= WORD)
text1.place(x= 0, y=0 , width = 400, height= 200)

text2 = Text(frame2, font = 'times 20 bold ', bg= 'white', relief = GROOVE, wrap= WORD, fg='green')
text2.place(x= 0, y=0 , width = 400, height= 200)


#scrollbars
scrollbar1= Scrollbar(frame2)
scrollbar1.pack(side= 'right', fill='y')
scrollbar1.configure(command= text1.yview)
text1.configure(yscrollcommand= scrollbar1.set)

scrollbar2= Scrollbar(frame2)
scrollbar2.pack(side= 'right', fill='y')
scrollbar2.configure(command= text2.yview)
text2.configure(yscrollcommand= scrollbar2.set)


#transaterbutton
transbutton= Button(root, text= 'TRANSLATE', font= 'Immpact 15 bold', activebackground = "grey", cursor= 'hand2', bd= 5, bg= "red", fg ='white', command=translate )
transbutton.place(x=440, y =250)

labelchange()

root.configure(bg='blue')
root.mainloop()