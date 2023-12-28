# Amass-Log-to-CSV

## Description

The Amass-Log-to-CSV tool is a Python script designed to transform the output from an Amass scan into a more manageable CSV file format. This conversion facilitates easier data manipulation and analysis, allowing users to extract valuable insights from their Amass scan results.

## Usage

1. Perform an Amass scan and save the output to a log file using the following command:

    ```bash
    sudo amass enum -active -d anir0y.in -p 21,22 -o anir0y.log
    ```

2. Run the provided Python script to convert the Amass log file to CSV format. Use the following command in the command-line interface (CLI):

    ```bash
    python3 amass-log-to-csv.py anir0y.log
    ```

3. The script will create an output CSV file with the same name as the input log file, but with the `.csv` extension. For example, if the input file is `anir0y.log`, the output file will be `anir0y.csv`.

4. IF you just want domain names
   ```bash
   cat anir0y.log | grep a_record| awk -F ' ' '{print $1}'  | sort | uniq | tee tmp.log
   ```

## Requirements

Ensure you have the required Python packages installed by running the following command:

```bash
pip install -r requirements.txt
```
---

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40Anir0y)](https://twitter.com/anir0y)
