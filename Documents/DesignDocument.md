# Design Document

## WSU Academic Research Hub
--------
Prepared by:

* `Alexander Larsen`,`Voiland College`
* `Erick Pairault`,`Voiland College`
* `Gabriel Muccillo Hartz`,`Voiland College`
* `Calell Figuerres`,`Voiland College`
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [WSU Academic Research Hub](#your-project-title)
  - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

### Document Revision History

| Name       | Date       | Changes       | Version    |
| ---------- | ---------- | ------------- | ---------- |
| Revision 1 | 2021-10-05 | Initial draft | 1.0        |


# 1. Introduction

Explain the purpose for providing this design document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief). 

Then provide a brief description of your project and state your project goal.

At the end of the introduction, provide an overview of the document outline.

[Section II](#2-architectural-and-component-level-design) includes …

[Section III](#22-subsystem-design) includes …

# 2.	Architectural and Component-level Design
## 2.1 System Structure

![](./images/UML%20Component.png)

Our app uses the Model-View-Controller architecture. The Model contains the table definitions (tables and the columns within that those tables). The View contains the markup that the user sees; the user interface. The Controller handles user interactions received from the View, processes the received data, and updates the Model (and tells the view to refresh, accordingly).

The MVC architecture handles decomposition for us, as each system is separate from the others and (theoretically) could be replaced with an equivalent and the app would still work correct. Moreover, each subsystem (the separate model, view, and controller) utilizes, in some way, the other, but does not strictly depend on the *way* one or both of its siblings works in order to function properly.

## 2.2 Subsystem Design 

(**Note1**: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

(**Note2**: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document in iteration-2 and make changes  and/or add more details in iteration-2.)

### 2.2.1 Model

Briefly explain the role of the model. 

(***in iteration-1***) Include a list of the tables (models) in your database and explain the role of each table. Provide the attributes of the tables (including relationships). 

(***in iteration -2***) Revise the database model. Provide a UML diagram of your database model showing the associations and relationships among tables. Your UML diagram should also show the methods of your models.

### 2.2.2 Controller

The main role of the Controller is to form the connection between the users input in the applciation to the database where it can be stored and remember. It's other main role is to navigate the user through the application. Within our Controller, we have auth_forms, auth_routes (both contain the input fields and navigation for authenticaion), forms, and routes.

The role of the routes files is to send the user to the correct navigation page with the correct form loaded when needed. Upon a Post request after a users input is valdiated, the routes should input the valdiated fields into the database. 

The role of the forms files is to create the input fields and sanitze the users input to make sure it isn't malicious. These input fields are stored in a form the routes can access and use.

Furthermore on our forms, all the fields included in these files are identical to the attributes found in the models section above. Any attribute that has a DataRequired validator will be found in the form for the users input, and the other fields not required will be added later on. For example, in the next iteration, professor will have a positions attribute that will be dedicated to holding all the positions the professor has created. However, this attribute will not be added upon registration because it is not required. 

#### Iteration 1 Routes

|    | Methods           | URL Path              | Description        |
|:--:|:-----------------:|:---------------------:|:------------------:|
| 1. | `GET`, `POST`     | `/`                   | Shows the homepage |
| 2. | `GET`             | `/register`           | Shows a screen to pick between a student and professor account |
| 3. | `GET`, `POST`     | `/register/student`   | Shows a form to register as a student, and also accepts the submission of that form and processes it 
| 4. | `GET`, `POST`     | `/register/professor` | Shows a form to register as a professor, and also accepts the submission of that form and processes it |
| 5. | `GET`, `POST`     | `/postposition`       | Available only to professors, it shows a form to create a research position in addition to accepting and processing it |
| 6. | `GET`, `POST`     | `/login`              | Shows a form to log in to the application |

#### Iteration 2 Routes

|    | Methods           | URL Path              | Description        |
|:--:|:-----------------:|:---------------------:|:------------------:|
| 1. | `GET`, `POST`     | `/createapplication `                   | Available only to students, it shows a form to create a application for a position the student navigated to |
| 2. | `GET`           | `/displaypositions`           | Page where students can navigate to view all positions posted |
| 3. | `GET`, `POST`     | `/position`   | Page where students navigate to view the details of a specific position 
| 4. | `GET`     | `/viewallstudents` | For professors when they navigate to see who applied for their positions|
| 5. | `GET`     | `/viewstudent`       | For professors who picks an individual student to view from viewallstudents|
| 6. | `GET`     | `/mypositions`              | For professors to see all the positions they have created |

### 2.2.3 View and User Interface Design 

Briefly explain the role of the view. Explain how you plan to build the user interfaces and mention the frameworks/libraries you plan to use (e.g., Bootstrap).  

Provide a list of the page templates you plan to create (or you already created). Briefly describe the information that will be displayed on those pages and the forms that will be rendered (i.e., explain the input and output for each page). Make sure to mention which use-cases in your “Requirements Specification” document will utilize these interfaces for user interaction. You can supplement your description with UI sketches or screenshots. 

(***in iteration-1***) Brainstorm with your team members and identify the pages that you think should be created.  If you included most of the major pages, it will be acceptable. 

(***in iteration-2***) Revise your page list and descriptions and include any additional pages that you will include in your view.  In iteration-2, you will be deducted points if your view description is still superficial and doesn't list and explain all pages of your application. 


# 3. Progress Report

With iteration completed, in terms of use cases, we have finished with student registration, professor registration, login/logout for both types of users, and our app can create a position through the professor user. With these done we are currently on track. However, we have done much more work in the backend of our app that is not implemented yet including creating the model for application and setting up the neccesary database relationships (i.e. professor to position, languages to student and to position, interests to student and to position, and vice versa). We've also successfully created a polymorphic user that student and professor both inherit from. 

Our UI, previously using various libary tools from the latest bootstrap will now use, will now use a specific flask-bootstrap libary. This will make UI design quicker and better.

Looking forward to iteration two, we plan to shift our focus to positions and the applications created for them. This will include professors being able to view their posted positions, allowing students to view a positions details, allowing students to create an application for a position, allowing professors to view which students applied to each postion, and allowing professors to view each individual student application. 

# 4. Testing Plan

(***in iteration 1***)
Don't include this section.

(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? 
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)

  For testing, we plan to test differently for each section of work. When changing the database and seeing if we can create certain objects, we will be doing query statements in python and creating the object manually. In the last iteration, most of our testing was done through the app itself where multiple functionality pieces were tested. For example, when seeing if the forms, routes, and UI worked correctly for a use case like student registration, we would merge all the work out team did into our UI branch and through trial and errors we would polish up the code to get a working version on the app. 

# 5. References

None