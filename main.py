# from src.api.firestore import firestore

# firestore.init_business("Geminish BM")

# print(firestore.authenticate_user("minhtq2005@gmail.com", "admin1234beforehash"))

# print(firestore.authenticate_user("minhtq2005@gmail.com", "admin1234beforehas"))


from datetime import datetime
import sys
from rich import print, inspect
from src.backend import driver
from src.backend import sample
from rich import print, print_json

def watch(func):
    def inner(*args, **kwargs):
        start = datetime.now()
        try:
            func(*args, **kwargs)        
        finally:
            print(f"Execution time: {(datetime.now() - start).seconds} s.")
    return inner


@watch
def main():
    # sample.main()
    driver.create_driver()


if __name__ == "__main__":
    main()