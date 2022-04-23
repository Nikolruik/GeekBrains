from pprint import pprint

class Road:
    __massa = 1.5

    def __init__(self, lenght=0, width=0, tickness=0.05):
        self._len = lenght
        self._wid = width
        self._tick = tickness

    def get_volume(self):
        return self._len*self._wid*self._tick*self.__massa

    def get_param(self):
        k = [('lenght', 'm'), ('width', 'm'), ('tickness', 'm'), ('massa', 't'), ('volume', 'm3')]
        v = [self._len, self._wid, self._tick, self.__massa, self.get_volume()]
        return {k[0]: (v, k[1]) for k, v in zip(k, v)}

    if __name__ == '__main__':
        a = Road()
        pprint(a.get_param(), indent=2)
        b = Road(100, width=6)
        pprint(Road.get_param(b), indent=2)
