# consensus/config.py


def configure_consensus(consensus_type="pow", difficulty=4, staking_wallets=None):
    """
    Configures the consensus mechanism.
    """
    if consensus_type not in {"pow", "pos", "hybrid"}:
        raise ValueError(f"Invalid consensus type: {consensus_type}")

    return {
        "mechanism": consensus_type,
        "difficulty": difficulty,
        "staking_wallets": staking_wallets or {},
    }
