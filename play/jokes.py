def dark_joke():
  url = 'https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw' #https://sv443.net/jokeapi/v2/
  response = requests.get(url)
  res = response.json()
  part1, part2 = res['setup'], res['delivery']
  x = []
  joke = (part1, part2)
  setup, line = joke[0], joke[1]
  x.append(setup)
  x.append(line)
  return x

print(dark_joke())
