class LargeInteger:

    def __init__(self, integer_str):
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

    @property
    def integer_str(self):
        array = [str(abs(i)) for i in reversed(self.array)]
        string = "".join(array)
        if self.sign == -1:
            string = '-' + string
        return string

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return self.integer_str

    def __mul__(self, other):
        if str(self) == '0' or str(other) == '0':
            return LargeInteger('0')
        n = max(len(self), len(other))
        if n < 3:
            return LargeInteger(str(int(self.integer_str) * int(other.integer_str)))
        else:
            m = n // 2
            x = LargeInteger(self.integer_str)
            x.array = x.array[m:] if m < len(x) else [0]
            y = LargeInteger(self.integer_str)
            y.array = y.array[:m]
            w = LargeInteger(other.integer_str)
            w.array = w.array[m:] if m < len(w) else [0]
            z = LargeInteger(other.integer_str)
            z.array = z.array[:m]

            part1 = x * w
            part1.array = [0] * (2*m) + part1.array
            part2 = x * z + w * y
            part2.array = [0] * m + part2.array
            part3 = y * z

            return part1 + part2 + part3

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
