# Extractor
Python scripts to extract data from text files

Inspired by [EmailsFromFile](http://patrickmylund.com/projects/emailsfromfile/) by Patrick Mylund Nielsen

Compatable with Python 2.7


## EmailsFromFile
A Python script writen by Patrick Mylund Nielsenthat extracts all unique email addresses from a file. It follows a regular expression pattern based on the RFC 2822 standardand should thus return all valid email addresses regardless of how they appear in the file. For example, EmailsFromFile will distinguish between separate email addresses in a comma-separated list of values, such as a CSV file containing names, addresses, phone numbers and email addresses.

### Usage
```
 python emailsfromfile.py <filename> [separator] [encoding]
```


## UUIDsFromFile
A Python script that extracts all unique UUIDs from a file. It follows a regular expression pattern.

### Usage
```
 python uuidsfromfile.py <filename> [separator] [encoding]
```