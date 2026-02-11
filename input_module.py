"""
Input/Output Module for handling file uploads and exports
"""

import tkinter as tk
from tkinter import filedialog, messagebox


def upload_text_file(text_widget):
    """
    Open a file dialog to upload a text file and insert its content into the text widget.
    
    Args:
        text_widget: The tkinter Text widget to insert the content into
    
    Returns:
        str: The text content that was loaded, or None if cancelled
    """
    try:
        file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Clear the text widget and insert the file content
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
            return content
    except UnicodeDecodeError:
        messagebox.showerror("Error", "Could not read file. Please ensure it's a valid text file.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload file: {str(e)}")
    
    return None


def export_text_file(text_widget):
    """
    Open a file dialog to export the text widget content to a file.
    
    Args:
        text_widget: The tkinter Text widget to export content from
    """
    try:
        content = text_widget.get("1.0", tk.END).strip()
        
        if not content:
            messagebox.showwarning("Warning", "No text to export.")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save text file as",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            messagebox.showinfo("Success", f"File saved successfully to:\n{file_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export file: {str(e)}")
