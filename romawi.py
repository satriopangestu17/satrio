##roman to angka
class solution:
        def romantoangka(self, x):
                roman = {'I':1, 'V':5, 'X':10,
                'L':50, 'C':100, 'D':500, 'M':1000}
                result = 0
                for i in range(0, len(x)-1):
                        a = x[i]
                        aafter = x[i+1]
                        if roman[a] < roman[aafter]:
                                result -= roman[a]
                        else:
                                result += roman[a]
                result+=roman[x[-1]] 
                return result
print(solution().romantoangka('IV'))

##angka to roman

class py_solution:
    def romandict(self, num):
        val = [1000, 900, 500, 400, 100, 90,
        50, 40, 10, 9, 5, 4, 1]
        syb = ['M', 'CM', 'D', 'CD', 'C',
        'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_num = ''
        i = 0
        while num >0:
            for _ in range(num // val [i]):   ##* the result will be integer
                # print(_)
                roman_num += syb[i]
                # print(_)
                num -= val[i]
            i += 1
        return roman_num
print(py_solution().romandict(22))
