import csv
import re
import sys

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                 AUTHOR INFO                                 ┃
# ┠─────────────────────────────────────────────────────────────────────────────┨
# ┃ Author      : @anir0y {anir0y.in}                                           ┃
# ┃                                                                             ┃
# ┃                             AMASS COMMAND                                   ┃
# ┠─────────────────────────────────────────────────────────────────────────────┨
# ┃ Command     : sudo amass enum -active -d anir0y.in -p 21,22 -o anir0y.log   ┃
# ┃                                                                             ┃
# ┃                    SCRIPT TO CONVERT AMASS LOG TO CSV                       ┃
# ┠─────────────────────────────────────────────────────────────────────────────┨
# ┃ Script      : python3 amass-log-to-csv.py anir0y.log                        ┃
# ┃ Output File : anir0y.csv                                                    ┃
# ┃                                                                             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def strip_color_codes(text):
    # Use a regular expression to remove color codes
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

def convert_to_csv(input_file_path):
    # Generate output file path based on the input file name
    output_file_path = input_file_path.rsplit('.', 1)[0] + '.csv'

    # Open the input and output files
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        # Create a CSV writer object
        csv_writer = csv.writer(output_file)

        # Write the header to the CSV file
        csv_writer.writerow(['Source FQDN', 'Record Type', 'Destination FQDN'])

        # Iterate through each line in the input file
        for line in input_file:
            # Strip color codes from the line
            line = strip_color_codes(line)

            # Split the line based on ' --> ' and ' (FQDN)'
            parts = line.strip().split(' --> ')

            # If there are at least two parts
            if len(parts) >= 2:
                source_fqdn = parts[0]
                
                # If there are three parts, use the second part as record_type
                if len(parts) == 3:
                    record_type = parts[1].replace(' (FQDN)', '')
                    destination_fqdn = parts[2].replace(' (FQDN)', '')
                else:
                    record_type = 'Unknown'
                    destination_fqdn = parts[1].replace(' (FQDN)', '')

                # Write the data to the CSV file
                csv_writer.writerow([source_fqdn, record_type, destination_fqdn])

    print(f"Conversion complete. CSV file saved at {output_file_path}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <input_file>")
        sys.exit(1)

    # Get the input file path from the command line arguments
    input_file_path = sys.argv[1]

    # Call the function to convert to CSV
    convert_to_csv(input_file_path)
