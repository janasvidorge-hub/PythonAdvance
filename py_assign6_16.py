class Knapsack:

    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)

    # Top-Down approach using Memoization
    def top_down(self):
        memo = {}

        def solve(i, remaining):
            if i == 0 or remaining == 0:
                return 0

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            if self.weights[i - 1] > remaining:
                result = solve(i - 1, remaining)
            else:
                include = self.values[i - 1] + solve(
                    i - 1,
                    remaining - self.weights[i - 1]
                )

                exclude = solve(i - 1, remaining)

                result = max(include, exclude)

            memo[(i, remaining)] = result
            return result

        return solve(self.n, self.capacity)

    # Bottom-Up approach using Dynamic Programming
    def bottom_up(self):
        dp = [
            [0] * (self.capacity + 1)
            for _ in range(self.n + 1)
        ]

        for i in range(1, self.n + 1):
            for w in range(self.capacity + 1):

                if self.weights[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]

                else:
                    include = (
                        self.values[i - 1]
                        + dp[i - 1][w - self.weights[i - 1]]
                    )

                    exclude = dp[i - 1][w]

                    dp[i][w] = max(include, exclude)

        return dp[self.n][self.capacity]


# Main program
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsack = Knapsack(weights, values, capacity)

print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)

print("\nUsing Top-Down Approach:")
print("Maximum Value:", knapsack.top_down())

print("\nUsing Bottom-Up Approach:")
print("Maximum Value:", knapsack.bottom_up())