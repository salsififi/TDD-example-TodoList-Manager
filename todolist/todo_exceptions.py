class TodoNotFoundError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__("Todo not found")


class TodoNotDoneError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__("Todo not done")
