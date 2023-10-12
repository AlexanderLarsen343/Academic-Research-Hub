# Software Requirements Specification

## 
--------
Prepared by:

* `Alexander Larsen`, `Voiland College`
* `Erick Pairault`, `Voiland College`
* `Gabriel Muccillo Hartz`, `Voiland College`
* `Calell Figuerres`, `Voiland College`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name       | Date       | Changes       | Version    |
| ---------- | ---------- | ------------- | ---------  |
| Revision 1 | 2023-10-05 | Initial draft | 1.0        |

----
# 1. Introduction

This is an application where students can find job positionings demanding a certain set of skills that are posted by professors. To create such application, we will used Flask as our base functionality, SQL alchemy for our database, HTML for templates, CSS for styling, and maybe Bootstrap for more styling. 

## 1.1 Document Purpose

The purpose of this document is to create a foundation of ideas of our project to make sure all group members are on the same page.

## 1.2 Product Scope

The purpose of our application is to create a convient and easy connection between professors creating research opportunities and students for looking those oppotunities. Both parties should be able to have a secured account with login. Professors will be able to post opportunities and view student applications. Students will be able to browse posted opportunities and apply. 

## 1.3 Document Overview

The rest of the document will go indepth on both functional and nonfunctional requirements. Going over what the end goal is for each user, we will create a list of use cases that will then shape the functionality of our system.

----
# 2. Requirements Specification
This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

## 2.1 Customer, Users, and Stakeholders

The main users of this application will be students and professors. The customer and stakeholer in this scenario will be the instituion that makes use of this software.

----
## 2.2 Use Cases

This section will go over all use case for all iterations of the project. Each use case will be either from the perspective of the professor or student.

For each use case you should have the following:

* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).

Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.

You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.

| Use case # 1      |As a student, I want to be able to register an account|
| ----------------- |--|
| Name              | Add registration  |
| Users             | Student  |
| Rationale         | A student needs to be able to create an account  |
| Triggers          | A student navigates to registration  |
| Preconditions     | Account cannot already exist when registering.   |
| Actions           | 1. A student chooses on the "Sign in" option <br> 2. System displays login page <br> 3. User selects register option <br> 4. System displays register form <br> 5. User inputs information like username, password, and email. <br> 6. System will check validation of submission (character limitations and required fields) <br> 7. If passed validation, a new user account will be created for the student and their information stored in the system <br> 8. System will notify the user that their account has been created |
| Alternative Path  | If the account already exists, then the user will just be redirected to the same page upon submission. |
| Postconditions    | Student account is now in the database  |
| Acceptance tests  | Add a student either in python or through the app and query the database manually  |
| Iteration         | Iteration 2  |

| Use case # 2      |  As a user, I want to be able to log into my account |
| ------------------ |--|
| Name              | Add Login  |
| Users             | Student  |
| Rationale         | Accounts have all your information and are how students apply to positions. They must be able to login to access these features |
| Triggers          |  Student navigates to login page |
| Preconditions     | Page is already loaded and student is not already signed in |
| Actions           |  1. Student enters into the signin page <br> 2. System displays login page <br> 3. Student enters their username and password in appropiate fields <br> 3.  System will check validation of submission (character limitations and required fields)<br> 4. If succesfull, Student is redirected to the homepage and issued a flash message of their account sign in|
| Alternative paths | Submission is invalid and student is navigated to the same login page with errors  |
| Postconditions    | Student user is now in their account  |
| Acceptance tests  | Test via creating a user and logging in  |
| Iteration         | Iteration 2  |

| Use case # 3      | As a student, I want to review the open positions|
| ------------------ |--|
| Name              | Add position review|
| Users             | Student |
| Rationale         | Students must be able to search and see applications to apply to them|
| Triggers          | Students navigate to the applications page |
| Preconditions     | Student is signed in and the page is loaded correctly|
| Actions           |1. Student navigates to the applications page <br> 2. System displays applications page<br> 3. Student can choose their interests of what they are looking for <br> 4. System will reorder applications to preferences |
| Alternative paths | Student is not signed in and is redirected to the login page when trying to enter the applications page|
| Postconditions    | Student can view the applications they want |
| Acceptance tests  |Go into the website with a student user with applications already created by faculty, and see if applications display correctly and if they can be ordered to preference.|
| Iteration         | Iteration 1|

| Use case # 4      | As a student, I want to read an applications details and descriptions|
| ------------------ |--|
| Name              | Add application details |
| Users             | Student |
| Rationale         | When looking for positions, a student needs to be able to see the qualifications and details of each position|
| Triggers          | Student navigates to the applications page |
| Preconditions     | Student is signed in, page is already loaded, and the student may click on the application for more details |
| Actions           | 1. Student navigated to the applications page <br> 2. System displays applications page <br> 3. Student chooses an application to view <br> 4. System displays all application details |
| Alternative paths | Student is not signed in and is sent to the login page when trying to navigate into the applications page|
| Postconditions    | Application details shown on page |
| Acceptance tests  | Go into the website and check if the student can see basic application information on the applciations page. Then, enter a specific application and see if the application details are all viewable and correct.|
| Iteration         |Iteration 1 |

| Use case # 5      | As a student, I want to be able to apply to research positions  |
| ------------------ |--|
| Name              | Apply for research positions.  |
| Users             | Students.  |
| Rationale         | A student needs to be able to apply for a research position.  |
| Triggers          | A student chooses to apply for a research position.  |
| Preconditions     | The student has not yet applied to the position.  |
| Actions           | 1. The student selects a research position that is posted. <br> 2. The software displays the position information and the option for the student to apply. <br> 3. The student selects “Apply for postion” for the positions they desire. <br> 4. The software updates the user's current list of applied positions, the software updates the current list of users that applied for the postion. <br> 5. The student is alerted that they are now sucessfully applied for the position.  |
| Alternative paths | 1. In Step 3 the student does not apply for the position and comes back to the home page. <br> 2. In step 5 the application coudn't handle the student's request and alerts that the application was not sucessful.  |
| Postconditions    | The software updates the user's current list of applied positions, and the current list of users that applied for the postion.  |
| Acceptance tests  | 1. Search in the database model for the student if they are applied for the desired position. <br> 2. Search in the database model for research position if the student is listed in the applicants.  |
| Iteration         | Iteration 1  |

| Use case # 6      | As a student, I want to be able to see the status of my applied applications |
| ------------------ |--|
| Name              | Check current state of applied positions.  |
| Users             | Students  |
| Rationale         | A student needs to be able to view the research positions they already applied to and check the statuses of their applications.  |
| Triggers          | A student chooses to see the current positions they applied for.  |
| Preconditions     | The page containing the current positions applied for a student is already loaded.  |
| Actions           | 1. The student selects the option to view their current applied positions. <br> 2. The software imports the list of positions from the database that matches the one from the current student. <br> 3. The software displays the list of positions applied and the status of each of the positions which include: Pending, Approved for Interview, Hired, and Not Hired. |
| Alternative paths | 1. In Step 2 the application could not handle the student's request and alerts the student that the data could not be retrived.  |
| Postconditions    | The software displays the list of positions applied and the status of each of the positions.  |
| Acceptance tests  | 1. Check the status of the response to the request made by the student to the server.  |
| Iteration         | Iteration 3  |

| Use case # 7      | As a student, I want to be to able to pull out of an application I applied to |
| ------------------ |--|
| Name              | Withdraw from current applicaitions.  |
| Users             | Students.  |
| Rationale         | If the student is no longer interested in a research position, they can withdraw their application.  |
| Triggers          | A student chooses to withdrawn from a position that they applied for in the past.  |
| Preconditions     | The student is currently applied for a position.  |
| Actions           | 1. The student selects the option to view their current applied positions. <br> 2. The software imports the list of positions from the database that matches the one from the current student.<br>3. The software displays the list of positions applied and the status of each of the positions which include and the option for the student to withdraw from the position.<br>4. The student selects the option to withdraw from the desired position.<br>5. The application updates the database with the new status for the current student applications and the target position applicants.<br>6. The application reloads the page with the updated list of positions applied for the student.|
| Alternative paths | 1. In Step 6 the application could not handle the student's request and alerts the student that they could not withdraw sucessfully from the desired applicaition.  |
| Postconditions    | The software displays the updated list of positions applied.  |
| Acceptance tests  | 1. Check the status of the response to the request made by the student to the server.  |
| Iteration         | Iteration 3  |

| Use case # 9      | As a faculty member, I want to be able to create an account |
| ------------------ |--|
| Name              | Create a faculty account and enter profile information.  |
| Users             | Faculty.  |
| Rationale         | Set a faculty account with username and password, name, last name, WSU ID, email, and phone.  |
| Triggers          | A member of faculty that does not have an account chooses to create one.  |
| Preconditions     | The faculty member does not have an account registered in the system.  |
| Actions           | 1. The user enters the website and is prompted to log in or register. <br> 2. The user chooses the register option and is redirected to the register page. <br> 3. A form is displayed for the user to input their information. <br> 4. The form is validated and its information is uploaded to the database, the user is considered to be registered in the system. <br> 5. The user is redirected to the login page and alerted that the they were sucessfully registered.
| Alternative paths | 1. In Step 4 the form could not be validated and the user is flashed with the errors returned by the flask-form. <br> 2. The user is redirected to the register page.  |
| Postconditions    | The user is now registered in the system, with the updated database carrying their data.  |
| Acceptance tests  | 1. Check the status of the response to the request made by the user to the server.  |
| Iteration         | Iteration 3  |

| Use case # 10      | As a faculty member, I can register an account |
| ------------------ |--|
| Name               | Add faculty registration |
| Users              | Faculty members |
| Rationale          | Faculty members need to be able to register accounts |
| Triggers           | Faculty member chooses registration option |
| Preconditions      | Registration page is already loaded |
| Actions            | 1. Faculty member enters registration page 2. The system shows the user the registration page <br> 3. Faculty member gives name, email, password, etc. <br> 4. Backend validates input values <br> 5. If validation passes, a new faculty account is created and stored <br> 6. The system redirects the user to the login page, saying their account has successfully been created |
| Alternative Path   | A faculty member attempts to sign in using unknown credentials, they'll be prompted if they want to register |
| Postconditions     | Faculty account is now in database |
| Acceptance tests   | Added faculty member in Python or through app and query database |
| Iteration          | Iteration 2 |


| Use case # 11      | As a faculty member, I want to be able to login to my account |
| ------------------ |--|
| Name               | Add login |
| Users              | Faculty members |
| Rationale          | Accounts have all user information and how faculty create applications; therefore, they must be able to login |
| Triggers           | Faculty member navigates to login page |
| Preconditions      | Page is loaded and they're not already signed in |
| Actions            | 1. Faculty member navigates to sign in page <br> 2. The system shows the user the sign in page <br> 3. They enter their username and password <br> 4. Backend validates input and queries database for matching identity <br> 5. If successful, faculty member is navigated to home page and logged in |
| Alternative Path   | Validation fails and they're redirected to the same page with errors shown |
| Postconditions     | Faculty member is now logged in |
| Acceptance tests   | Create a user and attempt to log in |
| Iteration          | Iteration 2 |


| Use case # 12      | As a faculty member, I want to create undergraduate research positions |
| ------------------ |--|
| Name               | Add research position creation |
| Users              | Faculty members |
| Rationale          | Faculty members want to be able to create UG research positions of undergrads to apply for |
| Triggers           | Faculty member navigates to undergrad research position creation page |
| Preconditions      | The page is loaded; the signed-in user is a faculty member |
| Actions            | 1. Faculty member navigates to research position creation page <br> 2. The system shows the faculty member the position creation form <br> 3. Member provides application info (title, description, start/end date, etc.) <br> 4. Backend validates member's inputs <br> 5. If successful, the application is added to the database |
| Alternative Path   | Validation fails and they're redirected to the same page with errors shown |
| Postconditions     | A new research position application is created |
| Acceptance tests   | Create a research position application |
| Iteration          | Iteration 1 |

| Use case # 13      | As a faculty member, I want to be able to view a students qualifications to see if they fit the position |
| ------------------ |--|
| Name              | View Student Qualifications  |
| Users             | Faculty Users  |
| Rationale         | A faculty user should be able to view the qualifications of a student to make an informed decision as to whether or not they should proceed with approving them for an interview.  |
| Triggers          | The faculty selects “View Student Qualifications”.  |
| Preconditions     | Student(s) have applied for the research position, and the student(s) have all the appropriate criteria filled out.  |
| Actions           | 1. The user selects “View Student Qualifications”.<br>2. The software displays the student’s GPA, technical elective courses they have taken, research topics they are interested in, programming languages they have experience with, and prior research experience.  |
| Alternative paths | 1. After step 2, the user may choose to close the page that displays the student’s qualifications.  |
| Postconditions    | The student’s information is displayed to the faulty user.  |
| Acceptance tests  | Make sure that the student’s information that is displayed correctly contains their GPA, technical elective courses, research topics, programming language, and prior research experience.  |
| Iteration         | Iteration 2  |

| Use case # 14      | As a faculty member, I want to be able to approve or reject a student's application  |
| ------------------ |--|
| Name              | Approve for Interview  |
| Users             | Faculty Users  |
| Rationale         | A faculty user after having reviewed a student’s profile, should be able to have the ability to approve or decline the student for an interview. This is also relevant for the student who should be able to check their application later to see if they were accepted or not for an interview.  |
| Triggers          | The faculty selects the “Approve/Decline for interview” option.  |
| Preconditions     | There are student applications for the research position the faculty has posted/ is looking at.  |
| Actions           | 1. The user selects a research position they have posted.<br>2. The software displays the list of students who have applied for the position.<br>3. The faculty selects “Approve/Decline for interview” for the application(s) they desire.<br>4. The software asks for confirmation from the user.<br>5. The user selects their choice.<br>6. The software updates the application(s) according to the choice.  |
| Alternative paths | 1. In step 3, the user can select multiple applications to Approve or Decline for interview at a time. In the case they choose multiple, the software will specify all the applications that have been selected for Approval/Rejection for confirmation.<br>2. In step 5, the user can select to not confirm their selection the software will return to the list of students that have applied for the position.  |
| Postconditions    | Student Applications for the research position will have “Approved/Rejected for interview” updated on their application.  |
| Acceptance tests  | Make sure that all applications the user accepted or rejected have been appropriately displayed on their profile.  |
| Iteration         | Iteration 3  |


| Use case # 15      | As a faculty member, I want to be able to I want to be able to change the status of an application.  |
| ------------------ |--|
| Name              | Update Status of Application  |
| Users             | Faculty Users  |
| Rationale         | A faculty user after having interviewed a student, should be able to have the ability to hire or reject a student for the position. This is also relevant for the student who should be able to check their application later to see if they were accepted or not for the research position.  |
| Triggers          | The faculty selects the “Hire/Decline” option. |
| Preconditions     | There are student applications for the research position the faculty has posted, and the application the user is looking at has already been “Approved for Interview”. |
| Actions           | 1. The user selects a research position they have posted.<br>2. The software displays the list of students who have applied for the position.<br>3. The user selects a student application that has already been “Approved for Interview”.<br>4. The software displays the student application.<br>5. The user selects “Update Status of Application”.<br>6. The software asks “Hire/Decline”.<br>7. The user selects their choice.<br>8. The software asks for confirmation from the user.<br>9. The user selects their choice.<br>10. The software updates the application according to the choice.  |
| Alternative paths | 1. In step 3, the user may select an application that has not been “Approved for Interview” and in this case when the user selects “Update Status of Application” the software will not display the options to “Hire/Decline”.<br>2. In step 9, if the user chooses to not confirm their choice the software will return to the student application.  |
| Postconditions    | Student Applications for the research position will have “Hired/Declined” updated on their application.  |
| Acceptance tests  | Make sure that all applications the user hired or declined have been appropriately displayed on their profile.  |
| Iteration         | Iteration 3  |


| Use case # 16      | As a faculty member, I want to be able to take down positions I posted |
| ------------------ |--|
| Name              | Delete Research Position  |
| Users             | Faculty Users  |
| Rationale         | A faculty user may need to delete a research position because all the slots are filled, there wasn’t enough funding, or because an error that requires the position to be removed.  |
| Triggers          | The faculty selects “Delete Research Position”.  |
| Preconditions     | The research position already exists.  |
| Actions           | 1. The user selects “Delete Research Position”.<br>2. The software asks for confirmation from the user.<br>3. The user selects “yes”.<br>4. The software removes the research position and updates all the applications for the position. |
| Alternative paths | 1. In step 3, the user may select no, and the software returns to the research position page.  |
| Postconditions    | The research position doesn’t exist and application for the position show “Position is not available”.  |
| Acceptance tests  | Make sure that the research position no longer appears and that on the status of all applications it is stated “Position is not available”.  |
| Iteration         | Iteration 3  |
----
## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. [Enter a Concise Requirement Name]:  [provide a concise description, in clear and easily understandable language to specify the requirement]

----
# 3. User Interface

Here you should include the sketches or mockups for the main parts of the interface.
![](/Requirements%20Document%20Images/1.jpg "1.jpg")
![](/Requirements%20Document%20Images/2.jpg "2.jpg")
![](/Requirements%20Document%20Images/3.jpg "3.jpg")
![](/Requirements%20Document%20Images/4.jpg "4.jpg")

----
# 4. Product Backlog

Link to Git Repo Issues: https://github.com/WSU-CptS-322-Fall-2023/termproject-mowthelawn/issues

----
# 4. References

No references yet

----
----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 

| Max Points  | **Content** |
| ----------- | ------- |
| 10          | Do the requirements clearly state the customers’ needs? |
| 5           | Do the requirements avoid specifying a design (note: customer-specified design elements are allowed; non-functional requirements may specify some major design requirements)? |
| | |  
|    | **Completeness** |
| 25 | Are use cases written in sufficient detail to allow for design and planning? |
| 4 | Do use cases have acceptance tests? | 
| 25 | Is your use case model complete? Are all major use cases included in the document? |
| 10 |  Are the User Interface Requirements given with some detail? Are there some sketches, mockups?  |
| | |  
|   | **Clarity** |
| 5 | Is the document carefully written, without typos and grammatical errors? |
| 4 | Is each part of the document in agreement with all other parts? |
|   | Are all items clear and not ambiguous? (Minor document readability issues should be handled off-line, not in the review, e.g. spelling, grammar, and organization). |
|   |   |
|    | **GitHub Issues** |
| 12 | Has the team setup their GitHub Issues page? Have they  generated the list of user stories, use-cases, created milestones, assigned use-cases (issues) to milestones?   Example GitHub repo (check the issues): https://github.com/WSU-CptS322-Fall2022/TermProjectSampleRepo/issues  |

