import pdfplumber
import os

# Open a text file to write the output
with open("all.summaries.txt", "w") as output_file:
    # Iterate through all PDF files in the folder
    for file_name in os.listdir("."):
        if file_name.endswith(".pdf"):
            # Write the first 7 characters of the file name to the text file
            output_file.write(file_name[:7] + "\n")
            
            # Open the PDF file
            with pdfplumber.open(file_name) as pdf:
                extracted_text = ""
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        # Find the word "Synopsis" and extract text from there to the end
                        if "Synopsis" in text:
                            extracted_text = text.split("Synopsis", 1)[1]
                            break
                
                # Write the extracted text to the file followed by two newlines
                output_file.write(extracted_text.strip() + "\n\n")
