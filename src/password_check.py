from re import findall


class PassRules:
    def __init__(self, password, rules):
        self.password = password
        self.rules = {
            'minSize': 0,
            'minUppercase': 0,
            'minLowercase': 0,
            'minDigit': 0,
            'minSpecialChars': 0,
            'noRepeted': 0,
        }
        self.no_machts = []

        for rule in rules:
            self.rules[rule['rule']] = rule['value']

    def min_pass_size(self):
        arg = 'minSize'
        min_size = self.rules[arg]
        total_size = len(self.password)
        if total_size < min_size:
            self.no_machts.append(arg)

    def min_pass_upper(self):
        arg = 'minUppercase'
        min_upper = self.rules[arg]
        upper_size = [char.isupper() for char in self.password].count(True)
        if upper_size < min_upper:
            self.no_machts.append(arg)

    def min_pass_lower(self):
        arg = 'minLowercase'
        min_lower = self.rules[arg]
        lower_size = [char.islower() for char in self.password].count(True)
        if lower_size < min_lower:
            self.no_machts.append(arg)

    def min_pass_digit(self):
        arg = 'minDigit'
        min_digit = self.rules[arg]
        digit_size = [char.isdigit() for char in self.password].count(True)
        if digit_size < min_digit:
            self.no_machts.append(arg)

    def min_pass_special(self):
        arg = 'minSpecialChars'
        min_special = self.rules[arg]
        regex = '[@_!#$%^&*()<>?/\|}{~:]'
        special_size = len(findall(regex, self.password))
        if special_size < min_special:
            self.no_machts.append(arg)

    def pass_repeticion(self):
        arg = 'noRepeted'
        max_repetition = self.rules[arg]
        if max_repetition:
            regex = '((.)\2{{{max_repetition}}})'.format(
                max_repetition=str(max_repetition) + ','
            )
            repetitions = bool(findall(rf'{regex}', self.password))
            if repetitions:
                self.no_machts.append(arg)

    def check_all(self):
        self.min_pass_size()
        self.min_pass_upper()
        self.min_pass_lower()
        self.min_pass_digit()
        self.min_pass_special()
        self.pass_repeticion()

        return self.no_machts
