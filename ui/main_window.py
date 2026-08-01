import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chrome Profile Manager")
        self.geometry("1000x650")
        self.minsize(900, 600)

        # Header
        title = ctk.CTkLabel(
            self,
            text="Chrome Profile Manager",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        # Search
        self.search = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Search Profile..."
        )
        self.search.pack(pady=10)

        # Table Frame
        self.table = ctk.CTkScrollableFrame(self, width=900, height=420)
        self.table.pack(padx=20, pady=10, fill="both", expand=True)

        # Header Row
        headers = ["Profile", "Status", "Action"]
        for col, text in enumerate(headers):
            lbl = ctk.CTkLabel(
                self.table,
                text=text,
                font=("Arial", 14, "bold")
            )
            lbl.grid(row=0, column=col, padx=20, pady=10)

        # Demo Data
        for i in range(1, 6):
            ctk.CTkLabel(
                self.table,
                text=f"Profile {i:03}"
            ).grid(row=i, column=0, padx=20, pady=8)

            ctk.CTkLabel(
                self.table,
                text="Ready"
            ).grid(row=i, column=1)

            ctk.CTkButton(
                self.table,
                text="Open",
                width=80
            ).grid(row=i, column=2)
