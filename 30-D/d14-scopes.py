class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

        # Add your code here

    def computeDifference(self):
        maximum_element = max(self.__elements)
        minimum_element = min(self.__elements)

        self.maximumDifference = maximum_element - minimum_element

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
