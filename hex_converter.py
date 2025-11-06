import tkinter as tk
from tkinter import ttk, messagebox

class HexConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("محول النص إلى Hex والعكس")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # إعداد واجهة المستخدم
        self.setup_ui()
        
    def setup_ui(self):
        # إطار العنوان
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=10)
        
        title_label = ttk.Label(title_frame, text="محول النص إلى Hex والعكس", 
                               font=("Arial", 16, "bold"))
        title_label.pack()
        
        # إطار الإدخال
        input_frame = ttk.LabelFrame(self.root, text="النص المدخل")
        input_frame.pack(fill="x", padx=20, pady=10)
        
        self.input_text = tk.Text(input_frame, height=5, width=70)
        self.input_text.pack(padx=10, pady=10, fill="both", expand=True)
        
        # إطار الأزرار
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.to_hex_btn = ttk.Button(button_frame, text="تحويل إلى Hex", 
                                    command=self.convert_to_hex)
        self.to_hex_btn.pack(side="left", padx=5)
        
        self.from_hex_btn = ttk.Button(button_frame, text="تحويل من Hex", 
                                      command=self.convert_from_hex)
        self.from_hex_btn.pack(side="left", padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="مسح", 
                                   command=self.clear_text)
        self.clear_btn.pack(side="left", padx=5)
        
        # إطار الإخراج
        output_frame = ttk.LabelFrame(self.root, text="الناتج")
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.output_text = tk.Text(output_frame, height=5, width=70)
        self.output_text.pack(padx=10, pady=10, fill="both", expand=True)
        
    def convert_to_hex(self):
        """تحويل النص إلى ترميز Hex"""
        input_data = self.input_text.get("1.0", "end-1c").strip()
        
        if not input_data:
            messagebox.showwarning("تحذير", "يرجى إدخال نص للتحويل")
            return
        
        try:
            # تحويل النص إلى bytes ثم إلى hex
            hex_result = input_data.encode('utf-8').hex()
            # تنسيق النتيجة لعرضها بشكل أفضل
            formatted_hex = ' '.join([hex_result[i:i+2] for i in range(0, len(hex_result), 2)])
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", formatted_hex)
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحويل: {str(e)}")
    
    def convert_from_hex(self):
        """تحويل ترميز Hex إلى نص"""
        input_data = self.input_text.get("1.0", "end-1c").strip()
        
        if not input_data:
            messagebox.showwarning("تحذير", "يرجى إدخال نص hex للتحويل")
            return
        
        try:
            # إزالة المسافات من النص المدخل
            clean_hex = input_data.replace(' ', '')
            
            # التحقق من أن النص المدخل هو hex صالح
            if not all(c in '0123456789abcdefABCDEF' for c in clean_hex):
                messagebox.showerror("خطأ", "النص المدخل ليس ترميز hex صالح")
                return
            
            # تحويل hex إلى bytes ثم إلى نص
            text_result = bytes.fromhex(clean_hex).decode('utf-8')
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", text_result)
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحويل: {str(e)}")
    
    def clear_text(self):
        """مسح جميع الحقول"""
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = HexConverterApp(root)
    root.mainloop()