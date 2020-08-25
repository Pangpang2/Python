from mako.template import Template


template = Template(filename='tpl.txt', module_directory=None)

office_list=[{'name':'KFC Dental 57', 'id': '58', 'street': '123 Nye Street', 'city':'Los', 'state':'ss', 'zipcode':'test'},
             {'name': 'KFC Dental 56', 'id': '56', 'street': '124 Nye Street', 'city':'Los', 'state':'ss', 'zipcode':'test'}]

block_uploads =[{'id': 5, 'office_list':office_list,'approved_by':'test'},
                {'id':6, 'office_list':office_list, 'approved_by':'null'}]
custom_data = {'block_uploads': block_uploads}
print template.render(**custom_data)



