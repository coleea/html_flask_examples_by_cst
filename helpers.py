import json
import hashlib


def get_contacts():
    with open('contacts.json', 'r') as f:
        contacts = json.loads(f.read())
    
    return contacts


def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        contacts = f.write(json.dumps(contacts))


def get_contact(id):
    contacts = get_contacts()
    
    for contact in contacts:
        if contact['id'] == id:
            return contact
    raise ValueError(f'Contact {id} not found')


def activate_contacts():
    contacts = get_contacts()
    
    for contact in contacts:
        contact["status"] = 'active'

    save_contacts(contacts)


def delete_contact(id):
    contacts = get_contacts()
    
    for contact in contacts:
        if contact["id"] == id:
            contact["status"] == 'inactive'
            break

    save_contacts(contacts)


def get_active_contacts():
    contacts = get_contacts()

    return [contact 
    for contact in contacts 
    if contact['status']=='active']


def get_hash(text):
    return hashlib.sha224(text.encode()).hexdigest().upper()[0:15]


def get_agent(id):
    return {
        'name':'Agent Smith', 
        'email': f'void{id}@null.org', 
        'id': get_hash(str(id))
        }


def get_page_of_agents(pages_number):
    return [
        get_agent(id+1) for id in range((pages_number-1)*10,pages_number*10)
    ]
