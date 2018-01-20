class Function1():

    @staticmethod
    def request(next_func):
        def func():
            print('func1 begin')
            next_func()
            print('func1 end')
        return func


class Function2():

    @staticmethod
    def request(next_func):
        def func():
            print('func2 begin')
            next_func()
            print('func2 end')
        return func


class Function3():

    @staticmethod
    def request(next_func):
        def func():
            print('func3 begin')
            next_func()
            print('func3 end')
        return func


def core():
    print('core')


func = core
functions = [Function1.request, Function2.request, Function3.request]
for f in functions:
    func = f(func)

func()

# result
#
# func3 begin
# func2 begin
# func1 begin
# core
# func1 end
# func2 end
# func3 end
