import tkinter as tk
import random

# Đọc danh sách từ và định nghĩa từ file txt
def load_words_and_definitions(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            word_def_pairs = [line.strip().split(':') for line in lines]
            return word_def_pairs
    except FileNotFoundError:
        return []

# Tạo giao diện và chức năng hiển thị từ và định nghĩa
class FlashcardApp:
    def __init__(self, master, word_def_pairs):
        self.master = master
        self.word_def_pairs = word_def_pairs
        random.shuffle(self.word_def_pairs)  # Trộn lẫn danh sách từ và định nghĩa
        self.index = 0  # Chỉ số hiện tại của từ và định nghĩa

        self.master.title("Flashcard App")
        self.master.geometry("600x600+{}+{}".format(int(master.winfo_screenwidth()/2 - 200), 
                                             int(master.winfo_screenheight()/2 - 400)))

        self.flashcard = tk.Label(master, text="", font=("Arial", 50), wraplength=500)
        self.flashcard.pack(pady=20)

        self.definition_label = tk.Label(master, text="", font=("Arial", 20), wraplength=500)
        self.definition_label.pack(pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.BOTTOM, pady=10)

        # Đặt các nút vào trong khung
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_word)
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.show_def_button = tk.Button(self.button_frame, text="Show Definition", command=self.show_definition)
        self.show_def_button.pack(side=tk.RIGHT, padx=10)


        self.show_next_word()

    def show_next_word(self):
        if self.index < len(self.word_def_pairs):
            self.current_word, self.current_definition = self.word_def_pairs[self.index]
            self.flashcard.config(text=self.current_word)
            self.definition_label.config(text="")
            self.index += 1
        else:
            self.flashcard.config(text="End of list")
            self.definition_label.config(text="")

    def show_definition(self):
        self.definition_label.config(text=self.current_definition)

# Khởi tạo ứng dụng
def run_app(word_file):
    word_def_pairs = load_words_and_definitions(word_file)
    root = tk.Tk()
    app = FlashcardApp(root, word_def_pairs)
    root.mainloop()

# Tên file chứa danh sách từ và định nghĩa
word_file = 'vocab.txt'
run_app(word_file)
