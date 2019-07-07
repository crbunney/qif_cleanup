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
        "PDD PAYMENT RECEIVED  D/DEBIT, GBP -51.90": "PDD PAYMENT RECEIVED  D/DEBIT",
        "PPURCHASE - DOMESTIC, MORDOR, TESCO STORES 1234": "PTESCO STORES 1234",
        "PPURCHASE - DOMESTIC, MORDOR, M & S SIMPLY FOOD": "PM & S SIMPLY FOOD",
        "PPURCHASE - DOMESTIC, 35314369991, PAYPAL *EPOSGEAR": "PPAYPAL *EPOSGEAR",
        "PPURCHASE - DOMESTIC, 35314369991, PAYPAL *GIVING COM": "PPAYPAL *GIVING COM",
        "PRECURRENT TRANSACTION, 020 31116494, TEST": "PTEST",
        "PPURCHASE - DOMESTIC, MORDOR, SUBWAY, GBP 10.99": "PSUBWAY",
        "PMAINTAINING THE ACCOUNT - MONTHLY FEE, 0.00": "PMAINTAINING THE ACCOUNT - MONTHLY FEE",
        "PCASH WITHDRAWAL AT TESCO PERSONAL FINANCE ATM TESCO PLY B RD, PLYMOUTH,200.00 GBP , ON 11-, 200.00":
            "PCASH WITHDRAWAL AT TESCO PERSONAL FINANCE ATM TESCO PLY B RD, PLYMOUTH",
        "PCARD PAYMENT TO ALDI 25 780,30.59 GBP, RATE 1.00/GBP ON 14-01-2019, 30.59": "PCARD PAYMENT TO ALDI 25 780"
    }

    for testin, expected in cases.items():
        yield check_clean_line, testin, expected


def check_clean_line(testin, expected):
    testout = clean_line(testin)
    assert testout == expected, '{} is not {}'.format(testout, expected)
