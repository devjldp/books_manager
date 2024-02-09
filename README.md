# Bookish Blaze
![alt text](/documentation/bookishBlaze.png)
### by Jose Luis Diaz Pulgar

## Introduction
*Bookish Blaze* is a virtual book club that enables users worldwide to connect and share their opinions on books. The mechanics are based on the administrator uploading a book every week, which becomes the selected book for the weekly reading. Once read, users can leave their opinions on it. Additionally, users will have a list of books read in previous weeks and can read others' opinions as well as write their own.

* The link to the live website is here: [Bookish Blaze](https://milestone-3-books-app-94b1da5eec2e.herokuapp.com/)

## User Experience:

### Admin goals:

As the visionary behind Bookish Blaze, our primary business goals are:

Content Management:

- Implement basic CRUD operations to efficiently manage the dynamic content of our virtual book club, ensuring a seamless experience for administrators.

- Enable administrators to insert captivating books into our database weekly, fostering a diverse and engaging reading experience for our global community.


- Facilitate administrators in editing and updating book details, providing enhanced user engagement and ensuring our book collection stays current and intriguing.
Database Visibility:

- Provide administrators with a clear view of all books inserted in the database, enhancing the overall management and organization of our virtual library.

-Empower administrators to efficiently delete books from the database, ensuring a curated and relevant selection for our community.

### User Goals:

Discovering Books:

- Easily navigate the website to discover a comprehensive list of books, including details on different genres, authors, and captivating synopses.

- Expressing Opinions: L leave your opinions on the selected book of the week, fostering a community-driven discourse and sharing diverse perspectives.

- Access a list of books read in previous weeks, allowing you to revisit others' opinions and contribute your insights for an enriched reading experience.

## User Stories:

  - ### As the Administrator, I want to:
      -  have a user-friendly interface that allows me to efficiently add new books to the virtual book club every week. 
      -  the capability to edit and update book details easily. 
      -  the functionality to remove books from the database. This ensures that we maintain a curated and relevant selection, aligning with the preferences and interests of our community.
      -  a clear and comprehensive view of all the books currently present in the database.

  - ### As a new User, I want to:
      - easily create a user account on Bookish Blaze. This includes providing basic information such as username, email, and password.
      - easily navigate the website to discover a comprehensive list of books.
      - access detailed synopses of books to get a sense of their content and decide which ones interest me. 
      - be able to express my opinions on the selected book of the week. 
      - the option to explore a list of books that have been read in previous weeks.

  - ### As a general user of the website, I want to:
  - easily log in to my account.
  - explore book recommendations or reviews from other users. 


## Design of the website.

The bookish app ha sido dividida en dos principales categorias. una seccion para los administradores y otra para los usuarios, con una landing page en comun para ambos.

### Landing page: 
The homepage features an elegant and minimalistic design, with a hero image and two call-to-action buttons that direct the user to the registration or login form. The navigation menu is placed on top of the page and is fixed to improve the user experience.
### User area:
#### Resgiter:
A form for the registration of a new user. Users will fill out the form with their name, email, username, and password.
#### Log-in:
A form where the user enters their username and password. If any data is incorrect, a message is displayed warning of the issue.

#### Profile area:
A page displaying the user's data and showing the book currently being read by the community.

#### List of books: 
A list of books read in previous weeks. A link is provided to select a book and display more information about it.

#### Book info /review
This page shows information about the selected book, as well as reviews from other users. Additionally, there is a form for the user to input their own opinion.

### Admin area:
#### Management area:
With two buttons to add a new book and go to the list of books stored in the database.

#### Add a book:
A form that connects to the database and stores a new book entered by the administrator. This introduced book will be the chosen one to be read during the week.

#### List of books:
Displays the list of books stored in the database. Each book has the option to access the editing page or simply delete the book from the database.

#### Edit a book:
A basic form that connects to the database and allows the updating of the selected book's data.

## Fonts:
The fonts used were imported from Google Fonts. The two families used are **Montserrat** and **Protest Rio**

## Colors:
* Footer: #856a50;
* Header: #856a50;
* Link colors: #fafafa
* hover effect in links: #a5d6a4
* buttons admin: #422e49;

## Tools:
- HTML
- CSS
- JavaScript.
- [Heroku](https://heroku.com): Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- Python: Language used for the backend and main CRUD actions.
- [MongoDB](https://www.mongodb.com/atlas/database): NoSQL database where books, users, and reviews will be stored.
- [flask](https://flask.palletsprojects.com/en/3.0.x/): Flask is a micro web framework written in Python.
- [flask-paginate](https://pythonhosted.org/Flask-paginate/): flask-paginate is a simple paginate extension for flask which is a reference to will_paginate, and uses Bootstrap as a CSS framework.
- [Git](https://git-scm.com/): was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/): is used as the repository for the project's code after being pushed from Git.
- [Figma](): is used to create wireframes.

## Wirframes:

## Testing

### Code Validation

### User Stories Testing

#### Admin stories
- **Add a new book:** Form to add a new book, book successfully inserted into the database, and displayed in the list of books.  
![alt text](/documentation/user_admin_stories/addBook.png)
![alt text](/documentation/user_admin_stories/addBook2.png)
![alt text](/documentation/user_admin_stories/addBook3.png)
  
- **Edit a book:** Form to update a selected book, book successfully updated into the database.  
![alt text](/documentation/user_admin_stories/editBook.png)
![alt text](/documentation/user_admin_stories/editBook2.png)
![alt text](/documentation/user_admin_stories/message.png)

- **Delete a book:** Book successfully deleted.  
![alt text](/documentation/user_admin_stories/delete1.png)

#### User Stories

- **Sign in:** Sign In and redirect to the profile view  
![alt text](/documentation/user_admin_stories/userLogin.png)

- **book list:** Booklist for users with a link to add reviews and check information  
![alt text](/documentation/user_admin_stories/user_book_list.PNG)

- **Add a new review:** add a review in the selected book.  
![alt text](/documentation/user_admin_stories/addReview.png)
![alt text](/documentation/user_admin_stories/displayReview.png)


### Manual Testing:
* Manual tests with different cases can be found in the next Excel file. [Manual test](/documentation/manual%20test%20-%20milestone3.xlsx) 

### Lighthouse:

![alt text](/documentation/lighthouse/landingPage.png)
![alt text](/documentation/lighthouse/register.png)
![alt text](/documentation/lighthouse/signIn.png)
![alt text](/documentation/lighthouse/adminManager.png)
![alt text](/documentation/lighthouse/addBook.png)
![alt text](/documentation/lighthouse/editBook.png)
![alt text](/documentation/lighthouse/bookList.png)
![alt text](/documentation/lighthouse/userBookList.png)


### Bugs:
As of the project delivery, no bugs have been observed.

## Deployment
* The site was deployed to Heroku.  
* The link to the live website is here: [Bookish Blaze](https://milestone-3-books-app-94b1da5eec2e.herokuapp.com/)

* The code can be found in GitHub: [Bookis Blaze](https://github.com/devjldp/books_manager)


## Credits

### Pictures
main image: it was downloaded from [here](https://www.vecteezy.com/photo/28112855-a-cup-of-coffee-with-book-and-pen-on-the-wooden-table-ai-generated)

### code
Code to validate a password using javascript: Follow this article [here](https://www.w3resource.com/javascript/form/password-validation.php)



