
key_to_direction = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}
Key = "Up"
current = key_to_direction[Key]
meow = current[1]
print(meow)