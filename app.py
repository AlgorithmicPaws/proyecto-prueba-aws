import pandas as pd
from utils import is_prime
def f(event, context):
    print("Hola soy una lambda")
    print(is_prime(5))
    return {}