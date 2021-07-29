class ExceptionNone(Exception):
    def __init__(self, *args):
        super(ExceptionNone, self).__init__('Variable don\'t have any data')


class ExceptionNotNumber(Exception):
    def __init__(self, *args):
        super(ExceptionNotNumber, self).__init__('Variable is not number')
