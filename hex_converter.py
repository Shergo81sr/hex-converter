import tkinter as tk
from tkinter import ttk, messagebox

class HexConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Hex Converter")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        # Title frame
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=10)
        
        title_label = ttk.Label(title_frame, text="Text to Hex Converter", 
                               font=("Arial", 16, "bold"))
        title_label.pack()
        
        # Input frame
        input_frame = ttk.LabelFrame(self.root, text="Input Text")
        input_frame.pack(fill="x", padx=20, pady=10)
        
        self.input_text = tk.Text(input_frame, height=5, width=70)
        self.input_text.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Buttons frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.to_hex_btn = ttk.Button(button_frame, text="Convert to Hex", 
                                    command=self.convert_to_hex)
        self.to_hex_btn.pack(side="left", padx=5)
        
        self.from_hex_btn = ttk.Button(button_frame, text="Convert from Hex", 
                                      command=self.convert_from_hex)
        self.from_hex_btn.pack(side="left", padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="Clear", 
                                   command=self.clear_text)
        self.clear_btn.pack(side="left", padx=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(self.root, text="Output")
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.output_text = tk.Text(output_frame, height=5, width=70)
        self.output_text.pack(padx=10, pady=10, fill="both", expand=True)
        
    def convert_to_hex(self):
        """Convert text to hex encoding"""
        input_data = self.input_text.get("1.0", "end-1c").strip()
        
        if not input_data:
            messagebox.showwarning("Warning", "Please enter text to convert")
            return
        
        try:
            # Convert text to bytes then to hex
            hex_result = input_data.encode('utf-8').hex()
            # Format result for better display
            formatted_hex = ' '.join([hex_result[i:i+2] for i in range(0, len(hex_result), 2)])
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", formatted_hex)
        except Exception as e:
            messagebox.showerror("Error", f"Conversion error: {str(e)}")
    
    def convert_from_hex(self):
        """Convert hex encoding to text"""
        input_data = self.input_text.get("1.0", "end-1c").strip()
        
        if not input_data:
            messagebox.showwarning("Warning", "Please enter hex text to convert")
            return
        
        try:
            # Remove spaces from input
            clean_hex = input_data.replace(' ', '')
            
            # Validate if input is valid hex
            if not all(c in '0123456789abcdefABCDEF' for c in clean_hex):
                messagebox.showerror("Error", "Input is not valid hex encoding")
                return
            
            # Convert hex to bytes then to text
            text_result = bytes.fromhex(clean_hex).decode('utf-8')
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", text_result)
        except Exception as e:
            messagebox.showerror("Error", f"Conversion error: {str(e)}")
    
    def clear_text(self):
        """Clear all text fields"""
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = HexConverterApp(root)
    root.mainloop()