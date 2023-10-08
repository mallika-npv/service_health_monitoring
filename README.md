# service_health_monitoring
## Overview
The Service Health Monitoring System is a robust web application designed to oversee the operational status of web services hosted on a server. 
It empowers users to monitor one or more services and gain valuable insights into the historical uptime and downtime patterns of these web services over the past 30 days. 
This document provides comprehensive information on the system's functionalities, guiding developers and users alike on its usage and capabilities.

## Features
### 1. User Registration and Authentication
Implement a user-friendly registration page allowing new users to create accounts securely.
Create a login interface enabling registered users to enter their username and password securely, ensuring authentication.

### 2. Dashboard
Design an intuitive dashboard where users can monitor the health of services in real-time.
Display the operational status (up or down) of each service dynamically.
Include a section for users to select and monitor specific services tailored to their needs.
Present service data visually and informatively, utilizing color-coded indicators (green for up, red for down) to provide a quick and clear overview.

### 3. Search Feature
Create a robust search functionality enabling users to search for services that experienced downtime for more than 5 minutes within the last 30 days.
Implement filters and date pickers, enhancing the search experience by allowing users to refine their searches based on specific criteria and time frames.

### 4. Notifications
Implement email notifications using a reliable service.
Configure the system to send email notifications to users when a service remains down for an extended period, ensuring timely awareness and action.

## Getting Started
For setting up this project in your PC.

### Prerequisites:
1. 'HTML' and 'CSS' for the front end
2. 'Django' for the backend
3. 'JS' integrated in HTML for function calls and notification api

### Installation:
Clone this repository to your local machine.
In your temimal enter : python manage.py runserver

### Issues and Developements
1. Created a dummy server with a few services
2. develope a graph representation of the data available
