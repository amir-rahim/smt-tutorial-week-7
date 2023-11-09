import os, random

with open("test_file", "wb") as f:
    for i in range(random.randint(0, 10000)):
        f.write(random.randint(0, 255).to_bytes(1, 'little'))

    os.system("cat test_file")

# Run this multiple times
