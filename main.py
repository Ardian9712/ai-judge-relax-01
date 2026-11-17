from pathlib import Path


TEXT = (
    "The last plate is stacked. The sink is empty, still faintly warm from the water. The kettle sits quiet on the cold burner, its whistle long finished. A single low lamp over the counter leaves the rest of the room in soft shadow. The wooden chair is pulled slightly away from the table, its seat empty, waiting for nothing. Outside the window the street is dark. Inside, the air smells of soap and the last of the evening's bread. No timer ticks. No list remains. The house holds its breath the way a room does when the day has finally set everything down."
)


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
