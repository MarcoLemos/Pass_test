"""Test PassRules and his functions"""
from src.password_check import PassRules, VarNames

var_names = VarNames

pass_rules = PassRules(
    'TeeesteSenhaForte!123&',
    [
        {'rule': var_names.min_size, 'value': 25},
        {'rule': var_names.min_upper_case, 'value': 4},
        {'rule': var_names.min_lower_case, 'value': 16},
        {'rule': var_names.min_special_chars, 'value': 3},
        {'rule': var_names.no_repeated, 'value': 2},
        {'rule': var_names.min_digit, 'value': 4},
    ],
)


def test_min_pass_size():
    pass_rules.min_pass_size()
    assert var_names.min_size in pass_rules.no_macht


def test_min_pass_upper():
    pass_rules.min_pass_upper()
    assert var_names.min_upper_case in pass_rules.no_macht


def test_min_pass_lower():
    pass_rules.min_pass_lower()
    assert var_names.min_lower_case in pass_rules.no_macht


def test_min_pass_digit():
    pass_rules.min_pass_digit()
    assert var_names.min_digit in pass_rules.no_macht


def test_min_pass_special():
    pass_rules.min_pass_special()
    assert var_names.min_special_chars in pass_rules.no_macht


def test_pass_repetition():
    pass_rules.pass_repetition()
    assert var_names.no_repeated in pass_rules.no_macht


def test_verify():
    if pass_rules.no_macht:
        assert pass_rules.verify is False
    else:
        assert pass_rules.verify is True


def test_check_all():
    pass_rules.no_macht = []
    pass_rules.check_all()
    assert var_names.min_size in pass_rules.no_macht
    assert var_names.min_upper_case in pass_rules.no_macht
    assert var_names.min_lower_case in pass_rules.no_macht
    assert var_names.min_special_chars in pass_rules.no_macht
    assert var_names.no_repeated in pass_rules.no_macht
    assert var_names.min_digit in pass_rules.no_macht
