#Tea settings model, independent of the GUI

class TeaSettings:
    LIMITS = {
        "steepTime": (1, 10),
        "numSugars": (0, 10),
        "numCreams": (0, 10),
    }

    def __init__(self, steepTime=3, numSugars=0, numCreams=0):
        self.steepTime = steepTime
        self.numSugars = numSugars
        self.numCreams = numCreams
        self._listeners = {attr: [] for attr in self.LIMITS}

    def subscribe(self, attr, callback):
        """Call callback(newValue) whenever attr changes."""
        self._listeners[attr].append(callback)

    def adjust(self, attr, delta):
        """Change attr by delta if within limits. Returns True if it changed."""
        lo, hi = self.LIMITS[attr]
        value = getattr(self, attr) + delta
        if not lo <= value <= hi:
            return False
        setattr(self, attr, value)
        for callback in self._listeners[attr]:
            callback(value)
        return True
