import random
import string

def randon_nok_serial():
    lt = 3
    random_alpha = "".join(random.choice(string.ascii_uppercase) for _ in range(lt))
    lt2 = 3
    random_alpha2 = "".join(random.choice(string.ascii_uppercase) for _ in range(lt2))
    random_number = str(random.randint(1000000, 9999999))
    random_number2 = str(random.randint(1000, 9999))
    unique = "NOK" + random_number2 + random_number + random_alpha2 + random_alpha
    return unique
