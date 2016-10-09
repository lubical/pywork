# property 检查参数及用属性直接访问的利器
# assert 断言，正确不显示，错误显示


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an int')
        if value < 0:
            raise ValueError('height must above 0')
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width
# test:


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
