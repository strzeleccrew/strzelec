import os


def console_clean(function):
    def cleaner(*args, **kwargs):
        a = function(*args, **kwargs)
        os.system('cls')
        return a

    return cleaner
