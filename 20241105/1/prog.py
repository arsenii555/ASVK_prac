class Omnibus:
    attributes = dict()
    attrs = set()

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            if name not in Omnibus.attributes:
                Omnibus.attributes[name] = 0
            Omnibus.attributes[name] += 1
        self.attrs.add(name)

    def __getattr__(self, name):
        if not name.startswith('_'):
            return Omnibus.attributes.get(name, 0)

    def __delattr__(self, name):
        if not name.startswith('_'):
            if name in self.attrs:
                self.attrs.discard(name)
                if name in Omnibus.attributes:
                    Omnibus.attributes[name] -= 1
                if Omnibus.attributes[name] == 0:
                    del Omnibus.attributes[name]


import sys

exec(sys.stdin.read())
