import sys

def read_file(file_path):
    #reads content from a file
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, content, mode='w'):
   ##Writes content to a file
    with open(file_path, mode) as file:
        file.write(content + '\n')

def process_list(items, item_to_add, item_to_remove):
   #Appends and removes items from the list
    # Append item
    for _ in range(1):
        items.append(item_to_add)

    # Remove item
    while item_to_remove in items:
        items.remove(item_to_remove)

    return items

def main():
    if len(sys.argv) < 5:
        raise ValueError("Usage: script.py input_file output_file item_to_add item_to_remove")

    input_file, output_file, item_to_add, item_to_remove = sys.argv[1:5]

    try:
        items = read_file(input_file)
        items = [item.strip() for item in items]  # Removing characters

        processed_items = process_list(items, item_to_add, item_to_remove)

        write_file(output_file, '\n'.join(processed_items))

        # Appends the additional content
        write_file(output_file, "End of modifications.", mode='a')

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
