import customtkinter as ctk
from datetime import datetime
from services.data_service import DataService

ctk.set_appearance_mode("Dark")

class PulseBudgetPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service = DataService()

        # Window setup
        self.title("Pulse Budget — Personal Finance Tracker (Pro)")
        self.geometry("1100x680")
        self.configure(fg_color="#0B0F1A")

        # Layout: Left Panel (Form) / Right Panel (Summary, Analytics, Table)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self._build_ui()

    def _build_ui(self):
        # ==========================================
        # LEFT PANEL: ENTRY FORM
        # ==========================================
        self.frm_entry = ctk.CTkFrame(self, fg_color="#131A2A", corner_radius=12)
        self.frm_entry.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        lbl_title = ctk.CTkLabel(
            self.frm_entry, text="New Movement", font=("Segoe UI", 18, "bold"), text_color="#22D3EE"
        )
        lbl_title.pack(padx=15, pady=(20, 15), anchor="w")

        # Fields
        ctk.CTkLabel(self.frm_entry, text="Date", text_color="#8A9BB4").pack(padx=15, anchor="w")
        self.txtDate = ctk.CTkEntry(self.frm_entry, placeholder_text="YYYY-MM-DD", fg_color="#0B0F1A")
        self.txtDate.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.txtDate.pack(padx=15, pady=(0, 10), fill="x")

        ctk.CTkLabel(self.frm_entry, text="Description", text_color="#8A9BB4").pack(padx=15, anchor="w")
        self.txtDescription = ctk.CTkEntry(self.frm_entry, placeholder_text="e.g. Salary, Groceries", fg_color="#0B0F1A")
        self.txtDescription.pack(padx=15, pady=(0, 10), fill="x")

        ctk.CTkLabel(self.frm_entry, text="Category", text_color="#8A9BB4").pack(padx=15, anchor="w")
        self.cmbCategory = ctk.CTkOptionMenu(
            self.frm_entry, 
            values=["Food", "Utilities", "Salary", "Entertainment", "Transport", "Other"],
            fg_color="#0B0F1A", button_color="#22D3EE"
        )
        self.cmbCategory.pack(padx=15, pady=(0, 10), fill="x")

        ctk.CTkLabel(self.frm_entry, text="Amount (US$)", text_color="#8A9BB4").pack(padx=15, anchor="w")
        self.txtAmount = ctk.CTkEntry(self.frm_entry, placeholder_text="e.g. 50.00", fg_color="#0B0F1A")
        self.txtAmount.pack(padx=15, pady=(0, 10), fill="x")

        ctk.CTkLabel(self.frm_entry, text="Type", text_color="#8A9BB4").pack(padx=15, anchor="w")
        self.cmbKind = ctk.CTkOptionMenu(
            self.frm_entry, values=["Expense", "Income"], fg_color="#0B0F1A", button_color="#22D3EE"
        )
        self.cmbKind.pack(padx=15, pady=(0, 15), fill="x")

        # Action Buttons
        self.btnAdd = ctk.CTkButton(
            self.frm_entry, text="Add Transaction", fg_color="#22D3EE", text_color="#04121A",
            hover_color="#18A3B8", font=("Segoe UI", 13, "bold"), command=self._on_add
        )
        self.btnAdd.pack(padx=15, pady=5, fill="x")

        self.btnClear = ctk.CTkButton(
            self.frm_entry, text="Clear Form", fg_color="transparent", border_width=1,
            border_color="#8A9BB4", text_color="#8A9BB4", command=self._clear_form
        )
        self.btnClear.pack(padx=15, pady=5, fill="x")

        self.lblStatus = ctk.CTkLabel(self.frm_entry, text="", text_color="#FB7185", font=("Segoe UI", 11), wraplength=200)
        self.lblStatus.pack(padx=15, pady=10)

        # ==========================================
        # RIGHT PANEL: DASHBOARD & TABLE
        # ==========================================
        self.frm_right = ctk.CTkFrame(self, fg_color="transparent")
        self.frm_right.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")
        self.frm_right.grid_rowconfigure(2, weight=1)
        self.frm_right.grid_columnconfigure(0, weight=1)

        # 1. Summary Header
        self.frm_summary = ctk.CTkFrame(self.frm_right, fg_color="#131A2A", corner_radius=12)
        self.frm_summary.grid(row=0, column=0, pady=(0, 10), sticky="ew")

        # Smart Health Panel
        self.frm_health = ctk.CTkFrame(self.frm_right, fg_color="#131A2A", corner_radius=12)
        self.frm_health.grid(row=1, column=0, pady=(0, 10), sticky="ew")

        self.lblHealthScore = ctk.CTkLabel(
            self.frm_health, text="Health Score: --", font=("Segoe UI", 13, "bold"), text_color="#22D3EE"
        )
        self.lblHealthScore.pack(side="left", padx=15, pady=10)

        self.lblHealthAdvice = ctk.CTkLabel(
            self.frm_health, text="", font=("Segoe UI", 11, "italic"), text_color="#8A9BB4"
        )
        self.lblHealthAdvice.pack(side="left", padx=10, pady=10)

        self.lblIncome = ctk.CTkLabel(self.frm_summary, text="Income: $0.00", text_color="#4ADE80", font=("Segoe UI", 14, "bold"))
        self.lblIncome.pack(side="left", padx=20, pady=12)

        self.lblExpense = ctk.CTkLabel(self.frm_summary, text="Expenses: $0.00", text_color="#FB7185", font=("Segoe UI", 14, "bold"))
        self.lblExpense.pack(side="left", padx=20, pady=12)

        self.lblBalance = ctk.CTkLabel(self.frm_summary, text="Balance: $0.00", text_color="#22D3EE", font=("Segoe UI", 14, "bold"))
        self.lblBalance.pack(side="right", padx=20, pady=12)

        # 2. Category Expense Breakdown (Bars)
        self.frm_bars = ctk.CTkFrame(self.frm_right, fg_color="#131A2A", corner_radius=12)
        self.frm_bars.grid(row=1, column=0, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.frm_bars, text="Expenses Breakdown", font=("Segoe UI", 12, "bold"), text_color="#8A9BB4").pack(padx=15, pady=(8, 4), anchor="w")
        self.frm_bars_container = ctk.CTkFrame(self.frm_bars, fg_color="transparent")
        self.frm_bars_container.pack(fill="x", padx=15, pady=(0, 10))

        # 3. Filter Bar & Table
        self.frm_table_container = ctk.CTkFrame(self.frm_right, fg_color="#131A2A", corner_radius=12)
        self.frm_table_container.grid(row=2, column=0, sticky="nsew")
        self.frm_table_container.grid_rowconfigure(1, weight=1)
        self.frm_table_container.grid_columnconfigure(0, weight=1)

        # Filter Header
        frm_filter = ctk.CTkFrame(self.frm_table_container, fg_color="transparent")
        frm_filter.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

        ctk.CTkLabel(frm_filter, text="History", font=("Segoe UI", 14, "bold"), text_color="#E6EDF7").pack(side="left")

        self.cmbFilterKind = ctk.CTkOptionMenu(
            frm_filter, values=["All", "Expense", "Income"], fg_color="#0B0F1A", button_color="#22D3EE",
            width=110, command=lambda _: self._refresh_ui()
        )
        self.cmbFilterKind.pack(side="right")

        # Scrollable Table
        self.tblTransactions = ctk.CTkScrollableFrame(self.frm_table_container, fg_color="#0B0F1A", corner_radius=8)
        self.tblTransactions.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="nsew")

        self._refresh_ui()

    def _on_add(self):
        """Validates and processes input."""
        self.lblStatus.configure(text="", text_color="#FB7185")

        date = self.txtDate.get().strip()
        desc = self.txtDescription.get().strip()
        cat = self.cmbCategory.get()
        amt_str = self.txtAmount.get().strip()
        kind = self.cmbKind.get()

        if not desc:
            self.lblStatus.configure(text="Please enter a description.")
            return

        try:
            amt = float(amt_str)
            if amt <= 0:
                self.lblStatus.configure(text="Amount must be greater than zero.")
                return
        except ValueError:
            self.lblStatus.configure(text="Enter a valid numerical amount.")
            return

        self.service.add_transaction(date, desc, cat, amt, kind)
        self.lblStatus.configure(text="Saved & Auto-synced to JSON!", text_color="#4ADE80")
        self._clear_form()
        self._refresh_ui()

    def _on_delete(self, transaction_id: int):
        """Deletes a transaction after action trigger."""
        if self.service.delete_transaction(transaction_id):
            self.lblStatus.configure(text="Transaction removed.", text_color="#22D3EE")
            self._refresh_ui()

    def _clear_form(self):
        self.txtDescription.delete(0, "end")
        self.txtAmount.delete(0, "end")

    def _refresh_ui(self):
        self._render_table()
        self._render_bars()
        self._update_totals()

    def _update_health_panel(self):
        health = self.service.get_financial_health()
        self.lblHealthScore.configure(
            text=f"Health Score: {health['score']}/100 ({health['status']})",
            text_color=health['color']
        )
        self.lblHealthAdvice.configure(text=health['advice'])

    def _render_table(self):
        for w in self.tblTransactions.winfo_children():
            w.destroy()

        filter_val = self.cmbFilterKind.get()
        transactions = self.service.get_filtered_transactions(filter_val)

        if not transactions:
            lbl_empty = ctk.CTkLabel(
                self.tblTransactions,
                text="No transactions yet. Add your first income or expense to get started.",
                text_color="#8A9BB4", font=("Segoe UI", 12, "italic")
            )
            lbl_empty.pack(pady=40)
            return

        for t in reversed(transactions):
            row_color = "#4ADE80" if t.kind.lower() == "income" else "#FB7185"
            prefix = "+" if t.kind.lower() == "income" else "-"

            frm_row = ctk.CTkFrame(self.tblTransactions, fg_color="#131A2A", corner_radius=6)
            frm_row.pack(fill="x", padx=5, pady=4)

            lbl_info = ctk.CTkLabel(
                frm_row, text=f"{t.date}  |  {t.description} ({t.category})", text_color="#E6EDF7"
            )
            lbl_info.pack(side="left", padx=10, pady=6)

            # Delete button (btnDelete)
            btn_del = ctk.CTkButton(
                frm_row, text="✕", width=28, height=24, fg_color="transparent",
                hover_color="#FB7185", text_color="#8A9BB4",
                command=lambda tid=t.id: self._on_delete(tid)
            )
            btn_del.pack(side="right", padx=8)

            lbl_val = ctk.CTkLabel(
                frm_row, text=f"{prefix}${t.amount:.2f}", text_color=row_color,
                font=("JetBrains Mono", 12, "bold")
            )
            lbl_val.pack(side="right", padx=10)

    def _render_bars(self):
        for w in self.frm_bars_container.winfo_children():
            w.destroy()

        breakdown = self.service.get_category_breakdown()
        if not breakdown:
            ctk.CTkLabel(self.frm_bars_container, text="No expense data for breakdown.", text_color="#8A9BB4", font=("Segoe UI", 10, "italic")).pack(anchor="w")
            return

        for cat, ratio in breakdown.items():
            frm_b = ctk.CTkFrame(self.frm_bars_container, fg_color="transparent")
            frm_b.pack(fill="x", pady=2)

            ctk.CTkLabel(frm_b, text=f"{cat} ({ratio*100:.1f}%)", text_color="#E6EDF7", font=("Segoe UI", 10), width=120, anchor="w").pack(side="left")
            bar = ctk.CTkProgressBar(frm_b, fg_color="#0B0F1A", progress_color="#22D3EE", height=10)
            bar.set(ratio)
            bar.pack(side="left", fill="x", expand=True, padx=8)

    def _update_totals(self):
        totals = self.service.calculate_totals()
        self.lblIncome.configure(text=f"Income: ${totals['income']:.2f}")
        self.lblExpense.configure(text=f"Expenses: ${totals['expense']:.2f}")
        self.lblBalance.configure(text=f"Balance: ${totals['balance']:.2f}")


if __name__ == "__main__":
    app = PulseBudgetPro()
    app.mainloop()