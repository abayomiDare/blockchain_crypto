from block import Block


class BlockChain:
    """
    Blockchain is a public ledger of transactions
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain: list = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self) -> str:
        return f"BlockChain: {self.chain}"


def main():
    block_chain = BlockChain()
    block_chain.add_block("one")
    block_chain.add_block("two")

    print(block_chain)


if __name__ == "__main__":
    main()
