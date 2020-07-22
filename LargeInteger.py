class LargeInteger:

    def __init__(self, integer_str):
        self.integer_str = integer_str
        if integer_str[0] == '-':
            self.sign = -1
            array = [int(c) for c in integer_str[1:]]
        elif integer_str[0] == '+':
            self.sign = 1
            array = [int(c) for c in integer_str[1:]]
        else:
            self.sign = 1
            array = [int(c) for c in integer_str]
        self.array = [self.sign * i for i in reversed(array)]

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return self.integer_str

    @staticmethod
    def _adjust_array(array):
        while len(array) > 0 and array[-1] == 0:
            array.pop(-1)

        if len(array) == 0:
            return [0], 1

        array_new = []
        if array[-1] > 0:
            sign = 1
            for i in range(len(array) - 1):
                item = array[i]
                if 10 > item >= 0:
                    array_new.append(item)
                elif item >= 10:
                    array_new.append(item - 10)
                    array[i+1] += 1
                else:
                    array_new.append(item + 10)
                    array[i+1] -= 1
        else:
            sign = -1
            for i in range(len(array) - 1):
                item = array[i]
                if -10 < item <= 0:
                    array_new.append(item)
                elif item <= -10:
                    array_new.append(item + 10)
                    array[i+1] -= 1
                else:
                    array_new.append(item - 10)
                    array[i+1] += 1
        if array[-1] != 0:
            array_new.append(array[-1])
        while len(array_new) > 0 and array_new[-1] == 0:
            array_new.pop(-1)
        array_new = [i*sign for i in array_new]
        return array_new, sign

    def __add__(self, other):
        array = []
        for a, b in zip(self.array, other.array):
            array.append(a+b)
        if len(self) > len(other):
            array.extend(self.array[len(other):])
        else:
            array.extend(other.array[len(self):])
        array, sign = self._adjust_array(array)
        array = [str(i) for i in reversed(array)]
        if sign == -1:
            array.insert(0, '-')
        return LargeInteger("".join(array))

    def __sub__(self, other):
        other = -other
        return self + other

    def __neg__(self):
        integer_str = self.integer_str
        if integer_str[0] == '-':
            integer_str[0] = '+'
        elif integer_str[0] == '+':
            integer_str[0] = '-'
        else:
            integer_str = '-' + integer_str
        return LargeInteger(integer_str)
