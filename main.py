import asyncio
import string


class ProductGenerator:
    def __init__(self, alphabet, repeats, filename):
        self.alphabet = alphabet
        self.repeats = repeats
        self.filename = filename

    async def write_combinations(self, prefix=""):
        if len(prefix) == self.repeats:
            with open(self.filename, "a") as f:
                f.write(prefix + "\n")
            return

        for char in self.alphabet:
            await self.write_combinations(prefix + char)

    async def generate_products(self):
        with open(self.filename, "w"):
            pass  # clear the file if it already exists

        tasks = [self.write_combinations(char) for char in self.alphabet]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    alphabet = string.ascii_lowercase + string.digits
    repeats = 6
    filename = "products.txt"
    pg = ProductGenerator(alphabet, repeats, filename)
    asyncio.run(pg.generate_products())
