import tkinter as tk
from tkinter import messagebox
from hugchat import hugchat

# Function to initialize the chatbot
def initialize_chatbot():
    cookie_path = r"E:\Project soil\huggingface.co.json"
    try:
        chatbot = hugchat.ChatBot(cookie_path=cookie_path)
        chatbot.switch_llm(6)
        return chatbot
    except FileNotFoundError:
        messagebox.showerror("Error", "The authentication cookie file is missing.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
    return None

# Function to fetch soil details using the chatbot
def get_soil_info(chatbot, soil):
    if not chatbot:
        messagebox.showerror("Error", "ChatBot initialization failed.")
        return None

    try:
        conversation_id = chatbot.new_conversation()
        chatbot.change_conversation(conversation_id)
        prompt = f"detailed information on Minerals present, crops supported, maintainence cost and ways to keep {soil.lower()} fertile in india. Must include all factors mentioned. Keep the language simple and understandable and include the costs in the maintainence factor with respect to latest indian market prices."
        response = chatbot.chat(prompt)
        
        if response:
            return response
        else:
            return "No response received."
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
        return None

# Function to handle the 'Submit' button click
def submit_query():
    soil = soil_entry.get().strip()
    if not soil:
        messagebox.showwarning("Input Required", "Please enter a soil name.")
        return
    
    response = get_soil_info(chatbot, soil)
    if response:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, response)

# Initialize chatbot once
chatbot = initialize_chatbot()

# Setting up the GUI
root = tk.Tk()
root.title("Soil Information Chatbot")
root.geometry("800x600")
root.resizable(True, True)

# Soil input label and entry field
soil_label = tk.Label(root, text="Enter Soil Name:")
soil_label.pack(pady=10)

soil_entry = tk.Entry(root, width=50)
soil_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Get Soil Info", command=submit_query)
submit_button.pack(pady=10)

# Result display text area
result_text = tk.Text(root, wrap="word", width=90, height=20)
result_text.pack(pady=10)

# Start the main loop
root.mainloop()
