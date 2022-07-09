from turtle import color
import colorama
import math

class ProgressBar:
    def __init__(self, progress, total, color = colorama.Fore.CYAN):

        percent = 100 * (progress /  float(total))
        # alt + 2 1 9 for █
        bar = '█' * int(percent) + '-' * (100 - int(percent))
        if color == "blue":
            pass
        print(color+f"\r|{bar}| {percent:.2f}%"+colorama.Fore.RESET, end="\r")


numbers = [x * 5 for x in range(2000, 3000)]
results = []

ProgressBar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    ProgressBar(i + 1, len(numbers))

print(f"\n\nfinished!")