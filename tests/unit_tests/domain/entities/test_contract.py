def test_create_contract(session, dummy_contract):
    contract = dummy_contract
    session.add(contract)
    session.commit()

    assert contract.id is not None


def test_contract_repr(dummy_contract):
    contract = dummy_contract
    assert repr(contract) == "Contract, status: signed, total_amount: 1000.0"
