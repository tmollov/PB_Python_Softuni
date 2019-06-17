import math as m

serial = input()
seasons = int(input())
episodes = int(input())
length = float(input())

ads = length * 0.2
specialEpisodes = seasons * 10
result = ((length + ads) * seasons * episodes) + specialEpisodes
print(f"Total time needed to watch the {serial} series is {m.ceil(result)} minutes.")