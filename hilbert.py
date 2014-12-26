class Hilbert():
    
    def __init__(self,order=1):
        self.x = 0 
        self.y = 0     
        self._step(0)
        self.iter = self._hil(0, 1, order)
    #delegate iterator
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.iter)
    
    def _hil(self, dirs, rot, order):
            if (order == 0): 
                return
            dirs += rot
            yield from self._hil(dirs, -rot, (order-1))
            yield from self._step(dirs)
            dirs -= rot
            yield from self._hil(dirs, rot, (order-1))
            yield from self._step(dirs)
            yield from self._hil(dirs, rot, (order-1))
            dirs -= rot
            yield from self._step(dirs)
            yield from self._hil(dirs, -rot, (order-1))
    
    def _step(self, dirs):
    
        dirs %= 4
    
        if dirs == 0:
            self.x += 1
        elif dirs == 1:
            self.y += 1
        elif dirs == 2:
            self.x -= 1
        else:
            self.y -= 1 
    
        yield self.x, self.y
