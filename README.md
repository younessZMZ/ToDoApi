# ToDoApi
This is a CRUD api with FastApi.

# How to use:

- Clone the project and open it with your python editor.
- Create virtual environment for your project.
```console
foo@bar:~$ python -m venv venv
```
- Activate your environment.
```console
foo@bar:~$ .\venv\Scripts\activate
```
- Install requirements in requirements.txt.
```console
foo@bar:~$ pip install -r requirements.txt
```
- Install MongoDB (if you are new to MongoDB this [Video](https://www.youtube.com/watch?v=EjcAqAJjmEo&t=52s) will help you.)

Once all the above steps are done, launch the main python file.

To access the swagger you can add /docs to your localhost like : http://127.0.0.1:8000/docs.

# CORS error.
If you face this error:

![The CORE error](/images/core_error.png)

You can make sure the origin used by your client is provided to your app as allow_origins argument (line 11 in main.py):

```python
origins = ["http://localhost:3000", "https://localhost:3000"]
```

To understand more this error and why it occurs you can refer to [this web site](https://www.stackhawk.com/blog/react-cors-guide-what-it-is-and-how-to-enable-it/).
