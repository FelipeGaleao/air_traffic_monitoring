from deltalake import DeltaTable, write_deltalake

class DeltaRSAdapter:
    def __init__(self):
        pass

    def write_to_deltalake(self, data, mode="append"):
        write_deltalake("./data/delta", data, mode=mode)