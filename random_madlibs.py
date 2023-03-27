from sample_madlibs import sw, rap
import random


if __name__ == "__main__":
    m = random.choice([sw, rap])
    m.madlib()
