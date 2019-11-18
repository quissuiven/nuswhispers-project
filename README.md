
# Analysis of student confession page NUSWhispers
NUSWhispers is the popular student confession page of the National University of Singapore.
In this project, we will scrape information of 44438 texts from https://nuswhispers.com/latest/, clean the data and perform NLP algorithms to answer the following questions: 
  - When did Prof Ben become popular and what topics do people ask him about?
  - What are the most popular modules students ask and share about?
  - What are the most popular topics that people talk about on NUSWhispers?
  - Over the years, do people get more positive or negative about finding jobs?
  - How do students feel during school semesters and how does it change nearing the exams?

We will create data visualizations to answer the questions, as well as deploy a web application for the general public to read.

### Folder Structure
  - '1. Text Analysis' contains all the files required to acquire, clean, analyze and visualize the text data
    -  '1. Text Analysis/models' contains the NLP models used in the analysis
    -  '1. Text Analysis/src' contains the scripts used to scrape, analyze and visualize the data:
       > '1. Text Analysis/src/webscraping.py' scrapes 6 content variables from 44438 urls
       > '1. Text Analysis/src/Exploratory Analysis & Experimentation.ipynb' conducts data cleaning and preliminary analysis
       > '1. Text Analysis/src/utils.py' stores all the essential functions from the preliminary analysis
       > '1. Text Analysis/src/Sentiment Analysis.ipynb' conducts in-depth sentiment analysis and visualization
       > '1. Text Analysis/src/Entity Extraction.ipynb' conducts in-depth entity extraction and visualization
       > '1. Text Analysis/src/Topic Modeling.ipynb' conducts in-depth topic modeling and visualization
  - '2. Web Application' contains all the files required to deploy a web application
    -  '2. Web Application/venv' contains the files needed to initialize a virtual environment  
    -  '2. Web Application/requirements.txt' contains the libraries to be built inside the virtual environment
    -  '2. Web Application/static' contains css and images of the visualizations made in the Text Analysis
    -  '2. Web Application/templates' contains the html files for each of the webpages
    -  '2. Web Application/main.py' is the backend Flask code that renders all the html pages
