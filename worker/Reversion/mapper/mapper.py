

class Mapper(object):

    def __init__(self):
        pass

    def execute_map(self, entity_model):
        entity_dict = entity_model.to_dictionary()

        return self.entity_str.format(**entity_dict)


    def get_item(self, entity_dict, key):
        if entity_dict.has_key(key):
            return entity_dict[key]
        return ''
