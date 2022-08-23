# Python: Multiset Implementation

class Multiset:
    def __init__(self):
        self.nums = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.nums.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.nums:
            self.nums.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.nums:
            return True
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.nums)
