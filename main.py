import logging
import pathlib
from string import ascii_lowercase, digits
from typing import Generator, Iterable

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

    def generate_combinations(self) -> Generator[str, None, None]:
        self.logger.info("[START] Combining started [START]")
        yield from self._generate_combinations_recursive("")
        self.logger.info(
            "[END] All combinations created successfully. See result.txt file [END]"
        )

    def _generate_combinations_recursive(
        self, prefix: str
    ) -> Generator[str, None, None]:
        if len(prefix) == self.str_len:
            yield prefix
            return

        for char in self.alphabet:
            yield from self._generate_combinations_recursive(prefix + char)


if __name__ == "__main__":
    repeats = 5
    alphabet_for_combinations = ascii_lowercase + digits
    combinator = Combinator(alphabet_for_combinations, repeats)
    with open(STORAGE.joinpath("result/result.txt"), mode="w") as file_result:
        for combination in combinator.generate_combinations():
            file_result.write(combination + "\n")
