
Sample project used as an introduction to the GraphQL.


*PROJECT SETUP*

1. Using Python 3.8 create a new virtualenv (3.7-3.9 might work, haven't tested)
2. Install all dependencies
`pip install -r requirements.txt`
3. Run migrations
`python mange.py makemigrations`
4. Migrate `python mange.py migrate`
5. Load fixtures `python manage.py loaddata ingredients`
6. Run collectstatic `python mange.py collectstatic`
7. Run server `python manage.py runserver`
8. Open `localhost:8000/graphql`
9. Run the following query:

```
query {
  allIngredients {
    id
    name
  }
}
```

And you're all good to go :)
