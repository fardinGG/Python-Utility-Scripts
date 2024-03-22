import os

def split_sql_file(input_file, lines_per_file=35000):
    with open(input_file, 'r') as f:
        sql_content = f.readlines()

    num_files = (len(sql_content) - 1) // lines_per_file + 1

    for i in range(num_files):
        start_index = i * lines_per_file
        end_index = (i + 1) * lines_per_file
        output_file = f'output{i+1}.sql'

        with open(output_file, 'w') as f:
            f.writelines(sql_content[start_index:end_index])

def main():
    input_file = 'input.sql'
    if os.path.exists(input_file):
        split_sql_file(input_file)
        print("Splitting completed successfully.")
    else:
        print(f"The file '{input_file}' does not exist in the current directory.")

if __name__ == "__main__":
    main()
