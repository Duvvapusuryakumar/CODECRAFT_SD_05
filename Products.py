import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# Function to load the CSV file
def load_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(title="Select the CSV File", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    
    if file_path:
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)
            global dataframe
            dataframe = df  # Store dataframe globally for later use
            # Show a message that the file is loaded
            messagebox.showinfo("File Loaded", "Dataset successfully loaded!")
            label_file.config(text=f"File loaded: {file_path.split('/')[-1]}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load the file: {e}")

# Function to extract relevant columns and save to a new CSV file
def extract_and_save():
    try:
        # Extract columns (modify the column names based on your dataset)
        columns_of_interest = ['Product Name', 'Price', 'Rating']  # Adjust based on dataset
        if all(col in dataframe.columns for col in columns_of_interest):
            products = dataframe[columns_of_interest]
            
            # Open a save file dialog to choose where to save the new CSV
            output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
            
            if output_file:
                # Save the extracted data to a new CSV
                products.to_csv(output_file, index=False)
                messagebox.showinfo("Success", f"Data saved to {output_file}")
        else:
            messagebox.showerror("Error", "Missing one or more required columns: 'Product Name', 'Price', 'Rating'")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process the data: {e}")

# Create the main window for the GUI
root = tk.Tk()
root.title("DMart Products Data Extractor")

# Set the size of the window
root.geometry("400x250")

# Label to display the loaded file
label_file = tk.Label(root, text="No file loaded", wraplength=300)
label_file.pack(pady=20)

# Button to load the file
btn_load = tk.Button(root, text="Load CSV File", command=load_file)
btn_load.pack(pady=10)

# Button to extract and save the data
btn_extract = tk.Button(root, text="Extract and Save Data", command=extract_and_save)
btn_extract.pack(pady=10)

# Start the GUI event loop
root.mainloop()
