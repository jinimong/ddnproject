class FourDigitYearConverter:
    regex = r'[1-2]\d{3}' # 1000 ~ 2999

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d'.format(value)
