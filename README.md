# Google sheet custom functions using Python and its libraries

## Objective 
To create custom functions for niche tasks which usually tasks input from google spreadsheet and then are processed in using Python, making the process more streamlined and simple for any user who is familiar with basic spreadsheet manipulation.

## Tools used
- Google spreadsheets
- Python
  - FastAPI package
  - Shapely package
  - Pycharm IDE
- AppScript (Basic)
- Version control - Git using GitHub
- Deployment using Heroku

## Design Architecture
The tools will include 2 services
1. Google spreadsheets
   - We will build a custom function using Google's AppScript which will let us send http requests to a API, to which we will send our input(s), in response we shall get the required output directly in spreadsheet cell.
2. An API
   - With the help of FastAPI we will build and API that will essential ease up the calculation (as it will have the capacity to utilize Python's package) and let the end user use this directly in spreadsheet without ever worrying about learner how to create complex code.

## Learnering from this exercise
- Creating and API
- Version Control using Git
- Deployment of web-app
- Creating custom google sheet function
- Foundation for further automation

## Walkthrough
[![Watch the video](https://img.youtube.com/vi/wh6j2vPPmDg/maxresdefault.jpg)](https://youtu.be/wh6j2vPPmDg)
