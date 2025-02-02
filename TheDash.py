#!/usr/bin/env python3
import time
import random
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------- Quiz Data -----------------------
# Each question is stored as a dictionary with the question text,
# three answer options (keys "a", "b", "c"), and the correct answer's key.
questions = [
    {"question": "Who was the first democratically elected leader of the Russian Federation?",
     "a": "A: Boris Johnson", "b": "B: Boris Yeltsin", "c": "C: Mikhail Gorbachev", "correct": "b"},
    {"question": "What was the first Carry On film ever made?",
     "a": "A: Carry On Sergeant", "b": "B: Carry On Cleo", "c": "C: Carry On Doctor", "correct": "a"},
    {"question": "Why did Tibetans grow long finger nails?",
     "a": "A: They're attention seekers.", "b": "B: To pick noses efficiently.", "c": "C: To scratch their back.", "correct": "c"},
    {"question": "Who signed the Magna Carta?",
     "a": "A: Henry III", "b": "B: King John I", "c": "C: Richard I", "correct": "b"},
    {"question": "What sport was Fanny Chmelar recognized for competing in?",
     "a": "A: Long Jump", "b": "B: Show Jumping", "c": "C: Ski-ing", "correct": "c"},
    {"question": "Which of these North Korean dictators ruled first?",
     "a": "A: Kim Il-Sung", "b": "B: Kim Jong-Un", "c": "C: Kim Jong-Il", "correct": "a"},
    {"question": "What was Shaun Ryder's autobiography called?",
     "a": "A: Twisting My Plums", "b": "B: Twisting My Melon", "c": "C: Twisting My Ankle", "correct": "b"},
    {"question": "Bartolomeo Cristofori invented what?",
     "a": "A: The Car", "b": "B: The Piano", "c": "C: The Trumpet", "correct": "b"},
    # Additional questions:
    {"question": "Which planet is known as the Red Planet?",
     "a": "A: Venus", "b": "B: Mars", "c": "C: Jupiter", "correct": "b"},
    {"question": "What is the capital of Australia?",
     "a": "A: Sydney", "b": "B: Canberra", "c": "C: Melbourne", "correct": "b"}
]

# Shuffle questions for a randomized order
random.shuffle(questions)

# ----------------------- Quiz Application -----------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Quiz")
        self.root.resizable(False, False)
        self.score = 0
        self.current_q_index = 0
        self.total_questions = len(questions)
        self.time_per_question = 15  # seconds
        self.remaining_time = self.time_per_question
        self.timer_id = None

        # Create frames
        self.question_frame = tk.Frame(root, padx=20, pady=20)
        self.question_frame.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root, padx=20, pady=10)
        self.button_frame.pack(fill=tk.X)

        self.status_frame = tk.Frame(root, padx=20, pady=10)
        self.status_frame.pack(fill=tk.X)

        # Question label
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14), wraplength=500, justify="left")
        self.question_label.pack(anchor="w")

        # Answer buttons (stored in a dictionary for ease of use)
        self.answer_buttons = {}
        for key in ["a", "b", "c"]:
            btn = tk.Button(self.button_frame, text="", font=("Arial", 12), width=40,
                            command=lambda k=key: self.check_answer(k))
            btn.pack(pady=5)
            self.answer_buttons[key] = btn

        # Timer and Score label
        self.timer_label = tk.Label(self.status_frame, text="Time: --", font=("Arial", 12))
        self.timer_label.pack(side=tk.LEFT, padx=(0, 20))
        self.score_label = tk.Label(self.status_frame, text=f"Score: {self.score}/{self.total_questions}", font=("Arial", 12))
        self.score_label.pack(side=tk.LEFT)

        # Start the quiz
        self.display_question()

    def display_question(self):
        # Cancel any existing timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.remaining_time = self.time_per_question
        self.update_timer()

        if self.current_q_index < self.total_questions:
            current_q = questions[self.current_q_index]
            self.question_label.config(text=f"Q{self.current_q_index + 1}: {current_q['question']}")
            # Set text for each answer button
            for key in ["a", "b", "c"]:
                self.answer_buttons[key].config(text=current_q[key], state=tk.NORMAL, bg="SystemButtonFace")
        else:
            self.end_quiz()

    def update_timer(self):
        self.timer_label.config(text=f"Time: {self.remaining_time} sec")
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            # Time's up; treat as incorrect answer and move on
            self.check_answer(None)

    def check_answer(self, selected):
        # Disable buttons to prevent multiple answers
        for btn in self.answer_buttons.values():
            btn.config(state=tk.DISABLED)

        current_q = questions[self.current_q_index]
        correct = current_q.get("correct")
        # Highlight the correct answer in green, wrong in red
        for key, btn in self.answer_buttons.items():
            if key == correct:
                btn.config(bg="green")
            elif key == selected:
                btn.config(bg="red")
        if selected == correct:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
        self.current_q_index += 1
        # Wait a moment before displaying next question
        self.root.after(1500, self.display_question)

    def end_quiz(self):
        # Cancel timer if running
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        # Clear frames and display final score and a "Play Again" button
        for widget in self.root.winfo_children():
            widget.destroy()
        end_frame = tk.Frame(self.root, padx=20, pady=20)
        end_frame.pack()
        final_msg = tk.Label(end_frame, text=f"Quiz Over! Your Score: {self.score} out of {self.total_questions}",
                              font=("Arial", 16))
        final_msg.pack(pady=20)
        play_again = tk.Button(end_frame, text="Play Again", font=("Arial", 14), command=self.restart_quiz)
        play_again.pack(pady=10)
        exit_btn = tk.Button(end_frame, text="Exit", font=("Arial", 14), command=self.root.quit)
        exit_btn.pack(pady=10)

    def restart_quiz(self):
        # Reset quiz parameters and reshuffle questions
        self.score = 0
        self.current_q_index = 0
        random.shuffle(questions)
        for widget in self.root.winfo_children():
            widget.destroy()
        # Rebuild the quiz interface
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.iconbitmap('favicon.ico')  # Replace with your icon file path if available
    root.mainloop()
