import csv
input_file = "data.csv"
output_file = "Cleaned_output.csv"

with open(input_file,"r")as infile,open(output_file, "w",newline="")as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row["age"] == "":
            row["age"] = "0"
        if row["city"] == "":
            row["city"] = "Unknown"    
        writer.writerow(row)
print("Data cleaning completed. Cleaned data saved to")            
