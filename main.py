from pathlib import Path


TEXT = (
    "The empty swing slows.\n\n"
    "Its arc was wide after the children left.\n\n"
    "Now each pass is shorter.\n\n"
    "Forward to the edge of the shade.\n\n"
    "Back almost to the trunk.\n\n"
    "The chain softens.\n\n"
    "A dry leaf catches on one seat and rides three times before it slips off.\n\n"
    "The grass beneath is already rising.\n\n"
    "One more small push of air.\n\n"
    "The swing barely reaches the shadow's edge.\n\n"
    "It hangs.\n\n"
    "Turns a little.\n\n"
    "Settles.\n\n"
    "The chains are quiet.\n\n"
    "The leaf on the ground does not move.\n\n"
    "Evening comes the way the swing stopped—without announcement."
)


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
