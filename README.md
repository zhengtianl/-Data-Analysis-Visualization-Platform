## Project Overview


## Structure
├── [src/](https://github.com/zhengtianl/comp90024groupwork/blob/9e443f16204ebad055c398bb17c5c23876b74b1d/src)                       # src code

├── [src/ansible/](https://github.com/zhengtianl/comp90024groupwork/blob/9e443f16204ebad055c398bb17c5c23876b74b1d/src/ansible%20new)                    # User/system tests

├── [src/Backend/](https://github.com/zhengtianl/comp90024groupwork/blob/9e443f16204ebad055c398bb17c5c23876b74b1d/src/Backend)  

├── [src/CouchDB/](https://github.com/zhengtianl/comp90024groupwork/blob/9e443f16204ebad055c398bb17c5c23876b74b1d/src/CouchDB)    

└── README.md (this file must be updated at all times. please, make sure you explain your github structure here and generate changelogs for each sprint before you tag it)

# Branching Strategy
1. Make sure a branch is created for each User Story Epic, and accountable developers should only implement the code in the corresponding branch.
2. Pull requests will be issued for merging the branches to main.
3. Code review should be hosted every time before different branches merged to main.

# Code Review Checklist
1. [x] /sentiment
2. [x] /alcohol
3. [x] /count
4. [x] /authorid


## Frontend User Guide

### 1. Installation and Configuration

First, make sure your computer has the necessary frontend development environment installed. Follow these steps for installation and configuration:

1. Download and install the latest version of Node.js: [https://nodejs.org](https://nodejs.org)
2. Install the package manager npm by running the following command in the command line: `npm install npm@latest -g`
3. Install project dependencies by running the following command in the project directory: `cd\src\FrontEnd\ npm install`
4. Configure the relevant settings for the project, such as API endpoints and authentication information.

### 2. Using the Frontend Application

Once your frontend environment is set up, you can use the frontend application by following these steps:

1. Start the application by running the following command in the command line: `cd\src\FrontEnd\ npm start`
2. Open your preferred web browser and visit the http://172.26.131.77:3000/ of the application.
3. Log in or register within the application.
4. Explore the different features and pages of the application and perform respective actions.
5. Refer to the accompanying help documentation if needed.

## Backend User Guide

### 1. Installation and Configuration

Before using the backend functionality, ensure that you have the necessary setup. Follow these steps for installation and configuration:

1. Install and configure the required backend dependencies, such as the programming language and framework specific to your project `cd\src\Backend\ . ./1.sh`.
2. Set up the database and ensure it is properly connected to the backend application.
3. see the data on ''
4. Configure any additional backend settings, such as server ports and API endpoints.

### 2. Using the Backend Application

Once the backend is properly set up, you can utilize its functionalities by following these steps:

1. Start the backend application or server using the appropriate command or script.
2. Ensure the backend application is running and properly connected to the frontend or any other client applications.
3. Implement any necessary authentication or authorization mechanisms as per your project requirements.
4. Make requests to the backend API endpoints using appropriate HTTP methods to perform CRUD (Create, Read, Update, Delete) operations or any other specified actions.
5. Handle and process any backend responses or errors within the frontend or client application as required.




## Frontend Page Rendering Test Cases



- Test Case ID: TC001
- Description: Verify that the home page is rendered correctly with all required components and data.
- Steps:
  1. [x] Navigate to the home page.
  2. [x] Check if the page title is displayed correctly.
  3. [x] Verify that the main content, such as posts or featured items, are rendered and visible.
  4. [x] Test the responsiveness of the page by resizing the browser window and ensuring that the layout adapts accordingly.
  5. [x] Check if any dynamic data, such as real-time updates or API fetches, are correctly displayed.



- Test Case ID: TC002
- Description: Verify that the profile page is rendered correctly with the user's information and relevant components.
- Steps:
  1. [x] Log in with valid credentials.
  2. [x] Navigate to the profile page.
  3. [x] Verify that the user's profile picture, username, and other details are displayed accurately.
  4. [x] Check if any editable fields, such as bio or profile picture upload, are functioning correctly.
  5. [x] Test the visibility of any user-specific content, such as private posts or followers, based on the user's permissions.



- Test Case ID: TC003
- Description: Verify that the search results page is rendered properly with relevant search data and filtering options.
- Steps:
  1. [x] Enter a search query in the search bar.
  2. [x] Click on the search button or press Enter.
  3. [x] Verify that the search results are displayed in a well-organized manner, showing relevant information for each result.
  4. [x] Test the functionality of filtering options, such as sorting by relevance or date.
  5. [x] Check if pagination is implemented correctly and allows navigation through multiple pages of search results.



- Test Case ID: TC004
- Description: Verify that the error page is rendered correctly when encountering unexpected errors or invalid URLs.
- Steps:
  1. [x] Manually enter an invalid URL or simulate an error condition.
  2. [x] Verify that the error page is displayed with an appropriate error message or description.
  3. [x] Test the visibility of any error-related information, such as error codes or contact support details.
  4. [x] Ensure that the error page provides a clear way to navigate back to the main pages or retry the operation.



