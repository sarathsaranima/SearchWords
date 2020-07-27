# Products

A simple python program that search for a keyword in 200 line input text file without 
inbuilt search function and extracts all results to a csv file with index starting from 1

#### Pre-requisites

1. Python3.2+ installed

#### Running the application
1. Open up terminal and navigate to the `SearchWords` folder
2. Execute the following commands:

```cmd

py -3 run.py
```

This prompts to input a search file and a keyword as below

```
Enter the text file path :C:\GitRepo\SearchWords\text_file.txt
Enter the keyword to search in text:lorem

```

On Completion gives the below message

``` 
No of lines in the text: 200
Input Successfully Validated..
The count of keyword matches :9
Successfully generated output file key_count.csv
```

# Unit Testing

Start the unit testing using below steps.

1. Open up a new terminal and navigate to the `SearchWords\tests` folder
2. Execute the following commands:

```cmd

py -3 test_run.py
```
This should execute the unit tests and produce the following output


----------------------------------------------------------------------
Ran 2 tests in 0.013s

OK

