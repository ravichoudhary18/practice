class Flat:
    def __init__(self, list_flat=None, dict_flat=None, list_of_dict=None) -> None:
        self.list_flat = list_flat
        self.dict_flat = dict_flat
        self.list_of_dict = list_of_dict

    def list_of_dict_flat_in(self, data=None):
        if data is None:
            data =  self.list_of_dict
        
        if isinstance(data, list):
            data = data[0]
        
        flat_list = []
        for key, value in data.items():
            if isinstance(value, dict):
                flat_list.extend(self.list_of_dict_flat_in(value))
            else:
                flat_list.append({key: value})

        return flat_list

    def list_flat_in(self, data=None):
        if data is None:
            data = self.list_flat

        flat_list = []
        for item in data:
            if isinstance(item, list):
                flat_list.extend(self.list_flat_in(item))
            else:
                flat_list.append(item)
        return flat_list


flat = Flat(list_flat = [123, [[15, 8, 56, [1, 2, 3, [1, 2, 6]]]]], list_of_dict=[{'user': {'name': 'ravi', 'age': 28, 'info': {'account': 'insta', 'join': 'today'}}}])
print(flat.list_flat_in())
print(flat.list_of_dict_flat_in())
