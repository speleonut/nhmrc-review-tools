import pdfplumber
import os
# Full discosure: I asked CoPilot to write this for me because I am hoping to learn python using the direct opposite of the recommended hard-way https://learnpythonthehardway.org/
# Problem: NHMRC makes a nice spreadsheet that you can go through for doing COI but they don't include the Synopsis; which is the bit you actually need to read to decide if you can review or not.  
# Depending on the scheme, you may have to open up 100s of pdfs to read through all of the applications they want you to check, which sucks and takes a long time.
# Usage: Once you have downloaded all of the synposises(?) just drop this script in the same folder and run it. 
# The script creates a single text file that you can easily scroll through leaving dealing with Sapphire as your main problem.

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
