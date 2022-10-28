from io import StringIO


class StringBuilder:
    _txt_str = None

    def __init__(self, value=""):
        self._txt_str = StringIO()
        if value != "":
            self._txt_str.write(value)

    def append(self, value):
        self._txt_str.write(value)

    def append_line(self, value=''):
        self._txt_str.write(value + '\r\n')

    def replace(self, item, new_value):
        temp = self._txt_str.getvalue()
        temp = temp.replace(item, new_value)
        self._txt_str = StringIO(temp)

    def to_string(self):
        self._txt_str.seek(0)
        self._txt_str.read()
        return self._txt_str.getvalue()


def __str__(self):
    return self._txt_str.getvalue()
