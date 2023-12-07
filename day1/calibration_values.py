import sys
from trie import Trie

# Day 1-1 Sum of the calibration values
# c. v. -> number made by the first and last digits of the line
def calibration_value(line: str) -> int:
    i, j = 0, len(line)-1
    while i < j and not(line[i].isdigit()):
        i += 1

    while j > i and not(line[j].isdigit()):
        j -= 1

    return 10*int(line[i]) + int(line[j])


# Day 1-2 Digits can also be spelled out
spelled_digits = ['one','two','three','four','five','six','seven','eight','nine']
prefix, suffix = Trie(), Trie()

for i, sd in enumerate(spelled_digits):
    prefix.insert(sd, i+1)
    suffix.insert(reversed(sd), i+1)

def first_digit(line: str) -> int:
    return find_digit(line, prefix)

def last_digit(line: str) -> int:
    return find_digit(reversed(line), suffix)
            
def find_digit(line: str, spelled: Trie) -> int:
    candidates = []
    for ch in line:
        # If character is digit, we found the answer
        if ch.isdigit():
            return int(ch)

        # Try to advance all the spelled digits candidates
        for i in range(len(candidates)):
            t = candidates[i].find(ch)
            if t is None:
                continue
            candidates[i] = t

        # Check if character can start a spelled digit
        # and include it in the candidates
        t = spelled.find(ch)
        if t is not None:
            candidates.append(t)
        
        # If one of the candidates is terminal, it's the answer
        for c in candidates:
            if c.value != -1:
                return c.value

def calibration_value2(line:str) -> int:
    return 10 * first_digit(line) + last_digit(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please inform the calibration document!")
        exit(0)

    with open(sys.argv[1],"r") as doc:
        answer = sum(
            calibration_value2(line.rstrip())
            for line in doc.readlines()
        )
        print(f"The sum of all the calibration values is {answer}")
