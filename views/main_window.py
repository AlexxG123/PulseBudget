# views/main_window.py
import customtkinter as ctk

# Configure the appearance (dark theme looks great)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):
    """Main window for Pulse Budget - Day 1 Setup"""
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Pulse Budget - Personal Finance Tracker")
        self.geometry("700x500")
        self.minsize(600, 400)

        # Grid configuration (1 column, 3 rows)
        self.grid_rowconfigure(0, weight=1)  # Top space
        self.grid_rowconfigure(1, weight=0)  # Center label
        self.grid_rowconfigure(2, weight=1)  # Bottom space
        self.grid_columnconfigure(0, weight=1)

        # Main welcome label
        self.label = ctk.CTkLabel(
            self,
            text="Welcome to Pulse Budget\n\nYour personal finance tracker.\n\n(Day 1 - Environment Ready)",
            font=("Arial", 24, "bold"),
            justify="center"
        )
        self.label.grid(row=1, column=0, padx=20, pady=20)

        # Footer label with version
        self.footer = ctk.CTkLabel(
            self,
            text="📊 Python 3.x | CustomTkinter | Ready for Sprint 1",
            font=("Arial", 12),
            text_color="gray"
        )
        self.footer.grid(row=2, column=0, pady=(0, 20))

if __name__ == "__main__":
    # This allows testing the window independently
    app = MainWindow()
    app.mainloop()