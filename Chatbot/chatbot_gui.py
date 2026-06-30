import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from faq_chatbot import get_response
def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return
    chat_area.insert(tk.END, "You: " + user_message + "\n")
    bot_response = get_response(user_message)
    chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n")
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x500")
chat_area = ScrolledText(root, width=70, height=20)
chat_area.pack(padx=10, pady=10)
frame = tk.Frame(root)
frame.pack(pady=10)
entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5)
send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)
root.mainloop()
