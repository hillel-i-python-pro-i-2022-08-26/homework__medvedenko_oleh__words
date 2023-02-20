import logging
import pathlib
import asyncio
from string import ascii_lowercase, digits
from typing import AsyncGenerator, Iterable
import aiofiles

STORAGE = pathlib.Path(__file__).parent.joinpath("words_storage")


def init_logger() -> logging.Logger:
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    return logger


class Combinator:
    def __init__(
            self,
            alphabet: Iterable,
            str_len: int,
            logger: logging.Logger = init_logger(),
    ):
        self.alphabet = alphabet
        self.str_len = abs(str_len)
        self.logger = logger

    async def generate_combinations(self) -> AsyncGenerator[str, None]:
        self.logger.info("[START] Combining started [START]")
        async for combination in self._generate_combinations_recursive(""):
            yield combination
        self.logger.info(
            "[END] All combinations created successfully. See result.txt file [END]"
        )

    async def _generate_combinations_recursive(
            self, prefix: str
    ) -> AsyncGenerator[str, None]:
        if len(prefix) == self.str_len:
            yield prefix
            return

        for char in self.alphabet:
            async for combination in self._generate_combinations_recursive(prefix + char):
                yield combination
                # self.logger.info(combination)


async def main():
    repeats = 3
    alphabet_for_combinations = ascii_lowercase + digits
    combinator = Combinator(alphabet_for_combinations, repeats)
    async with aiofiles.open(STORAGE.joinpath("result/result.txt"), mode="w") as file_result:
        async for combination in combinator.generate_combinations():
            await file_result.write(combination + "\n")


if __name__ == "__main__":
    asyncio.run(main())
