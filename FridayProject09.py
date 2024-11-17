import openai
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import scrolledtext

def configure():
    load_dotenv()

# Configure environment variables
configure()

# Set your OpenAI API key <------- DO NOT ENTER API Key here
openai.api_key = os.getenv('api_key')

#User testing API Key  <------------ Please enter 
openai.api_key = ('Please Enter your API key here')

# Function to get the AI response
def get_response():
    user_prompt = user_input.get("1.0", tk.END).strip()  # Get the user input
    if not user_prompt:
        output_box.insert(tk.END, "Please enter a prompt.\n")
        return

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )
        # Display the response in the output box
        assistant_response = response["choices"][0]["message"]["content"].strip()
        output_box.insert(tk.END, f"User: {user_prompt}\nAssistant: {assistant_response}\n\n")
    except Exception as e:
        output_box.insert(tk.END, f"Error: {e}\n")

# Function to clear all text from input and output boxes
def clear_all():
    user_input.delete("1.0", tk.END)  # Clear user input box
    output_box.delete("1.0", tk.END)  # Clear output box

# Create the main Tkinter window
window = tk.Tk()
window.title("ChatGPT GUI")

# Input box for the user's prompt
tk.Label(window, text="Enter your prompt:").pack(pady=5)
user_input = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10)
user_input.pack(pady=5)

# Submit button
submit_button = tk.Button(window, text="Submit", command=get_response)
submit_button.pack(pady=5)

# Clear All button
clear_button = tk.Button(window, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

# Output box for the assistant's response
tk.Label(window, text="Response:").pack(pady=5)
output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15, state=tk.NORMAL)
output_box.pack(pady=5)

# Start the Tkinter main loop
window.mainloop()
