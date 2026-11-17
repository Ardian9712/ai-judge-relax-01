from pathlib import Path


TEXT = (
    "By evening, the lake has forgotten the wind. Small ripples loosen, then disappear, until the water holds the sky like a pane of smoked glass. Along the reeds, a heron lifts one foot, sets it down, and waits. A single ring widens behind it, touching the reflection of the darkening pines before fading. On the far shore, the last windows glow softly, then blur into blue. Somewhere, a dock rope taps once against a post. The sound travels a little way and is gone. Nothing crosses the lake now. The evening settles over its surface, and the water keeps the quiet without asking anything of it."
)


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
