import utils

k, v = utils.get_population()
print(k)
print(v)

#print(utils.A)

cntry_list = [
  {
  "Country": "Mexico",
  "Population": 500
  },
  {
    "Country": "Colombia",
    "Population": 1000
  }
]

result = utils.population_by_country(cntry_list, 'Mexico')
print(result)