from qifcleanup.qifcleanup import clean_line


def test_clean_line():
    cases = {
        "!Type:CCard": "!Type:CCard",
        "D27/07/2018": "D27/07/2018",
        "T-123.45": "T-123.45",
        "T-6.54": "T-6.54",
        "M** 8933": "M** 8933",
        "^": "^",
        "PINITIAL BALANCE": "PINITIAL BALANCE",
        "PDD PAYMENT RECEIVED  D/DEBIT": "PDD PAYMENT RECEIVED  D/DEBIT",
        "PPURCHASE - DOMESTIC, MORDOR, TESCO STORES 5884": "PTESCO STORES 1234",
        "PPURCHASE - DOMESTIC, MORDOR, M & S SIMPLY FOOD": "PM & S SIMPLY FOOD",
        "PPURCHASE - DOMESTIC, 35314369991, PAYPAL *EPOSGEAR": "PPAYPAL *EPOSGEAR",
        "PPURCHASE - DOMESTIC, 35314369991, PAYPAL *GIVING COM": "PPAYPAL *GIVING COM",
        "PRECURRENT TRANSACTION, 020 31116494, TEST": "PTEST",
        "PPURCHASE - DOMESTIC, MORDOR, SUBWAY, GBP 10.99": "PSUBWAY"
    }

    for testin, expected in cases.items():
        yield check_clean_line, testin, expected


def check_clean_line(testin, expected):
    testout = clean_line(testin)
    assert testout == expected, '{} is not {}'.format(testout, expected)
