# Numpy and panda weather
This Python script performs a  analysis of weather conditions across different cities. It uses sample data to illustrate key functionalities of the NumPy, Pandas, and Matplotlib libraries.

# Webscraping and JSON
Uses an API to Obtain JSON Formatted Data 
The script also sends a request to the OpenWeatherMap API to fetch weather data for a specified city. It Extracts and Manipulates Values from JSON Formatted Data. After receiving the JSON response from the API, the script extracts the temperature, weather condition, and wind speed. It then prints these values, demonstrating data manipulation.

# Fundamentals
The Python script performs several operations involving file handling, list manipulation, and command line interaction.

Reads a File: The script reads contents from an input file specified by the user via the command line. The file is expected to contain a list of items, with one item per line.

Appends an Item to a List Iteratively: The script takes an item provided by the user and appends it to the list of items read from the file. The appending is done inside a loop, though the loop iterates only once.

Removes an Item from the List Iteratively: The script also removes an item (specified by the user as another command line argument) from the list. If the item appears multiple times in the list, it will be removed in each iteration until it no longer exists in the list.

Writes to a File: After modifying the list , the script writes the updated list to an output file specified by the user. Each item in the list is written to a new line in the file.

Appends Additional Content to the File: The script then appends a line to the same output file.

Error Handling: It raises a ValueError if the required command line arguments are not provided. It also catches a FileNotFoundError if the input file does not exist, and a general Exception for other errors, printing an error message in each case.

Command Line Arguments: The script uses sys.argv to accept user input. It expects four arguments in addition to the script name: the input file path, the output file path, the item to be appended to the list, and the item to be removed from the list.
