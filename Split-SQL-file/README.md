### Script Description:

This Python script is designed to split a large SQL file into smaller files based on a specified number of lines per file. The script takes an input SQL file named `input.sql` located in the same directory as the script itself. It then splits the content of the input SQL file into multiple output files, with each output file containing a maximum of 35,000 lines of SQL queries. If the total number of lines in the input SQL file is not evenly divisible by 35,000, the remaining lines are written to an additional output file.

### Instructions for Use:

1. **Prepare the Input SQL File:**
   - Ensure that the input SQL file you want to split is named `input.sql`.
   - Place the `input.sql` file in the same directory as the Python script.

2. **Download and Run the Python Script:**
   - Download the provided Python script to your local machine.

   ```python
   # Save the Python script with a meaningful name, e.g., split_sql.py
   ```

   - Open a terminal or command prompt.

   ```
   # Navigate to the directory containing the Python script and input SQL file
   cd /path/to/directory
   ```

   - Run the Python script by executing the following command:

   ```
   python split_sql.py
   ```

3. **Monitor the Output:**
   - The script will process the input SQL file and split it into multiple output files.
   - Output files will be named `output1.sql`, `output2.sql`, and so on, with each file containing up to 35,000 lines of SQL queries.
   - If the total number of lines in the input SQL file is not evenly divisible by 35,000, the remaining lines will be written to an additional output file.

4. **Verify Output Files:**
   - Once the script execution is complete, verify that the output files contain the expected SQL content.
   - You can open and review each output file using a text editor or SQL development tool.

5. **Customization (Optional):**
   - If you need to adjust the number of lines per output file, you can modify the `lines_per_file` parameter in the script.
   - You can also customize the input SQL file name by changing the `input_file` variable in the script if your input SQL file has a different name.

By following these instructions, you can effectively split a large SQL file into smaller files using the provided Python script.