## Requirements:
If you don't have Django>=1.10.5 and markdown>=2.6.8, then

```python
pip install Django==1.10.5
pip install markdown
pip install pypandoc
pip install djangorestframework
```
We also need Pandoc to be installed on your server.

[How to install Pandoc](http://pandoc.org/installing.html)


## How to use:

Step into the "mysite" directory and type

```python
python3 manage.py runserver
```

Open http://127.0.0.1:8000/wowCS/ in your browser.







## Update Log:

#### 2.22 Version 0.3

Diyi

- Add user login/logout/register/profile
- Add user_auth for each function.
- Optimize the url routing rules
- Create Restful API

Xueguang

- Add Drop downs and list display.
- Add edit button and delete button for notes.

#### 2.23 Version 0.4

Diyi

- Add create notebook and note 

- Insert the Django pagedown widget in create/edit note.

- Solve the illegal notebook_title problem

- Filter the  user available notebooks seen in the drop down list in creating a new note.

- Solve the duplicate notebook name problem.

- add empty default notebook for new user.

Xueguang 

- Add favorite button
- Handling note edit/view/delete redirection problem in jquery. (main.js)

  ​

  ​
