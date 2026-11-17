from pathlib import Path


TEXT = (
    "On the porch, a woman dozes in a rocking chair, a quilt loose over her knees.\n\n"
    "The hem brushes a knot in the floorboard, then draws back. The chair comes forward. The hem brushes the knot again.\n\n"
    "For a while it goes just that far, with a low creak from one runner. Then the hem reaches only the near edge of the knot. On the next pass, a little less.\n\n"
    "The chair still rocks, but the creak has gone. The hem moves over a smaller patch of wood, back and forth, until a loose thread rests against the board.\n\n"
    "It lifts once more.\n\n"
    "Then it lies along the grain of the wood."
)


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
