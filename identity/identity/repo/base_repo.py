class DbObj:
    def __init__(self, data_source):
        self.data_source = data_source

    def add_item(self):
        raise NotImplemented

    def get_by_id(self, item_id):
        raise NotImplemented

    def get_all(self):
        raise NotImplemented

    def update_item(self):
        raise NotImplemented
