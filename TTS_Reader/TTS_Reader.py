# # import PyPDF2
# # from gtts import gTTS
# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# # import os

# # # Function to open file dialog
# # def text_extract(pdf_path):
# #     # Opens the pdf file. The rb is for read binary mode
# #     with open(pdf_path, 'rb') as file: 
# #         reader = PyPDF2.PdfFileReader(file) 
# #         text = "" 
# #         for page in reader.pages: 
# #             text += page.extract_text()
# #     return text

# # # Function to save text to speech
# # def text_to_speech(text, output_file):
# #     tts = gTTS(text=text, lang='en')
# #     tts.save(output_file)

# # # Function to select pdf file    
# # def select_pdf():
# #     root = tk.Tk()
# #     root.withdraw() # Hide the main window
# #     file_path = filedialog.askopenfilename(
# #         title="Select PDF file", 
# #         filetypes=[("PDF files", "*.pdf")]
# #     )
# #     return file_path

# # # Function to convert pdf to audio
# # def pdf_to_audio():
# #     pdf_path = select_pdf() # Get the path of the pdf file
# #     if pdf_path: # Check if a file was selected
# #         text = text_extract(pdf_path)
# #         # Dynamically generate the output file name
# #         base_name = os.path.splitext(os.path.basename(pdf_path))[0]
# #         output_file = f"{base_name}.mp3"
# #         text_to_speech(text, output_file)
# #         messagebox.showinfo("Success", f"Audio file saved as {output_file}")
# #     else:
# #         messagebox.showerror("No file selected", "Please select a PDF file")
        
# # # Setting up the GUI
# # def setup_gui():
# #     root = tk.Tk()
# #     root.title("PDF to Audio Converter")
    
# #     # Create a frame
# #     frame = tk.Frame(root, padx=20, pady=20)
# #     frame.pack(padx=10, pady=10)
    
# #     # Create a label for the button
# #     label = tk.Label(frame, text="Click the button to select a PDF file to convert to audio")
# #     label.pack(pady=10)
    
# #     convert_button = tk.Button(frame, text="Convert PDF to Audio", command=pdf_to_audio)
# #     convert_button.pack(pady=10)
    
# #     root.mainloop()
        
# # # Run the GUI
# # setup_gui()

# import PyPDF2
# from gtts import gTTS
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import os

# # Function to open file dialog
# def text_extract(pdf_path):
#     try:
#         # Opens the pdf file. The rb is for read binary mode
#         with open(pdf_path, 'rb') as file: 
#             reader = PyPDF2.PdfFileReader(file) 
#             text = "" 
#             for page in reader.pages: 
#                 text += page.extract_text()
#         return text
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return None

# # Function to save text to speech
# def text_to_speech(text, output_file):
#     try:
#         tts = gTTS(text=text, lang='en')
#         tts.save(output_file)
#         print(f"Audio saved to {output_file}")
#     except Exception as e:
#         print(f"Error converting text to speech: {e}")

# # Function to select pdf file    
# def select_pdf():
#     root = tk.Tk()
#     root.withdraw() # Hide the main window
#     file_path = filedialog.askopenfilename(
#         title="Select PDF file", 
#         filetypes=[("PDF files", "*.pdf")]
#     )
#     return file_path

# # Function to convert pdf to audio
# def pdf_to_audio():
#     pdf_path = select_pdf() # Get the path of the pdf file
#     if pdf_path:
#         print(f"Selected PDF: {pdf_path}")
#         text = text_extract(pdf_path)
#         if text:
#             output_file = os.path.splitext(pdf_path)[0] + ".mp3"
#             text_to_speech(text, output_file)
#         else:
#             print("No text extracted from the PDF.")
#     else:
#         print("No PDF file selected.")

# # Run the conversion
# if __name__ == "__main__":
#     pdf_to_audio()

import PyPDF2
from gtts import gTTS
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to open file dialog
def text_extract(pdf_path):
    try:
        # Opens the pdf file. The rb is for read binary mode
        with open(pdf_path, 'rb') as file: 
            reader = PyPDF2.PdfReader(file) 
            text = "" 
            for page in reader.pages: 
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

# Function to save text to speech
def text_to_speech(text, output_file):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_file)
        print(f"Audio saved to {output_file}")
    except Exception as e:
        print(f"Error converting text to speech: {e}")

# Function to select pdf file    
def select_pdf():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select PDF file", 
        filetypes=[("PDF files", "*.pdf")]
    )
    return file_path

# Function to convert pdf to audio
def pdf_to_audio():
    pdf_path = select_pdf() # Get the path of the pdf file
    if pdf_path:
        print(f"Selected PDF: {pdf_path}")
        text = text_extract(pdf_path)
        if text:
            output_file = os.path.splitext(pdf_path)[0] + ".mp3"
            text_to_speech(text, output_file)
        else:
            print("No text extracted from the PDF.")
    else:
        print("No PDF file selected.")

# Run the conversion
if __name__ == "__main__":
    pdf_to_audio()