# ISOM350 Practical Midterm Fall 2023

Please read instructions carefully. Depending on the question, you might have to edit Readme.md to respond to questions or modify the project files.

This directory contains the following files:
- **.gitigniore**: just ignore this file
- **README.md**: this file, which contains the questions and will require for some questions that you edit the file to answer them
- **q1.py**: This is a python file that contains the code for question 1. To run this file, you can use the following command: `python q1.py` in terminal.
- **q2_project**: This is a directory that contains a django project. You will need to modify/examine this project to answer the remaining questions. To run this project, you run the following command: `python manage.py runserver` in terminal from within the `q2_project` directory.

## Questions (Total 100 pts)

### Question 1 (40 pts)
Perform the following tasks:
1. **15 pts:** Create a django project directory named `q1_project`.
2. **25 pts:** Create a view that displays the following message: ```Question1 Done!```. The view should be linked to the path `q1/`.

### Question 2 (60 pts)
The directory `q2_project` contains a django project. Please answer/complete the following questions/tasks:
1. **5 pts:** What are the available paths in this project? (list them all here)
2. **5 pts:** What are the available view functions? (List them all here)
3. **5 pts:** Is there a view function that is not linked to a path? If so, what is it? (Answer here)
4. **20 pts:** The view `greeting_view` should display the following message if you open it for the first time:
```Welcome! please tell us your name```
If you submit your name it should display a greeting with your name. For example, if you submit the name "Khaled", it should display:
```Hello Khaled!``` 
The view has a number of errors. Please fix them so that the view operates as described.
5. **25 pts:** The view `list_view` should display a list of all the products in the products variable. However, it is incomplete. Please complete it as described using django templates to display the list of products and using the appropriate html tags for this task.
6. **Bonus 10 pts:** Reorder the url paths such that you use urls.py in the app directory instead of the project directory. 

### Important notes
- You must commit your work and submit it to github. Successfully submitting your work to github guarantees you get a minimum of 10 pts in the quiz.
- If your submitted code does not run, you will get 0 for the question.
