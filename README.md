# Summer Camp Timetable and Schedule Generator

## Overview

Welcome to the Summer Camp Timetable and Schedule Generator! This tool is designed to automatically create timetables and schedules for different groups in a summer camp setting, and saves them automatically in a word document. Using this tool, you can efficiently manage and organize activities, ensuring a balanced and diverse schedule for all groups.

## Features

* Automated Scheduling: Generates schedules based on predefined rules and constraints.
* Activity Diversity: Ensures that each group participates in a wide variety of activities throughout the week.
* Conflict Avoidance: Prevents scheduling conflicts such as overlapping activities or repeated activities on the same day.
* Word Document Export: Automatically saves the generated schedules in a Word document format for easy distribution and printing.

## Schedule Structure

Each group has a daily schedule divided into six periods:

* Morning: 2 periods dedicated to sports.
* Afternoon: 4 periods, consisting of:
    * Lunch
    * Swim
    * 2 sports activities

Note: Lunch and swim are fixed at the same period every day.

## Application

While the primary use case for this tool is summer camps, it can also be adapted for use in other settings such as:
     
* Schools: For creating class schedules
* Organisations: For planning team activities or workshops.
* Sports Clubs: For scheduling training sessions and matches.

## Installation and Usage

* Prerequisites
    * Python 3.x
    * PyQt5
    * Python-docx
    * python-copy

1.Clone the Repository.

2.install the dependencies
* pip install PyQt5

## Usage

1. Run the program
        Excecute the ui.py file to launch the app
2. Generate Schedule
    *Open the application interface.
    *Input the required activity details.
    *Click on the "Generate Schedule" button.
    *The generated schedule will be automatically saved in a Word document.

*Note: If the document does not successfully generate, ensure that you specify the path where you want your schedules to be saved, this includes the pre-existing 2024 Template table in 'word.py'.*

## User Interface

The simple user interface is designed using QTDesigner.

## Screenshot


## Contribution

I welcome contributions to enhance the functionality and features of this tool.

## Contact

abdulngui718@gmail.com


