# Future Proof Technology Test Task 

Test task require to develop solution that can authorize without using email and password. First of all, we need to generate secure token. Token must contain information about user. This data must be encrypted, otherwise malicious people can access sensitive information. I am not cryptographer, that means l can't make secure solution, but there are many extension that can help me. In this task i use `itsdangerous` for generating token. It is both secure and well testing lib.


# HOW TO USE?

1. Go https://magic-link2234.herokuapp.com/create_delete

2. Add Email to the form 
3. Check your email and follow the link

If you want to remove "access" just add your email again


# HOW TO TEST?

1. Clone git repo 

2. ```python manage.py db init```
3. ```python manage.py db migrate```
4. ```python manage.py db upgrade```
5. ```python manage.py test --coverage```






