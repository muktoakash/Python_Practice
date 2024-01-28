"""
Awesome Range!

Accepts:
- start value
- end value
- step value (optional)
"""

class AwesomeRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

        self.current_value = start

    def __iter__(self):
        return self

    def __next__(self):
        current_value = self.current_value
        self.current_value += self.step

        if current_value >= self.end:
            raise StopIteration

        return current_value
