from statistics import mean


def calculate_averages(input_file_name, output_file_name):
    """Calculate average scores from an input CSV and write to an output file."""
    with open(input_file_name) as infile:
        lines = infile.readlines()

    with open(output_file_name, "w") as outfile:
        for line in lines:
            parts = line.strip().split(",")
            name = parts[0]
            scores = list(map(int, parts[1:]))
            avg = mean(scores)
            outfile.write(f"{name},{avg:.2f}\n")


def calculate_sorted_averages(input_file_name, output_file_name):
    """Calculate and write sorted averages by name from an input CSV."""
    with open(input_file_name) as infile:
        lines = infile.readlines()

    averages = {}
    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]
        scores = list(map(int, parts[1:]))
        avg = mean(scores)
        averages[name] = avg

    sorted_averages = sorted(averages.items(), key=lambda item: item[0])

    with open(output_file_name, "w") as outfile:
        for name, avg in sorted_averages:
            outfile.write(f"{name},{avg:.2f}\n")
