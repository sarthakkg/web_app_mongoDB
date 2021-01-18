# web_app_mongoDB
CRUD web application to manage and store subscribers and unsubscribers for email newsletters in Mongo DB. Send automated email to subscribers from database using Python MIMEText in HTML/CSS and plaintext from your email.

[![npm version](https://badge.fury.io/js/npm.svg)](https://badge.fury.io/js/npm)
![body-parser](https://img.shields.io/badge/body--parser-1.18.3-yellowgreen)
![express](https://img.shields.io/badge/express-4.16.4-blue)
![mongoDB](https://img.shields.io/badge/mongoDB-4.2-green)
![path](https://img.shields.io/badge/path-1.0-ff69b4)

** Great to manage your own email newsletters and subscribers in a database for free without paying an third-party email marketing company.**

## Installation
```bash
python get-pip.py
npm init -y
npm install body-parser
npm install express
npm install mongodb
npm install path

## Usage
Sets up a CRUD (create, read, update, delete) web application in Node JS. Web application allows users to fill in their contact information (name, email, status) to subscribe to email newsletters. User info is then updated in Mongo Database Atlas.

Python3 script sends email to all subscibed users from database. HTML/CSS is embedded within 
