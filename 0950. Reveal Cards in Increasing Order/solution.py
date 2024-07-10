class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        order = []
        simulation = [i for i in range(len(deck))]

        # play through the simulation. base case is when there is one card left, else we just pick the card and shuffle the next one behind
        while simulation:
            if len(simulation) == 1:
                order.append(simulation[-1])
                break
            else:
                first = simulation.pop(0)
                second = simulation.pop(0)
                order.append(first)
                simulation.append(second)

        # at this point, the order array will have the order of the indices that the deck will be revealed in
        deck.sort()
        result = [0] * len(deck)
        # we sort the deck in increasing order and put them in the corresponding indices in the result array
        for i in range(len(result)):
            result[order[i]] = deck[i]
        return result