from nltk.tokenize import word_tokenize
import string
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import os


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        return "Négative Sentiment"
    elif score['neg'] < score['pos']:
        return "Positive Sentiment"
    else:
        return "Neutral Sentiment"


df = pd.read_json('data.json')
marq = df['brand'][0]

ls = dict()
ls['com'] = []
for s in df['commentaire']:
    ls['com'].append(s.lower())
df['commentaire_lower'] = ls['com']

ls = dict()
ls['com1'] = []
for s in df['commentaire_lower']:
    ls['com1'].append(s.translate(str.maketrans('', '', string.punctuation)))
df['commentaire_Cleaned'] = ls['com1']

for s in df.index:
    tokenized_words = word_tokenize(str(df['commentaire_Cleaned'][s]), "french")

ls = dict()
ls['com2'] = []
for s in df.index:
    ls['com2'].append(sentiment_analyse(str(df['commentaire_Cleaned'][s])))
df['Classification'] = ls['com2']

negative = 0
positive = 0
neutre = 0

for s in df.index:
    if (str(df['Classification'][s])) == "Négative Sentiment":
        negative = negative + 1

    if (str(df['Classification'][s])) == "Positive Sentiment":
        positive = positive + 1
    if (str(df['Classification'][s])) == "Neutral Sentiment":
        neutre = neutre + 1
print("negative=", negative, "positive=", positive, "neutre=", neutre)

# Window
win = Tk()
win.state('zoomed')
win.configure(bg="#99CCFF")
win.title("Les résultats sont là !")

ttk.Label(win, text="Résultats de l'analyse des données obtenues pour la marque :", font='Calibri 20', background="#99CCFF").pack(pady=5)
ttk.Label(win, text=marq, font='Calibri 20', background="#99CCFF", foreground="#170FFF").pack(pady=5)

# Figure
fig, ax = plt.subplots()
fig.set_facecolor("#99CCFF")
ax.axis("equal")
ax.pie([negative, positive, neutre], labels=["Commentaires négatifs", "Commentaires positifs", "Commentaires neutres"], autopct='%1.1f%%')

canvas = FigureCanvasTkAgg(fig, master=win)
canvas.draw()
canvas.get_tk_widget().pack(pady=0)


def accueil():
    win.quit()
    win.destroy()
    os.system("python first_page.py")


def quitter():
    win.quit()


Button(win, text="Accueil", width=10, bg='#99CCFF', font='Calibri 20', fg="#000033", activebackground="#5e8ebf", command=accueil).pack(pady=5)
Button(win, text="Quitter", width=10, bg='#99CCFF', font='Calibri 20', fg="#000033", activebackground="#5e8ebf", command=quitter).pack(pady=5)
win.mainloop()
