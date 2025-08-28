import click
from scipy.stats import poisson
import csv


@click.command()
@click.argument("input_file", type=click.File("r"))
def main(input_file):
    results = []
    reader = csv.DictReader(input_file)
    for row in reader:
        name = row["name"]
        p_clean_sheet = float(row["p_clean_sheet"])
        avg_def_cons = int(row["def_cons"]) / int(row["starts"])
        expected_points = p_clean_sheet * 4 + poisson.sf(9, avg_def_cons) * 2
        results.append((name, expected_points))
    for name, expected_points in sorted(results, key=lambda x: x[1], reverse=True):
        print(f"{name} {round(expected_points, 3)}")


if __name__ == "__main__":
    main()
