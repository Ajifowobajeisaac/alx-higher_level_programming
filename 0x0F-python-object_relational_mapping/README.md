Python - Object-relational Mapping

Description

This project explores the integration of Python with MySQL databases, focusing on Object-relational Mapping (ORM) using SQLAlchemy and MySQLdb. The project aims to bridge the gap between databases and Python, allowing for efficient data manipulation and querying without the need for writing SQL queries.

Project Overview

The project is divided into two parts:

Direct Database Manipulation: Using MySQLdb to connect to a MySQL database and execute SQL queries directly from Python scripts.
Object-relational Mapping with SQLAlchemy: Implementing ORM to abstract database storage and focus on object manipulation in Python.
Learning Objectives

Understand the basics of Python programming.
Learn how to connect to a MySQL database from Python.
Perform basic data operations (SELECT, INSERT) on MySQL using Python.
Understand and implement Object-relational Mapping (ORM).
Map Python classes to MySQL tables.
Create Python Virtual Environments.
Requirements

Python 3.8.5
MySQLdb version 2.0.x
SQLAlchemy version 1.4.x
Ubuntu 20.04 LTS
Setup

Install Dependencies
Python 3.8 and MySQL should be installed on Ubuntu 20.04.
Install MySQLdb and SQLAlchemy using pip:
Copy code
sudo pip3 install mysqlclient
sudo pip3 install SQLAlchemy
Database Setup
MySQL server should be running on localhost at port 3306.
Relevant databases and tables should be set up as per the project instructions.
Project Tasks

Get all states: Script to list all states from the database.
Filter states: Script to filter states with names starting with 'N'.
SQL Injection prevention: Enhance scripts to prevent SQL injection.
Cities by states: Script to list all cities from a specific database.
All cities by state: Enhanced script to list cities by state.
ORM setup: Setting up ORM with SQLAlchemy.
List states via SQLAlchemy: Script to list all states using SQLAlchemy.
First state: Script to print the first state object from the database.
Contains 'a': List all states containing the letter 'a'.
Get a state: Script to display a state object with a specific name.
Add a new state: Script to add a new state to the database.
Update a state: Script to update the name of a specific state.
Delete states: Script to delete states with a name containing 'a'.
Cities in state: Define the class for City and list cities by state.
City relationship: Improve City and State classes to establish relationships.
List relationship: List all states and corresponding cities.
From city: List all city objects from the database.

Author
Isaac Ajifowobaje
