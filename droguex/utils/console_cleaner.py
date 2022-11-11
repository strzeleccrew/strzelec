import os


def console_clean(function):
    def cleaner(*args, **kwargs):
        os.system('cls')
        a = function(*args, **kwargs)
        return a

    return cleaner
