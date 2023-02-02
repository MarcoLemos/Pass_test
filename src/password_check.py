from re import findall, search


class VarNames:
    """
    Variables names for backend/frontend contract.
    """

    min_size = 'minSize'
    min_upper_case = 'minUppercase'
    min_lower_case = 'minLowercase'
    min_digit = 'minDigit'
    min_special_chars = 'minSpecialChars'
    no_repeated = 'noRepeted'


class PassRules:
    """
    Class receve two parameters password and rules.
    Then verify if the given password is in conformity with the rules.
    """

    def __init__(self, password, rules):
        self.password = password
        self.rules = {
            VarNames.min_size: 0,
            VarNames.min_upper_case: 0,
            VarNames.min_lower_case: 0,
            VarNames.min_digit: 0,
            VarNames.min_special_chars: 0,
            VarNames.no_repeated: 0,
        }
        self.no_macht = []
        self.verify = bool(self.no_macht)

        for rule in rules:
            self.rules[rule['rule']] = rule['value']

    def min_pass_size(self):
        min_size = self.rules[VarNames.min_size]
        total_size = len(self.password)
        if total_size < min_size:
            self.no_macht.append(VarNames.min_size)

    def min_pass_upper(self):
        min_upper = self.rules[VarNames.min_upper_case]
        upper_size = sum(map(str.isupper, self.password))
        if upper_size < min_upper:
            self.no_macht.append(VarNames.min_upper_case)

    def min_pass_lower(self):
        min_lower = self.rules[VarNames.min_lower_case]
        lower_size = sum(map(str.islower, self.password))
        if lower_size < min_lower:
            self.no_macht.append(VarNames.min_lower_case)

    def min_pass_digit(self):
        min_digit = self.rules[VarNames.min_digit]
        digit_size = sum(map(str.isdigit, self.password))
        if digit_size < min_digit:
            self.no_macht.append(VarNames.min_digit)

    def min_pass_special(self):
        min_special = self.rules[VarNames.min_special_chars]
        regex = '[@_!#$%^&*()<>?/\|}{~:]'
        special_size = len(findall(regex, self.password))
        if special_size < min_special:
            self.no_macht.append(VarNames.min_special_chars)

    def pass_repeticion(self):
        max_repetition = self.rules[VarNames.no_repeated]
        if max_repetition > 1:
            regex = '(.)\\1{' + str(max_repetition - 1) + '}'
            repetitions = bool(search(rf'{regex}', self.password))
            if repetitions:
                self.no_macht.append(VarNames.no_repeated)

    def check_all(self):
        self.min_pass_size()
        self.min_pass_upper()
        self.min_pass_lower()
        self.min_pass_digit()
        self.min_pass_special()
        self.pass_repeticion()

        return self.no_macht
