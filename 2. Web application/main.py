# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:29:43 2019

@author: Hong.Wen.Tai
"""

#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
#from weather import query_api
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#define home page route and corresponding function
@app.route('/')
def home():
    return render_template('home.html')
    
#define function that receives data posted to server and redirects to different links
@app.route("/managelinks" , methods=['GET', 'POST'])               
def manageLinks():
    #print(request.form)
    rating = request.form.get("rating") 
    if rating == "1":
        return redirect(url_for('link1'))
    elif rating == "2":
        return redirect(url_for('link2'))
    elif rating == "3":
        return redirect(url_for('link3'))
    elif rating == "4":
        return redirect(url_for('link4'))
    elif rating == "5":
        return redirect(url_for('link5'))

#define routes and functions for each link
@app.route("/profben" , methods=['GET'])
def link1(): 
    return render_template('profben.html') 

@app.route("/modsandcourses1", methods=['GET'])
def link2(): 
    return render_template('modsandcourses1.html') 
    
@app.route("/populartopics", methods=['GET'])
def link3(): 
    return render_template('populartopics.html') 

@app.route("/jobsentiment" , methods=['GET'])
def link4(): 
    return render_template('jobsentiment.html')    
    
@app.route("/semestersentiment" , methods=['GET'])
def link5(): 
    return render_template('semestersentiment.html') 

@app.route("/modsandcourses2" , methods=['GET'])
def link6(): 
    return render_template('modsandcourses2.html') 

if __name__=='__main__':
    app.run(debug=True)