import tkinter as tk
import time
import random

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Typing Test")
        self.master.geometry("400x400")
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "The five boxing wizards jump quickly.",
            "How vexingly quick daft zebras jump!",
            "Jaded zombies acted quaintly but kept driving their oxen forward.",
            "The quick onyx goblin jumps over the lazy dwarf.",
            "The jay, pig, fox, zebra, and my wolves quack!",
            "Waltz, nymph, for quick jigs vex Bud.",
            "Two driven jocks help fax my big quiz.",
            "Fickle jinx bog dwarves spy math quiz.",
            "Pack my box with five dozen liquor jugs."
        ]
        
        self.instructions_label = tk.Label(self.master, text="Type the following sentence as quickly and accurately as possible:")
        self.instructions_label.pack(pady=10)
        
        self.sentence_label = tk.Label(self.master, text="")
        self.sentence_label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_test)
        self.start_button.pack()
        
    def start_test(self):
        self.current_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.current_sentence)
        self.start_time = time.time()
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.entry.bind('<Return>', self.end_test)
        self.start_button.config(state="disabled")
        
    def end_test(self, event):
        self.end_time = time.time()
        self.entry.config(state="disabled")
        self.entry.unbind('<Return>')
        self.accuracy = self.calculate_accuracy()
        self.time_taken = self.end_time - self.start_time
        self.display_results()
        
    def calculate_accuracy(self):
        user_input = self.entry.get()
        correct_chars = 0
        for i in range(len(user_input)):
            if i >= len(self.current_sentence) or user_input[i] != self.current_sentence[i]:
                break
            correct_chars += 1
        accuracy = correct_chars / len(self.current_sentence)
        return accuracy * 100
        
    def display_results(self):
        self.instructions_label.config(text=f"Time taken: {self.time_taken:.2f} seconds\nAccuracy: {self.accuracy:.2f}%")
        self.start_button.config(text="Restart", state="normal", command=self.restart_test)
        
    def restart_test(self):
        self.instructions_label.config(text="Type the following sentence as quickly and accurately as possible:")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.start_button.config(text="Start", state="normal", command=self.start_test)
        
root = tk.Tk()
speed_typing_test = SpeedTypingTest(root)
root.mainloop()