import json
from random import randrange

from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
)

import jinja_partials

from helpers import (
    get_contacts,
    get_contact,
    save_contacts,
    get_page_of_agents,
    activate_contacts,
    get_active_contacts,
    delete_contact,
)

app = Flask(__name__)

jinja_partials.register_extensions(app)


@app.route("/")
@app.route("/examples/")
def get_htmx_examples():
    contacts = get_contacts()

    return render_template('htmx_examples.html')


@app.route("/examples/click-to-edit/")
def get_click_to_edit():
    contacts = get_contacts()
    
    return render_template(
        'click_to_edit.html',
        id=1, 
        contact=contacts[1],
        contacts=contacts)


@app.route(
    "/contact/<int:id>",
    methods=['GET'])
def get_single_contact(id):
    contacts = get_contacts()
    
    return jinja_partials.render_partial(
        'partials/click_to_edit_contact_get.html',
        id=id, 
        contact=contacts[id])


@app.route(
    "/contact/<int:id>",
    methods=['PUT'])
def put_contact(id):
    contacts = get_contacts()
    contacts[id]['name'] = request.form['firstName']
    contacts[id]['surname'] = request.form['lastName']
    contacts[id]['email'] = request.form['email']
    
    save_contacts(contacts)

    return jinja_partials.render_partial(
        'partials/click_to_edit_contact_get.html',
        id=id, 
        contact=contacts[id])


@app.route("/contact/<int:id>/edit")
def get_contact_edit_form(id):
    contacts = get_contacts()
    
    return jinja_partials.render_partial(
        'partials/click_to_edit_contact_put.html',
        id=id,
        contact=contacts[id])


@app.route("/examples/bulk-update/")
def get_bulk_update():
    contacts = get_contacts()
    
    return render_template(
        'bulk_update.html',
        contacts=contacts)


@app.route("/activate", methods=['PUT'])
def activate():
    contacts = get_contacts()
    
    for id in request.form.getlist('ids'):
        contacts[int(id)-1]['status']='active'
    
    save_contacts(contacts)

    return jinja_partials.render_partial(
        'partials/bulk_update_get.html',
        contacts=contacts)


@app.route("/deactivate", methods=['PUT'])
def deactivate():
    contacts = get_contacts()
    
    for id in request.form.getlist('ids'):
        contacts[int(id)-1]['status']='inactive'
    
    save_contacts(contacts)

    return jinja_partials.render_partial(
        'partials/bulk_update_get.html',
        contacts=contacts)


@app.route("/examples/click-to-load/")
def get_click_to_load():
    page_number = request.args.get('page', default=1, type=int)

    agents = get_page_of_agents(page_number)
    
    return render_template(
        'click_to_load.html',
        next_page=page_number+1,
        agents=agents)


@app.route("/contacts/")
def get_contacts_for_load():
    page_number = request.args.get('page', default=1, type=int)

    agents = get_page_of_agents(page_number)
    
    return render_template(
        'partials/click_to_load_get.html',
        next_page=page_number+1,
        agents=agents)


@app.route("/examples/delete-row/")
def get_delete_row():
    activate_contacts()
    contacts = get_active_contacts()
   
    return render_template(
        'delete_row.html',
         contacts=contacts)


@app.route(
    "/contact/<int:id>/",
    methods=['DELETE'])
def delete_row(id):
    delete_contact(id)

    return ""


@app.route("/examples/edit-row/")
def get_edit_row():
    contacts = get_contacts()
   
    return render_template(
        'edit_row.html',
         contacts=contacts)


@app.route("/contacts/<int:id>/edit")
def get_contact_for_edit(id):
    contact = get_contact(id)

    return render_template(
        'partials/edit_row_get_single_row.html', 
        contact=contact)

@app.route(
    "/contacts/<int:id>/",
    methods=["GET"])
def get_contact_for_row(id):
    contact = get_contact(id)

    return render_template(
        'partials/edit_row_show_single_row.html', 
        contact=contact)


@app.route(
    "/contacts/<int:id>/",
    methods=["PUT"])
def put_contact_for_row(id):
    contacts = get_contacts()

    contacts[id-1]['name'] = request.form['name']
    contacts[id-1]['email'] = request.form['email']

    save_contacts(contacts)

    return render_template(
        'partials/edit_row_show_single_row.html', 
        contact=contacts[id-1])


@app.route("/examples/confirm/")
def get_confirm():
       
    return render_template(
        'confirm.html')


@app.route("/confirmed/")
def get_confirmed():
       
    return "Confirmed"


@app.route("/examples/lazy-load/")
def get_lazy_load():
       
    return render_template(
        'lazy_load.html')


@app.route("/graph")
def get_graph():
       
    return "<img alt='Tokyo Climate' src='/static/tokyo.png'>"


@app.route("/examples/inline-validation/")
def get_inline_validation():
       
    return render_template(
        'inline_validation.html')

@app.route(
    "/contact/email",
    methods=["POST"])
def post_contact_email():
    email = request.form['email']
    
    if email == 'test@test.com':
        return render_template(
            'partials/inline_validation_email.html',
            email=email
        )
    elif '.com' in email:
        error_message = 'That email is already taken.  Please enter another email.'
    else:
        error_message = 'Please enter a valid email address'
    
    return render_template(
        'partials/inline_validation_error.html',
        email=email,
        error_message = error_message 
    )


@app.route("/examples/infinite-scroll/")
def get_infinite_scroll():
    page_number = request.args.get('page', default=1, type=int)

    agents = get_page_of_agents(page_number)

    last_agent = agents.pop()
    
    return render_template(
        'infinite_scroll.html',
        next_page=page_number+1,
        agents=agents,
        last_agent=last_agent)


@app.route("/infinite-scroll-contacts")
def get_contacts_for_scroll():
    page_number = request.args.get('page', default=1, type=int)

    agents = get_page_of_agents(page_number)

    last_agent = agents.pop()

    return render_template(
        'partials/infinite_scroll_get.html',
        next_page=page_number+1,
        agents=agents,
        last_agent=last_agent)


@app.route("/examples/active-search/")
def get_active_search():

    return render_template(
        'active_search.html')


@app.route(
    "/search",
    methods=['POST'])
def get_search():
    search_string = request.form['search']

    results = []

    if not search_string=="":
        results = [
            {'name': f'{search_string}{i}',
            'surname': 'Hivemind',
            'email': f'{search_string}{i}@hivemind.org'} for i in range(1,4)
        ]

    return render_template(
        'partials/active_search_get.html',
        results=results)


@app.route("/examples/progress-bar/")
def get_progress_bar():

    return render_template(
        'progress_bar.html')


@app.route(
    "/start",
    methods=['POST'])
def get_start():

    return render_template(
        'partials/progress_bar_job.html',
        percentage=0)


@app.route(
    "/job",
    methods=['GET'])
def get_job():
    # In production percentage must come
    # from a background job runner.
    # Here it is simulated.
    percentage = randrange(1,3)*50

    if percentage==50:
        return render_template(
            'partials/progress_bar_job.html', 
            percentage=percentage)
    else:
        return render_template(
            'partials/progress_bar_restart.html')


all_models = {
        'audi': ["A1", "A4", "A6"],
        'toyota': ["Landcruiser", "Tacoma", "Yaris"],
        'bmw': ["325i", "325ix", "X5"],
        }


@app.route("/examples/value-select/")
def get_value_select():
    make_models = all_models['toyota']

    return render_template(
        'value_select.html',
        models=make_models)


@app.route(
    "/models",
    methods=['GET'])
def get_models():
    make = request.args.get('make')
    make_models = all_models[make]

    return render_template(
        'partials/value_select_models.html',
        models=make_models)


@app.route("/examples/dialogs/")
def get_dialogs():

    return render_template(
        'dialogs.html')

@app.route(
    "/submit",
    methods=['POST'])
def submit():

    return request.headers.get('HX-Prompt')


@app.route("/examples/modal-custom/")
def get_custom_modal_dialogs():

    return render_template(
        'modal_custom.html')


@app.route(
    "/modal",
    methods=['GET'])
def get_modal():

    return render_template(
        'modal_custom_modal.html'
    )


@app.route("/examples/tabs-hateoas/")
def get_tabs_hateoas():

    return render_template(
        'tabs_hateoas.html')


@app.route("/tab1")
def get_tabs_hateoas_tab1():

    return render_template(
        'partials/tabs_hateoas_tab1.html')


@app.route("/tab2")
def get_tabs_hateoas_tab2():

    return render_template(
        'partials/tabs_hateoas_tab2.html')


@app.route("/tab3")
def get_tabs_hateoas_tab3():

    return render_template(
        'partials/tabs_hateoas_tab3.html')


@app.route("/examples/tabs-hyperscript/")
def get_tabs_hyperscript():

    return render_template(
        'tabs_hyperscript.html')



@app.route("/tab1-hyperscript")
def get_tabs_hyperscript_tab1():

    return render_template(
        'partials/tabs_hyperscript_tab1.html')


@app.route("/tab2-hyperscript")
def get_tabs_hyperscript_tab2():

    return render_template(
        'partials/tabs_hyperscript_tab2.html')


@app.route("/tab3-hyperscript")
def get_tabs_hyperscript_tab3():

    return render_template(
        'partials/tabs_hyperscript_tab3.html')


def create_items(ids):
    return [
        {'id':id,
        'value': f'Item {id}'}
        for id in ids
    ]


@app.route("/examples/sortable/")
def get_sortable():
    
    return render_template(
        'sortable.html',
        items=create_items([1,2,3,4,5]))


@app.route(
    "/items",
    methods=['POST'])
def get_items():

    return render_template(
        'partials/sortable_items.html',
        items=create_items(
            request.form.getlist('item')))


@app.route("/examples/update-other-content/")
def get_update_other_content():
    
    return render_template(
        'update_other_content.html',
        contacts = get_contacts())


@app.route(
    "/update-other-contents-expand-target-contacts",
    methods=['POST'])
def post_update_other_contents_expand_target_contact():
    contacts = get_contacts()
    contacts[id]['name'] = request.form['firstName']
    contacts[id]['surname'] = request.form['lastName']
    contacts[id]['email'] = request.form['email']
    
    save_contacts(contacts)

    return jinja_partials.render_partial(
        'partials/click_to_edit_contact_get.html',
        id=id, 
        contact=contacts[id])