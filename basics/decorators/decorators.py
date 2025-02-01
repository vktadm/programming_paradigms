def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("----Действие до функции----")
        func(*args, **kwargs)
        print("----Действие после функции")

    return wrapper


def func_decorator_return(func):
    def wrapper(*args, **kwargs):
        print("----Действие до функции----")
        result = func(*args, **kwargs)
        print("----Действие после функции")
        return result

    return wrapper


@func_decorator
def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")


@func_decorator_return
def some_func_return(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"

# Прописываем декорирование через замыкание
# some_func = func_decorator(some_func)
# some_func_return = func_decorator_return(some_function_return)

if __name__ == '__main__':
    some_func("Python forever!", "h1")
    func_result = some_func_return("New line", "h2")
    print("\n" + func_result)
