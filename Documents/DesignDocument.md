# Design Document

## WSU Academic Research Hub
--------
Prepared by:

* Alexander Larsen, Voiland College
* Erick Pairault, Voiland College
* Gabriel Muccillo Hartz, Voiland College
* Calell Figuerres, Voiland College
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

| Name       | Date       | Changes             | Version    |
| ---------- | ---------- | ------------------- | ---------- |
| Revision 1 | 2023-10-23 | Initial draft       | 1.0        |
| Revision 2 | 2023-11-07 | Iteration 2 changes | 2.0        |

# 1. Introduction
This design document details the layout, structure, and purpose of each portion of our Academic Research Hub application. The goal of this project is to (among other things) connect students and faculty members with available research opportunities, as it is generally difficult for upper-division faculty members to connect with lower-classmen (i.e., freshmen and sophomores).

This document will discuss the system architecture, progress over time, and testing methodology for our application.

<!-- Explain the purpose for providing this design document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief). 

Then provide a brief description of your project and state your project goal.

At the end of the introduction, provide an overview of the document outline.

[Section II](#2-architectural-and-component-level-design) includes …

[Section III](#22-subsystem-design) includes … -->

# 2.	Architectural and Component-level Design
## 2.1 System Structure

![](./images/UML%20Component.png)

Our app uses the Model-View-Controller architecture. The Model contains the table definitions (tables and the columns within that those tables). The View contains the markup that the user sees; the user interface. The Controller handles user interactions received from the View, processes the received data, and updates the Model (and tells the view to refresh, accordingly).

The MVC architecture handles decomposition for us, as each system is separate from the others and (theoretically) could be replaced with an equivalent and the app would still work correct. Moreover, each subsystem (the separate model, view, and controller) utilizes, in some way, the other, but does not strictly depend on the *way* one or both of its siblings works in order to function properly.

## 2.2 Subsystem Design 

<!-- (**Note1**: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

(**Note2**: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document in iteration-2 and make changes  and/or add more details in iteration-2.) -->

### 2.2.1 Model

The role of the model is to create the organization of tables within our database to hold all of our data for the system and users. 

Our model, when it comes to users, has an parent User class that Student and professor models inherit from. This way, we can still use UserMixin correctly with one User object.

Our model also has some many-to-many and one-many relationships within their tables. For example, interests has a many-to-one relationship with Student, Professor, and Position thus far. 

|    | Models            | Description           | Fields             |
|:--:|:-----------------:|:---------------------:|:------------------:|
| 1. | User              | Parent class for Student and Professor, this model represents the website user and accordingly contains the basic information of for all types of users in the website.| `id`<br> `password_hash` <br> `firstname` <br> `lastname` <br> `email` <br> `phone` <br> `user_type` |
| 2. | Student           | Child class of User, this model represents the website student type of user. | `id` -> `Id` associated to the `User` parent class `id`. <br> `wsu_id` <br> `major` <br> `graduation` <br> `gpa` <br> `experience` <br> `applications` -> Establishes one-to-many relationship between a student and research position applications that are associated to them. <br> `interests` -> Establishes a many-to-many relationship between students and interests. <br> `languages` -> Establishes a many-to-many relationship between students and languages.|
| 3. | Interest          | Interests that student user type can associate to their profile/ Interests that can be associated to a position. | `id` <br> `name` <br> `studentInterests` -> Establishes many-to-many relationship between interests and students. <br>  `positionLanguages` -> Establishes many-to-many relationship between interests and positions.|
| 4. | Language          | Languages that student user type can associate to their profile/ Languages that can be associated to a position. | `id` <br> `name` <br> `studentInterests` -> Establishes many-to-many relationship between languages and students.<br> `positionLanguages` -> Establishes many-to-many relationship between languages and positions.|
| 5. | Professor         | Child class of User, this model represents the website professor type of user. | `id` -> Id associated to the `User` parent class id. <br> `title` <br> `positions` -> Establishes one-to-many relationship between a professor and the positions that are associated to them.|
| 6. | Position          |Represents a research position created by a professor that students can apply for. | `id` <br> `title` <br> `description` <br> `start_date` <br> `end_date` <br> `work_load` <br> `languages` -> Establishes many-to-many relationship between positions and the languages. <br> `research_fields` -> Establishes one-to-many relationship between a position and the research_fields associated to it. <br> `candidates` <br> `applications` -> Establishes one-to-many relationship between a position and the applications associated to it. <br> `professor_id` -> Every position has one professor associated to it.|
| 7. | Application       | Represents the application made by a student for a position posted by a professor. | `id` <br> `date` <br> `status` <br> `position_id` -> Every application has one position associated to it. <br> `professor_id` -> Every application as one professor associated to it. |

#### UML Diagram

![](./images/Model.png)

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

<!-- |    | Methods           | URL Path              | Description        |
|:--:|:-----------------:|:---------------------:|:------------------:|
| 1. | `GET`, `POST`     | `/createapplication `                   | Available only to students, it shows a form to create a application for a position the student navigated to |
| 2. | `GET`           | `/displaypositions`           | Page where students can navigate to view all positions posted |
| 3. | `GET`, `POST`     | `/position`   | Page where students navigate to view the details of a specific position 
| 4. | `GET`     | `/viewallstudents` | For professors when they navigate to see who applied for their positions|
| 5. | `GET`     | `/viewstudent`       | For professors who picks an individual student to view from viewallstudents|
| 6. | `GET`     | `/mypositions`              | For professors to see all the positions they have created | -->

|    | Methods | URL Path | Description |
| -- | ------- | -------- | ----------- |
| 1. | `GET` | `/` | The homepage |
| 2. | `GET` | `/positions` | Displays the positions available to a user; for students, this is all applications (they can apply for), and for professors this is all the applications they've created |
| 3. | `GET`, `POST` | `/positions/new` | Only available to professors, it creates a new position
| 4. | `GET` | `/positions/<position_id>` | Displays the details of a specific position |
| 5. | `GET`, `POST` | `/positions/<position_id>/apply` | Only available to students, it allows a student to apply for the given position |
| 6. | `GET` | `/positions/<position_id>/applicants` | Only available to professors, it allows a professor to view all the applicants to a given position |
| 7. | `GET`, `POST` | `/login` | Allows a user to sign in |
| 8. | `GET` | `/register` | Allows a new user to select whether they want to register as a student or a professor |
| 9. | `GET`, `POST` | `/register/student` | Allows a user to register as a student |
| 10. | `GET`, `POST` | `/register/professor` | Allows a user to register as a professor 

### 2.2.3 View and User Interface Design 

The role of the view is to be the connection with what is displayed for the user and how it gets sent to the forms in Controller. Everything involving the UI of the app including templates, styling, and images can be found here.

<!-- Provide a list of the page templates you plan to create (or you already created). Briefly describe the information that will be displayed on those pages and the forms that will be rendered (i.e., explain the input and output for each page). Make sure to mention which use-cases in your “Requirements Specification” document will utilize these interfaces for user interaction. You can supplement your description with UI sketches or screenshots. -->

#### Iteration 1
| Template | Description |
| -------- | ----------- |
| `navbar.html` | Is the navigation bar on the op of each page and contains most of the links a user might need |
| `_position.html` | Our current display of a positions information obtained straight through the database. Only used on our index page thus far, but will be revamped else where |
| `base.html` | The base for all our templates that includes our imports from boostrap as well as the import for our CSS classes |
| `createPosition.html` | Displays the form for creating positions found in `form.py`. Upon submission goes through forms for validation and then user input is stored in database |
| `index.html` | Displays our homepage including the navigation bar and displays all of the positions posted by professors. Will be revamped to to have columns and not display all position information |
| `login.html` | Displays the page where users will log in or navigate to registration. Use login form found in `auth_forms.py` |
| `register.html` | Displays an option for users to identify if they are either student or professor. User simply clicks professor or student and is redirected to the appropiate registration page |
| `register_professor.html` | Displays the page where professors can input all their information into the Professor Registration form found in `auth_forms.py` |
| `register_student.html` | Displays the page where students can input all their information into the Student Registration form found in `auth_forms.py` |

Below are the pages we currently have done for iteration one with the revamped bootstrap/flask tool. 

![](./images/Project_Create_Position.png)
![](./images/Project_Home.png)
![](./images/Project_Login.png)
![](./images/Project_Register_Index.png)
![](./images/Project_Register_Professor.png)
![](./images/Project_Register_Student.png)

#### Iteration 2
<!-- Looking forward to iteration two, we plan on creating the following templates.

| Template | Description |
| -------- | ----------- |
| `create_application.html` | Will display the create application form found in forms.py. Will have all the input fields for the user and will be validated by the forms and models. |
| `view_position.html` | Will display all information on a specfic positoin. All information will obtained through database. No user input. |
| `display_students.html` | Will display a list of students who are have applied to a position. May be revamped into a pop-up instead of a entire page.|
| `display_student.html` | Will display the information of a student for a professor looking for qualifying students. Information will be obtained through database.  | -->

Iteration 2 will contain the following templates:

| Template | Description |
| -------- | ----------- |
| `errors/403.html` | Error page for when a user attempts to access a page they're not authorized to access |
| `errors/404.html` | Error page for when a user attempts to access something not know by the server |
| `register/index.html` | Page to allow a user to select what user type they want to register as |
| `register/register_student.html` | Form to register a user as a student |
| `register/register_professor.html` | Form to register a user as a professor |
| `_navbar.html` | The navbar shown everywhere |
| `_position.html` | An individual position used by `positions.html` as a sub-template |
| `base.html` | The base of the application; includes the header, HTML template, navbar, etc. |
| `createPosition.html` | Allows a professor to create a position that students can apply for |
| `index.html` | The homepage |
| `login.html` | The login page for users to login to the application |
| `position.html` | Shows the details of a specific position |
| `position_apply.html` | Allows a student to apply for a position |
| `positions.html` | Shows a list of positions; for students, this is all open positions; for professors, this is all positions they've created |

# 3. Progress Report

## October 23, 2023
With iteration 1 completed, in terms of use cases, we have finished with student registration, professor registration, login/logout for both types of users, and our app can create a position through the professor user. With these done we are currently on track. However, we have done much more work in the backend of our app that is not implemented yet including creating the model for application and setting up the neccesary database relationships (i.e. professor to position, languages to student and to position, interests to student and to position, and vice versa). We've also successfully created a polymorphic user that student and professor both inherit from. 

Our UI, previously using various libary tools from the latest bootstrap will now use, will now use a specific flask-bootstrap libary. This will make UI design quicker and better.

Looking forward to iteration two, we plan to shift our focus to positions and the applications created for them. This will include professors being able to view their posted positions, allowing students to view a positions details, allowing students to create an application for a position, allowing professors to view which students applied to each postion, and allowing professors to view each individual student application. 

## November 7, 2023
With iteration 2 completed, we'll have finished professors being able to:
- View the positions they've created
- View the details of a specific position
- View the applicants to a position

For students, they can now:
- View all available positions to apply for
- View the details of a specific position
- Apply to a position

Additionally, there is also:
- User permission checking; i.e., that a student can't create a new position or a professor view a position that isn't theirs (for now)
- 404 handling; i.e., if a user navigates to `/position/<gibberish>`, the application shows a proper error page

# 4. Testing Plan

<!-- (***in iteration 1***)
Don't include this section. -->

<!-- (***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? 
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK) -->

  <!-- For testing, we plan to test differently for each section of work. When changing the database and seeing if we can create certain objects, we will be doing query statements in python and creating the object manually. In the last iteration, most of our testing was done through the app itself where multiple functionality pieces were tested. For example, when seeing if the forms, routes, and UI worked correctly for a use case like student registration, we would merge all the work out team did into our UI branch and through trial and errors we would polish up the code to get a working version on the app.  -->

# 5. References

None