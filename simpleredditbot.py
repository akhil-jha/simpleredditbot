from tkinter import *
import pymysql
import praw
import re

reddit = praw.Reddit(client_id='jdJX--A6fdmztQ',
                     client_secret="4HUtWuOyvxqWbdYt0Tp2lzM6Iik", password=input("Enter password: "),
                     user_agent='PyEng Bot 1.0', username=input("Enter username"))

db = pymysql.connect("localhost", "root", "redhat", "bot")
cursor = db.cursor()


v1 = ''
v2 = ''
root = Tk()
root.title('BotBox')

label_1 = Label(root, text="Enter the Subreddit Name: ", font=("arial", 16, "bold"), fg="black")
search = StringVar()
entry_1 = Entry(root, textvariable=search)
label_1.grid(row=0)
entry_1.grid(row=0, column=2)


def val1():
    global v1
    v1 = str(search.get())


button1 = Button(text="Search", font=("arial", 12, "bold"), fg="black", command=val1)
button1.grid(row=0, column=3)

label_2 = Label(root, text="Enter the keyword to search: ", font=("arial", 16, "bold"), fg="black")
submit = StringVar()
entry_2 = Entry(root, textvariable=submit)
label_2.grid(row=2)
entry_2.grid(row=2, column=2)


def val2():
    global v2
    v2 = str(submit.get())


button2 = Button(text="Submit", font=("arial", 12, "bold"), fg="black", command=val2)
button2.grid(row=2, column=3)

root.mainloop()
subreddit = reddit.subreddit(v1)

for comment in subreddit.stream.comments():
    if re.search(v2, comment.body, re.IGNORECASE):
        author=str(comment.author)
        body=str(comment.body)
        print(author, body)
        cursor.execute("INSERT INTO bot(name,body) VALUES (%s,%s)", (author, body))
        db.commit()

db.close()