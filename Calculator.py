import tkinter as tk

class StylishCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Stylish Calculator")
        self.root.geometry("360x470")
        self.root.resizable(False, False)
        self.expression = ""

        # Colors and Fonts
        self.bg_color = "#1e1e2f"
        self.btn_color = "#32324a"
        self.op_color = "#ff9f43"
        self.eq_color = "#32ff7e"
        self.clear_color = "#ff5e57"
        self.text_color = "#ffffff"
        self.font = ("Consolas", 20)

        self.root.config(bg=self.bg_color)

        # Display Label
        self.display_var = tk.StringVar()
        self.display_label = tk.Label(
            root, textvariable=self.display_var, font=("Consolas", 24),
            bg="#2d2d44", fg="#00ffcc", relief="sunken", height=2,
            anchor='e', padx=10
        )
        self.display_label.pack(fill='both', padx=15, pady=(20, 10))

        # Buttons
        btns_frame = tk.Frame(self.root, bg=self.bg_color)
        btns_frame.pack(expand=True, fill="both", padx=15)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame, bg=self.bg_color)
            row_frame.pack(expand=True, fill='both', pady=3)
            for btn_text in row:
                bg = self.btn_color
                if btn_text in "+-*/":
                    bg = self.op_color
                elif btn_text == "=":
                    bg = self.eq_color
                elif btn_text == "C":
                    bg = self.clear_color

                btn = tk.Button(
                    row_frame, text=btn_text, font=self.font, bg=bg,
                    fg=self.text_color, activebackground="#444",
                    relief='flat', bd=0,
                    command=lambda txt=btn_text: self.on_button_click(txt)
                )
                btn.pack(side='left', expand=True, fill='both', padx=3)

        # Result
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(
            root, textvariable=self.result_var, font=("Consolas", 16),
            bg=self.bg_color, fg="#32ff7e"
        )
        self.result_label.pack(pady=(5, 10))

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
            self.result_var.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.result_var.set(f"{self.expression} = {result}")
                self.display_var.set(result)
                self.expression = result
            except ZeroDivisionError:
                self.result_var.set("Error: Division by 0")
                self.display_var.set("Error")
                self.expression = ""
            except:
                self.result_var.set("Invalid Expression")
                self.display_var.set("Error")
                self.expression = ""
        else:
            self.expression += char
            self.display_var.set(self.expression)

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = StylishCalculator(root)
    root.mainloop()
