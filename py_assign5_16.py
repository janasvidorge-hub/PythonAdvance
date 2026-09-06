class LCS:

    def __init__(self, sequence1, sequence2):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.table = []

    # Dynamic Programming method
    def find_lcs(self):
        m = len(self.sequence1)
        n = len(self.sequence2)

        # Create DP table
        self.table = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if self.sequence1[i - 1] == self.sequence2[j - 1]:
                    self.table[i][j] = self.table[i - 1][j - 1] + 1
                else:
                    self.table[i][j] = max(
                        self.table[i - 1][j],
                        self.table[i][j - 1]
                    )

        # Reconstruct LCS
        i = m
        j = n
        lcs = []

        while i > 0 and j > 0:

            if self.sequence1[i - 1] == self.sequence2[j - 1]:
                lcs.append(self.sequence1[i - 1])
                i -= 1
                j -= 1

            elif self.table[i - 1][j] >= self.table[i][j - 1]:
                i -= 1

            else:
                j -= 1

        lcs.reverse()

        return ''.join(lcs)

    # Display DP table
    def display_table(self):
        print("\nDynamic Programming Table:")

        for row in self.table:
            print(row)


# Main program
first_sequence = input("Enter the first sequence: ")
second_sequence = input("Enter the second sequence: ")

lcs = LCS(first_sequence, second_sequence)

result = lcs.find_lcs()

print("\nLongest Common Subsequence:", result)
print("LCS Length:", len(result))

lcs.display_table()