#!/usr/bin/env python
# interactive_color_sampler_full.py - Includes 256-color + forced RGB

ESC = "\033["
RESET = f"{ESC}0m"

# ==== 16-COLOR FOREGROUNDS (A–P) ====
FG_16_MAP = {
  "A": ("Black",    30),
  "B": ("Red",      31),
  "C": ("Green",    32),
  "D": ("Yellow",     33),
  "E": ("Blue",     34),
  "F": ("Magenta",    35),
  "G": ("Cyan",     36),
  "H": ("White",    37),
  "I": ("BrightBlack",  90),
  "J": ("BrightRed",  91),
  "K": ("BrightGreen",  92),
  "L": ("BrightYellow", 93),
  "M": ("BrightBlue",   94),
  "N": ("BrightMagenta",95),
  "O": ("BrightCyan",   96),
  "P": ("BrightWhite",  97),
}

# ==== 16-COLOR BACKGROUNDS (1–16) ====
BG_16_MAP = {
  1:  ("Black",    40),
  2:  ("Red",      41),
  3:  ("Green",    42),
  4:  ("Yellow",     43),
  5:  ("Blue",     44),
  6:  ("Magenta",    45),
  7:  ("Cyan",     46),
  8:  ("White",    47),
  9:  ("BrightBlack", 100),
  10: ("BrightRed",   101),
  11: ("BrightGreen", 102),
  12: ("BrightYellow",103),
  13: ("BrightBlue",  104),
  14: ("BrightMagenta",105),
  15: ("BrightCyan",  106),
  16: ("BrightWhite", 107),
}

# ==== 256-COLOR FOREGROUNDS (Q–X) ====
FG_256_MAP = {
  "Q": ("Idx28_dark_green",   "38;5;28"),
  "R": ("Idx40_green",    "38;5;40"),
  "S": ("Idx46_bright_green", "38;5;46"),
  "T": ("Idx160_red",     "38;5;160"),
  "U": ("Idx196_bright_red",  "38;5;196"),
  "V": ("Idx190_yellow",    "38;5;190"),
  "W": ("Idx226_bright_yel",  "38;5;226"),
  "X": ("Idx21_blue",     "38;5;21"),
}

# ==== 256-COLOR BACKGROUNDS (17–24) ====
BG_256_MAP = {
  17: ("Idx28_dark_green",   "48;5;28"),
  18: ("Idx40_green",    "48;5;40"),
  19: ("Idx46_bright_green", "48;5;46"),
  20: ("Idx160_red",     "48;5;160"),
  21: ("Idx196_bright_red",  "48;5;196"),
  22: ("Idx190_yellow",    "48;5;190"),
  23: ("Idx226_bright_yel",  "48;5;226"),
  24: ("Idx21_blue",     "48;5;21"),
}

# ==== FORCED RGB FOREGROUNDS (Y–Z, AA–AD) ====
FG_RGB_MAP = {
  "Y": ("ForcedDarkGreen",  "38;2;0;128;0"),
  "Z": ("ForcedLightGreen", "38;2;144;238;144"),
  "AA":("ForcedDarkRed",  "38;2;139;0;0"),
  "BB":("ForcedLightRed",   "38;2;255;99;71"),
  "CC":("ForcedDarkYellow", "38;2;184;134;11"),
  "DD":("ForcedLightYellow","38;2;255;255;0"),
}

# ==== FORCED RGB BACKGROUNDS (25–30) ====
BG_RGB_MAP = {
  25: ("ForcedDarkGreen",  "48;2;0;128;0"),
  26: ("ForcedLightGreen", "48;2;144;238;144"),
  27: ("ForcedDarkRed",  "48;2;139;0;0"),
  28: ("ForcedLightRed",   "48;2;255;99;71"),
  29: ("ForcedDarkYellow", "48;2;184;134;11"),
  30: ("ForcedLightYellow","48;2;255;255;0"),
}

def get_fg_code(id):
  if id in FG_16_MAP:
    return FG_16_MAP[id]
  elif id in FG_256_MAP:
    return FG_256_MAP[id]
  elif id in FG_RGB_MAP:
    return FG_RGB_MAP[id]
  return None

def get_bg_code(num):
  if num in BG_16_MAP:
    return BG_16_MAP[num]
  elif num in BG_256_MAP:
    return BG_256_MAP[num]
  elif num in BG_RGB_MAP:
    return BG_RGB_MAP[num]
  return None

def print_all_palettes():
  # 16-color FG
  print("==== THEMED 16-COLOR FOREGROUND (A–P) ====")
  for letter, (name, code) in FG_16_MAP.items():
    seq = f"{ESC}{code}m"
    print(f"{letter}: {seq}{name:20}{RESET}  # fg={code}")

  # 256-color FG
  print("\n==== 256-COLOR FOREGROUND (Q–X) ====")
  for letter, (name, code) in FG_256_MAP.items():
    seq = f"{ESC}{code}m"
    print(f"{letter}: {seq}{name:20}{RESET}  # fg={code}")

  # RGB FG
  print("\n==== FORCED RGB FOREGROUND (Y–Z, AA–DD) ====")
  for letter, (name, code) in FG_RGB_MAP.items():
    seq = f"{ESC}{code}m"
    print(f"{letter}: {seq}{name:20}{RESET}  # fg={code}")

  # 16-color BG
  print("\n==== THEMED 16-COLOR BACKGROUND (1–16) ====")
  for num, (name, code) in BG_16_MAP.items():
    seq = f"{ESC}{code}m"
    print(f"{num}:  {seq} {name:20} {RESET}  # bg={code}")

  # 256-color BG
  print("\n==== 256-COLOR BACKGROUND (17–24) ====")
  for num, (name, code) in BG_256_MAP.items():
    seq = f"{ESC}{code}m"
    print(f"{num}:  {seq} {name:20} {RESET}  # bg={code}")

  # RGB BG
  print("\n==== FORCED RGB BACKGROUND (25–30) ====")
  for num, (name, code) in BG_RGB_MAP.items():
    seq = f"{ESC}{code}m"
    print(f"{num}:  {seq} {name:20} {RESET}  # bg={code}")

def sample_pair(fg_id, bg_num):
  fg_name, fg_code = get_fg_code(fg_id)
  bg_name, bg_code = get_bg_code(bg_num)
  if fg_name is None:
    print(f"Unknown text color '{fg_id}'. Use A–P, Q–X, Y–Z, AA–DD.")
    return
  if bg_name is None:
    print(f"Unknown highlight '{bg_num}'. Use 1–30.")
    return
  
  seq = f"{ESC}{fg_code};{bg_code}m"
  text = f"{fg_name} text on {bg_name} highlight"
  print(f"{seq}{text}{RESET}  # fg={fg_code}, bg={bg_code}")

def sample_all_highlights_for_fg(fg_id):
  fg_name, fg_code = get_fg_code(fg_id)
  if fg_name is None:
    print(f"Unknown text color '{fg_id}'. Use A–P, Q–X, Y–Z, AA–DD.")
    return
  
  print(f"\nAll highlights for text color {fg_id} ({fg_name}):")
  all_bg_nums = sorted(set(list(BG_16_MAP) + list(BG_256_MAP) + list(BG_RGB_MAP)))
  for num in all_bg_nums:
    bg_name, bg_code = get_bg_code(num)
    seq = f"{ESC}{fg_code};{bg_code}m"
    text = f"{fg_name} text on {bg_name} highlight  ({fg_id}{num})"
    print(f"{seq}{text}{RESET}  # fg={fg_code}, bg={bg_code}")

def sample_all_text_for_bg(bg_num):
  bg_name, bg_code = get_bg_code(bg_num)
  if bg_name is None:
    print(f"Unknown highlight '{bg_num}'. Use 1–30.")
    return
  
  print(f"\nAll text colors for highlight {bg_num} ({bg_name}):")
  all_fg_ids = sorted(list(FG_16_MAP) + list(FG_256_MAP) + list(FG_RGB_MAP))
  for fg_id in all_fg_ids:
    fg_name, fg_code = get_fg_code(fg_id)
    seq = f"{ESC}{fg_code};{bg_code}m"
    text = f"{fg_name} text on {bg_name} highlight  ({fg_id}{bg_num})"
    print(f"{seq}{text}{RESET}  # fg={fg_code}, bg={bg_code}")

def parse_choice(choice):
  choice = choice.strip().upper()
  if not choice:
    return None, None, "empty"

  # Extract letters (text color) and digits (highlight)
  letters = ""
  digits = ""
  for ch in choice:
    if ch.isalpha():
      letters += ch
    elif ch.isdigit():
      digits += ch

  fg_id = letters if letters else None
  bg_num_str = digits if digits else None
  bg_num = int(bg_num_str) if bg_num_str else None

  return fg_id, bg_num, "ok"

def main():
  print("ANSI color demo in Windows Terminal (16-color + 256-color + RGB)")
  print("Switch between dark/light schemes to compare.\n")

  print_all_palettes()

  while True:
    try:
      choice = input("\nSample a color? (e.g. D5, 5D, D, 5, or blank to exit) > ")
    except EOFError:
      break

    if not choice.strip():
      break

    fg_id, bg_num, status = parse_choice(choice)
    if fg_id and bg_num is not None:
      sample_pair(fg_id, bg_num)
    elif fg_id:
      sample_all_highlights_for_fg(fg_id)
    elif bg_num is not None:
      sample_all_text_for_bg(bg_num)
    else:
      print("Please specify at least a letter or number (e.g. D5, D, 5).")

  print("\nDone.")

if __name__ == "__main__":
  main()
