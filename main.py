from pathlib import Path


TEXT = (
    "In the last light of afternoon, a gray cat sleeps on the wide sill above the garden. One paw rests over the edge, opening and closing once in a dream, while the sun warms the silver fur along its back. Dust turns slowly in the golden air. Beyond the glass, a small branch moves with the breeze, and a bird settles among the leaves. The house holds its quiet: a kettle cooling in the kitchen, curtains barely stirring, the clock making its patient rounds. The cat's whiskers tremble, then smooth. Nothing is waiting at the door. The light stays a little longer, soft on the sill, soft on the garden, soft on the sleeping cat."
)


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
