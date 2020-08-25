from testrail import *
import json

def get_client():
    client = APIClient('https://testrail.internetbrands.com//testrail/')
    client.user = 'may.li@internetbrands.com'
    client.password = 'Liapaopao2'
    return client

def get_case_info(client, case_id):
    case = client.send_get('get_case/{case_id}'.format(case_id=case_id))
    print(case)

    data = case['custom_data']
    precondition = case['custom_preconds']
    steps = case['custom_steps']

    return {"custom_data": data,
            "custom_preconds": precondition,
            "custom_steps": steps}
    # return {"custom_preconds": precondition}

def set_case_info(client, case_id, content):
    client.send_post('update_case/{case_id}'.format(case_id=case_id), content)


def set_case_filed(client, case_id, filed_name, filed_value):
    data = {filed_name: filed_value}
    client.send_post('update_case/'+case_id, json.dumps(data))

def copy_case_from_to(client):
    from_to_list = [[19935556,34166037]]


    for from_to in from_to_list:
        content = get_case_info(client, from_to[0])
        set_case_info(client, from_to[1], content)

def update_case_filed(client, case_list, content):
    for case_id in case_list:
        set_case_info(client, case_id, content)

def update_case_title(client):
    case_list = [
26620671,
26620672,
26620673,
26620674,
26620675,
26620676,
26620677,
26620678,
26620679,
26620680,
26620681,
26620682,
26620683,
26620684,
26620685,
26620686,
26620687,
28801005,
32823399,
32823400,
32823401,
32823402]
    for case_id in case_list:
        case = client.send_get('get_case/{case_id}'.format(case_id=case_id))

        title = case['title']
        print(title)
        title = title.replace(' - Remove Versioning', '')
        print(title)
        content = {"title": title}
        client.send_post('update_case/{case_id}'.format(case_id=case_id), content)


if __name__ == '__main__':
    client = get_client()
    copy_case_from_to(client)
    # update_case_title(client)





