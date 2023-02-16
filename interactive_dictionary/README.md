# Interactive Dictionary 
This project is an interactive dictionary. It uses a data.json file which contains an entire list of words and definitions. The program loads this file and ask the user for an input. After the user gives his input, it checks if the word exists in the file, and if it doesn't it uses python's difflib library to check for possible matches and allow the user to confirm if the suggestions are correct. If the word doesn't exist at all or isn't found, the program returns this statement and ends. If the word is found, then, it returns a list with all possible meanings for it. 

## How to run and use the program
Type the following command in the terminal: 
```
$ python3 app.py
```
Then, after you run the program, type in a word to search.
