input_file = "test.txt"
output_file = "log_analysis.txt"

with open(input_file, "r") as file:
    lines =file.readlines()

error = []

for line in lines:
    if "ERROR" in line:
        error.append(line)

with open(output_file, "w") as file:
    file.writelines(error)
print("Log analysis completed. Errors saved to", output_file)    
