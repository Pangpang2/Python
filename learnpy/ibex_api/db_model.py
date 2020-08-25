import string

def get_model_string(model, columns):
    columns = columns.split(',')
    for col in columns:
        print "     self." + col + " = ''"

    print '---------------------------------------------------'
    for col in columns:
        letter_list = col.split('_')
        letter_list = [l.capitalize() for l in letter_list]
        letter = ''.join(letter_list)
        print '     {0}_model.{1} = {2}_dictionary["{3}"]'.format(model, col, model, col)

    print '---------------------------------------------------'
    for col in columns:
        letter_list = col.split('_')
        letter_list = [l.capitalize() for l in letter_list]
        letter = ''.join(letter_list)
        print '     {0}_dictionary["{1}"] = Tools.check_null_and_single_quotify({2}_model.{3})'.format(model, col, model, col)

    print '-----------------------------------------------'
    for col in columns:
        print "                        {"+col+"},"
if __name__ == '__main__':


    print 'helloIam'.capitalize()
    #print dict(dict_1, **dict_2)
    get_model_string('visitor_versioned',
                     'id,client_id,address_id,type,first_name,last_name,birthday,active_in_pms,pms_id,'
                     'first_visit,staff_id,office_id,extensible_notes,gender,last_visit,last_maintenance,'
                     'dataset_version_id,dataset_version_deletess')

    get_model_string('email_versioned',
                     'id,visitor_id,email,relative_name, client_id, pms_id,link_id,dataset_version_id,dataset_version_deletes,is_valid')

