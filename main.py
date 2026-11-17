from pathlib import Path


TEXT = (
    "In the old barn, moonlight lies in a narrow stripe across the hay. A little owl sleeps on the beam above the quiet stalls, feathers rounded against the night air. Below, a mare shifts her weight and settles, the straw whispering under one hoof. The wooden door rests against its latch; beyond it, the fields are silver with dew. A moth circles the lantern once and disappears into the rafters. The owl’s head turns beneath one wing. Nothing moves except the faint dust in the moonbeam, drifting down through the warm, still dark."
)


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
