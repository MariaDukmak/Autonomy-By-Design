"""A mini voting systeem."""
import random
from typing import List


class Voting:
    def __init__(self, candidanten: List[str]):
        self.ballot_box = []
        self.choieces = List[str]
        self.ranking = List[int]
        self.candidanten = candidanten

    def add_votes(self, vote:int):
        if len(self.choieces) == len(self.ranking):
            self.ballot_box.append(vote)
        else:
            yield "niet geldige stem!"

    def count_votes(self):
        return {}

    def __str__(self):
        # print( f'Reesults are:{ max(i, y for i, y in zip(self.ballot_box, self.candidanten))}')
        pass


def plurality_votingsystem(votes: Voting):
    pass


if __name__ == "__main__":
    vote = Voting(["a", "b", "c"])
    for _ in range(1000):
        v = [candidat for candidat in range(1, len(vote.candidanten)+1)]
        vote.add_votes(random.sample(vote.candidanten, k=len(vote.candidanten), counts=v))
