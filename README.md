# example of htmx + python flask 

## This repo is forked from `https://tildegit.org/cst/htmx_examples`

---

# Enjoy the [HTMX examples](https://htmx.org/examples/) rendered with [Flask](https://flask.palletsprojects.com/en/2.1.x/)!


## Run on linux/mac

you must install python 3.8

```bash
pip install pipenv
pipenv install
pip env shell
pip install colorama
./run
```
Open http://localhost:5000/

---

## Run on windows

you must install python 3.8

```powershell
pip install pipenv
pipenv install
pip env shell
pip install colorama
.\run_windows.ps1
```
Open http://localhost:5000/

---

## 이 프로젝트에 사용된 라이브러리

- frontend
  - htmx
    - high power tools for HTML
    - https://htmx.org/
  - hyperscript
    - An easy & approachable language for modern web front-ends
    - https://hyperscript.org/
  - Sortable.js
    - JavaScript library for reorderable drag-and-drop lists
    - https://sortablejs.github.io/Sortable/
- server
  - flask
    - a lightweight WSGI web application framework
    - https://github.com/pallets/flask
  - jinja_partials
    - Simple reuse of partial HTML page templates in the Jinja template language for Python web frameworks
    - https://github.com/mikeckennedy/jinja_partials

---

## htmx 기본문법

- hx-post="/click"
  - POST로 "/click" 에 요청을 보낸다. 이 요청은 fetch가 아닌 XMLHttpRequest로 수행된다
- hx-trigger="click" 
  - onclick에 해당한다. hx-post가 어떤 이벤트로 트리거 되는지를 나타낸다
- hx-target="#parent-div"
  - querySelector로 #parent-div 엘리먼트를 찾고 그 엘리먼트를 리스폰스 받은 엘리먼트로 교체한다

- hx-swap="outerHTML"
  - 엘리먼트를 교체할 때 outerHTML의 값을 교체한다
  - innerHTML의 값을 교체할 수도 있다

---

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
