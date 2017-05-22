# QA Report Generation Script

### Example Usage of The Script Can Be Seen Below ###
```
python generate_report.py -i <inputfile.txt> -o <outputfile.html>
```

Note: You must ensure that your input.txt file is present within the root of this project and that your output file name must have an extension of .html

To generate all of the files simply issue the -a command. This will take every .txt file and generate an html report for each one in a new sub_directory (called html_reports/).

```
python generate_report.py -a
```
