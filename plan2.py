

import tkinter as tk
import random
import time
from tkinter import font, messagebox
from datetime import datetime

class LabExamSelector:
    def __init__(self):
        """"""
        # ======================================================================
        # WINDOW CONFIGURATION
        # ======================================================================
        self.root = tk.Tk()
        self.root.title("LAB EXAM QUESTION SELECTOR - MRIST")
        self.root.geometry("900x700")
        
        # Neuroscience-based color palette (optimized for focus and dopamine response)
        self.COLORS = {
            'primary_bg': '#0F1A30',        # Deep space blue - reduces eye strain
            'secondary_bg': '#1A2B4A',      # Darker blue - creates depth
            'accent': '#00D4AA',           # Cyan-green - stimulates focus
            'accent_light': '#4DFFD1',     # Light cyan - positive feedback
            'warning': '#FF6B9D',          # Pink-red - attention grabbing
            'success': '#2ECC71',          # Green - success confirmation
            'text_primary': '#FFFFFF',     # White - maximum contrast
            'text_secondary': '#B0BEC5',   # Light gray - reduced emphasis
            'card_bg': '#223354',          # Card background
            'highlight': '#7E57C2'         # Purple - visual interest
        }
        
        # Configure root window
        self.root.configure(bg=self.COLORS['primary_bg'])
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # ======================================================================
        # QUESTION BANK (Fixed set of 22 programming questions)
        # ======================================================================
        self.questions = [
            "1. Write a program to print \"Hello World\".",
            "2. Write a program to print \"Welcome to MRIST\".",
            "3. Write a program to take a name as input and display it.",
            "4. Write a program to take a name as input and display it along with \"MRIST\".",
            "5. Write a program to check whether a given number is even or odd.",
            "6. Write a program to check whether a given number is positive or negative.",
            "7. Write a program to check whether a given character is a vowel or consonant.",
            "8. Write a program to check whether a given year is a leap year.",
            "9. Write a program to calculate the area of a circle.",
            "10. Write a program to calculate the area of a triangle.",
            "11. Write a program to calculate the area of a rectangle.",
            "12. Write a program to calculate the area of a square.",
            "13. Write a program to display numbers from 1 to 100 using a loop.",
            "14. Write a program to display even numbers from 10 to 100.",
            "15. Write a program to display odd numbers from 10 to 100.",
            "16. Write a program to find the sum of the series\n   1 + 2 + 3 + 4 + … + n.",
            "17. Write a program to find the sum of the series\n   2 + 4 + 6 + … + n.",
            "18. Write a program to calculate the product of the series\n   1 × 2 × 3 × 4 × … × n.",
            "19. Write a program to print the following pattern:\n\n   *\n   **\n   ***\n   ****",
            "20. Write a program to generate the multiplication table of a given number.",
            "21. Write a program using a function to check whether a number is even or odd.",
            "22. Write a program using a function to check whether a year is a leap year."
        ]
        
        # Application state variables
        self.selected_question = None
        self.selection_history = []
        self.is_selecting = False
        self.total_selections = 0
        
        # Initialize UI components
        self.setup_ui()
        
        # Start the main event loop
        self.root.mainloop()
    
    def center_window(self):
        """Position window at the center of the screen"""
        self.root.update_idletasks()
        width = 900
        height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Construct all user interface elements with professional layout"""
        # ======================================================================
        # HEADER SECTION
        # ======================================================================
        header_frame = tk.Frame(self.root, bg=self.COLORS['primary_bg'])
        header_frame.pack(pady=(30, 20), fill=tk.X)
        
        # Main title with professional typography
        title_font = font.Font(family='Segoe UI', size=28, weight='bold')
        title_label = tk.Label(
            header_frame,
            text="LAB EXAM QUESTION SELECTOR",
            font=title_font,
            fg=self.COLORS['accent'],
            bg=self.COLORS['primary_bg']
        )
        title_label.pack()
        
        # Subtitle with institution name
        subtitle_font = font.Font(family='Segoe UI', size=14)
        subtitle_label = tk.Label(
            header_frame,
            text="MRIST - Programming Lab Assessment System",
            font=subtitle_font,
            fg=self.COLORS['text_secondary'],
            bg=self.COLORS['primary_bg']
        )
        subtitle_label.pack(pady=(5, 0))
        
        # ======================================================================
        # MAIN DISPLAY SECTION
        # ======================================================================
        display_frame = tk.Frame(
            self.root,
            bg=self.COLORS['secondary_bg'],
            relief=tk.FLAT,
            bd=0
        )
        display_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        # Question number indicator (dynamic)
        self.question_number_label = tk.Label(
            display_frame,
            text="SELECTED QUESTION",
            font=font.Font(family='Segoe UI', size=16, weight='bold'),
            fg=self.COLORS['accent_light'],
            bg=self.COLORS['secondary_bg']
        )
        self.question_number_label.pack(pady=(30, 5))
        
        # Question display area with professional styling
        question_display_frame = tk.Frame(
            display_frame,
            bg=self.COLORS['card_bg'],
            relief=tk.FLAT,
            bd=0
        )
        question_display_frame.pack(pady=10, padx=30, fill=tk.BOTH, expand=True)
        
        # Actual question text display
        self.question_text = tk.Text(
            question_display_frame,
            height=10,
            width=70,
            wrap=tk.WORD,
            font=font.Font(family='Consolas', size=13),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['card_bg'],
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=20,
            pady=20,
            state=tk.DISABLED
        )
        self.question_text.pack(expand=True, fill=tk.BOTH)
        
        # Default placeholder text
        self.question_text.config(state=tk.NORMAL)
        self.question_text.insert(1.0, "Click 'START SELECTION' to begin the random question selection process.\n\n"
                                      "The selected question will appear here with full details.")
        self.question_text.config(state=tk.DISABLED)
        
        # ======================================================================
        # CONTROL PANEL SECTION
        # ======================================================================
        control_frame = tk.Frame(self.root, bg=self.COLORS['primary_bg'])
        control_frame.pack(pady=20)
        
        # Primary action button - Start Selection
        self.select_button = tk.Button(
            control_frame,
            text="▶ START SELECTION",
            font=font.Font(family='Segoe UI', size=16, weight='bold'),
            bg=self.COLORS['accent'],
            fg=self.COLORS['primary_bg'],
            activebackground=self.COLORS['accent_light'],
            activeforeground=self.COLORS['primary_bg'],
            relief=tk.FLAT,
            bd=0,
            height=2,
            width=20,
            cursor='hand2',
            command=self.start_selection
        )
        self.select_button.grid(row=0, column=0, padx=10)
        
        # Secondary action button - Clear Selection
        clear_button = tk.Button(
            control_frame,
            text="🔄 CLEAR",
            font=font.Font(family='Segoe UI', size=14),
            bg=self.COLORS['highlight'],
            fg=self.COLORS['text_primary'],
            activebackground='#9575CD',
            activeforeground=self.COLORS['text_primary'],
            relief=tk.FLAT,
            bd=0,
            height=2,
            width=15,
            cursor='hand2',
            command=self.clear_selection
        )
        clear_button.grid(row=0, column=1, padx=10)
        
        # ======================================================================
        # STATISTICS PANEL
        # ======================================================================
        stats_frame = tk.Frame(self.root, bg=self.COLORS['secondary_bg'])
        stats_frame.pack(pady=10, padx=50, fill=tk.X)
        
        # Statistics labels
        stats_font = font.Font(family='Segoe UI', size=11)
        
        self.total_label = tk.Label(
            stats_frame,
            text="Total Selections: 0",
            font=stats_font,
            fg=self.COLORS['text_secondary'],
            bg=self.COLORS['secondary_bg']
        )
        self.total_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.time_label = tk.Label(
            stats_frame,
            text="Current Time: --:--:--",
            font=stats_font,
            fg=self.COLORS['text_secondary'],
            bg=self.COLORS['secondary_bg']
        )
        self.time_label.grid(row=0, column=1, padx=20, pady=10)
        
        self.status_label = tk.Label(
            stats_frame,
            text="Status: Ready",
            font=stats_font,
            fg=self.COLORS['success'],
            bg=self.COLORS['secondary_bg']
        )
        self.status_label.grid(row=0, column=2, padx=20, pady=10)
        
        # Update time display
        self.update_time()
        
        # ======================================================================
        # HISTORY DISPLAY
        # ======================================================================
        history_frame = tk.Frame(self.root, bg=self.COLORS['primary_bg'])
        history_frame.pack(pady=(10, 20), padx=50, fill=tk.BOTH, expand=True)
        
        # History label
        history_label = tk.Label(
            history_frame,
            text="Selection History",
            font=font.Font(family='Segoe UI', size=12, weight='bold'),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['primary_bg']
        )
        history_label.pack(anchor=tk.W, pady=(0, 5))
        
        # History listbox with scrollbar
        history_container = tk.Frame(history_frame, bg=self.COLORS['card_bg'])
        history_container.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar for history
        scrollbar = tk.Scrollbar(history_container, bg=self.COLORS['card_bg'])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # History listbox
        self.history_listbox = tk.Listbox(
            history_container,
            height=6,
            font=font.Font(family='Segoe UI', size=10),
            bg=self.COLORS['card_bg'],
            fg=self.COLORS['text_primary'],
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            selectbackground=self.COLORS['accent'],
            activestyle='none',
            yscrollcommand=scrollbar.set
        )
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_listbox.yview)
        
        # ======================================================================
        # FOOTER SECTION
        # ======================================================================
        footer_frame = tk.Frame(self.root, bg=self.COLORS['primary_bg'])
        footer_frame.pack(pady=10)
        
        footer_label = tk.Label(
            footer_frame,
            text="Professional Lab Exam System • MRIST • Secure Random Selection",
            font=font.Font(family='Segoe UI', size=9),
            fg=self.COLORS['text_secondary'],
            bg=self.COLORS['primary_bg']
        )
        footer_label.pack()
    
    def update_time(self):
        """Update current time display every second"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)
    
    def start_selection(self):
        """Initiate the random question selection process with visual feedback"""
        if self.is_selecting:
            return  # Prevent multiple simultaneous selections
        
        self.is_selecting = True
        self.select_button.config(state=tk.DISABLED, text="SELECTING...")
        self.status_label.config(text="Status: Selecting...", fg=self.COLORS['warning'])
        
        # Visual feedback animation
        self.animate_selection()
        
        # Schedule final selection after animation
        self.root.after(800, self.finalize_selection)
    
    def animate_selection(self):
        """Provide visual feedback during selection process"""
        # Change question number display during animation
        self.question_number_label.config(
            text=f"SELECTING...",
            fg=self.COLORS['warning']
        )
        
        # Clear and show random questions during animation
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        
        # Show multiple random questions quickly
        for i in range(5):
            random_index = random.randint(0, len(self.questions) - 1)
            preview_text = f"Question {random_index + 1}\n\n{self.questions[random_index][:100]}..."
            self.question_text.delete(1.0, tk.END)
            self.question_text.insert(1.0, preview_text)
            self.root.update()
            time.sleep(0.1)
        
        self.question_text.config(state=tk.DISABLED)
    
    def finalize_selection(self):
        """Complete the selection process and display the chosen question"""
        # Generate random question
        self.selected_question = random.choice(self.questions)
        question_num = int(self.selected_question.split('.')[0])
        
        # Update display with selected question
        self.question_number_label.config(
            text=f"SELECTED: QUESTION {question_num}",
            fg=self.COLORS['success']
        )
        
        # Update question text display
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(1.0, self.selected_question)
        self.question_text.config(state=tk.DISABLED)
        
        # Update statistics
        self.total_selections += 1
        self.total_label.config(text=f"Total Selections: {self.total_selections}")
        
        # Add to history
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"{timestamp} - Question {question_num}"
        self.selection_history.append(history_entry)
        self.history_listbox.insert(0, history_entry)
        
        # Keep history manageable
        if len(self.selection_history) > 10:
            self.selection_history.pop()
            self.history_listbox.delete(10)
        
        # Update status
        self.status_label.config(text="Status: Question Selected", fg=self.COLORS['success'])
        
        # Reset button state
        self.select_button.config(state=tk.NORMAL, text="▶ SELECT AGAIN")
        self.is_selecting = False
        
        # Visual confirmation effect
        self.confirm_selection()
    
    def confirm_selection(self):
        """Provide visual confirmation of successful selection"""
        original_bg = self.question_text.cget('bg')
        
        # Flash effect
        for _ in range(2):
            self.question_text.config(bg=self.COLORS['accent'])
            self.root.update()
            time.sleep(0.1)
            self.question_text.config(bg=original_bg)
            self.root.update()
            time.sleep(0.1)
    
    def clear_selection(self):
        """Reset the display to initial state"""
        if messagebox.askyesno("Clear Selection", "Clear current question and history?"):
            # Reset display
            self.question_number_label.config(
                text="SELECTED QUESTION",
                fg=self.COLORS['accent_light']
            )
            
            self.question_text.config(state=tk.NORMAL)
            self.question_text.delete(1.0, tk.END)
            self.question_text.insert(1.0, 
                "Click 'START SELECTION' to begin the random question selection process.\n\n"
                "The selected question will appear here with full details."
            )
            self.question_text.config(state=tk.DISABLED)
            
            # Clear history
            self.selection_history.clear()
            self.history_listbox.delete(0, tk.END)
            
            # Reset statistics
            self.total_selections = 0
            self.total_label.config(text="Total Selections: 0")
            
            # Update status
            self.status_label.config(text="Status: Ready", fg=self.COLORS['success'])
            
            # Reset button
            self.select_button.config(text="▶ START SELECTION")
            
            # Reset selection state
            self.selected_question = None
    
    def on_closing(self):
        """Handle application closing"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()


# ==============================================================================
# APPLICATION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("LAB EXAM QUESTION SELECTOR")
    print("MRIST - Professional Assessment System")
    print("=" * 70)
    print("\nInitializing application...")
    
    # Create and run the application
    app = LabExamSelector()
    
    print("\nApplication terminated.")
    print("=" * 70)