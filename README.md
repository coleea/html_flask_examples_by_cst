# example of htmx + python flask 

## This repo is forked from `https://tildegit.org/cst/htmx_examples`

---

# Enjoy the [HTMX examples](https://htmx.org/examples/) rendered with [Flask](https://flask.palletsprojects.com/en/2.1.x/)!


## Install (ubuntu)

never use python 3.10 version is incompetible

```
sudo apt install pipenv
pipenv install
```

## Run
```
./run
```

## Use
  - Open http://127.0.0.1:5000/
  - Enjoy!

## What is where

  
 - [html_examples.html](./templates/htmx_examples.html) links to all individual examples
  - Each example has its own template in /templates, e.g. [click_to_edit.html](./templates/click_to_edit.html)
  - Each example has its own jinja partial(s) in /templates/partials. e.g. [click_to_edit_contact_get.py](./templates/partials/click_to_edit_contact_get.html)
  - All routes are in [routes.py](./routes.py)
  - There's one main route by example, e.g. 
  ``` 
  @app.route("/examples/click-to-edit/")
def get_click_to_edit():
  ```
  - It is followed by additional routes, as the example requires, e.g.
  ```
@app.route(
    "/contact/<int:id>",
    methods=['GET'])
def get_contact(id):

@app.route(
    "/contact/<int:id>",
    methods=['PUT'])
def put_contact(id):
  ```

 ## Other notes

 Sample data is in [contacts.json](./contacts.json). There are simple routines to read and write to it. Not safe, not production ready, etc. 
 If you think that using something production-like, e.g. a DB would make more sense for the examples please let me know. My thinking so far is that it will only clutter the examples codebase. 

 ## Not super-easy?

 If the examples' implementation is not super-easy to install and figure out, please write me to tell me what makes it difficult.

 Thanks! 
