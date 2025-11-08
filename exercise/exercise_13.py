NUMBER_OF_DISKS = 5

# Use descriptive names for the pegs
source_peg = list(range(NUMBER_OF_DISKS, 0, -1))
auxiliary_peg = []
target_peg = []


def move_disks(n, source, auxiliary, target):
    """Move n disks from source to target using auxiliary peg."""
    if n <= 0:
        return

    # Move n - 1 disks from source to auxiliary
    move_disks(n - 1, source, target, auxiliary)

    # Move the nth disk from source to target
    target.append(source.pop())

    # Display current state of pegs
    print(source_peg, auxiliary_peg, target_peg, "\n")

    # Move the n - 1 disks from auxiliary to target
    move_disks(n - 1, auxiliary, source, target)


# Initiate the call from source_peg to target_peg using auxiliary_peg
move_disks(NUMBER_OF_DISKS, source_peg, auxiliary_peg, target_peg)
