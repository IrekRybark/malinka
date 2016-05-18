
class Observable:
    """
    Class based on example from http://wiki.wxpython.org/ModelViewController
    An observable calls callback functions when the data has changed
    o = Observable()
    def func(data):
    print "hello", data
    o.addCallback(func)
    o.set(1)
    --| "hello", 1
    """
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def add_callback(self, func):
        self.callbacks[func] = 1

    def del_callback(self, func):
        del self.callbacks[func]

    def _do_callbacks(self):
        for func in self.callbacks:
            func(self.data)

    def set(self, data):
        self.data = data
        self._do_callbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None


