import string
import random


class PasswordGenerator:
    def __init__(self,
                 length,
                 include_symbols,
                 include_numbers,
                 include_uppercase
                 ):
        """
        :param length: Length of the password
        :param include_symbols: include symbols like @#$%^&*
        :param include_numbers: include numbers
        :param include_uppercase: upper-case letters
        """
        self.length = length
        self.include_symbols = include_symbols
        self.include_numbers = include_numbers
        self.include_uppercase = include_uppercase

    def generate_password(self):
        if self.length < 6:
            raise ValueError('Password cannot be less than 6 characters.!')
        elif self.length > 16:
            raise ValueError('Password can be only of maximum 16 characters.!')

        all_checks = self.include_symbols and self.include_numbers and self.include_uppercase

        if all_checks:
            return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                          string.digits + string.punctuation, k=self.length))

        pwd = []
        if self.include_symbols:
            pwd.append(random.choice(string.punctuation))
        if self.include_numbers:
            pwd.append(random.choice(string.digits))
        if self.include_uppercase:
            pwd.append(random.choice(string.ascii_uppercase))

        remaining_len = self.length - len(pwd)
        pwd.extend(random.choices(string.ascii_lowercase, k=remaining_len))
        random.shuffle(pwd)

        return ''.join(pwd)


if __name__ == '__main__':
    obj = PasswordGenerator(10, True, True, True)
    rand_pwd = obj.generate_password()
    print(rand_pwd)
