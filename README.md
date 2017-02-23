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

Xueguang

- Add Drop downs and list display.