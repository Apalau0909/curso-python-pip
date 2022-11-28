def get_population():
  keys = ['col', 'bol', 'mex']
  values = [300, 400, 500]
  return(keys, values)

def population_by_country(data, country):
  ## Data will contain a list of dicts with Country and Population as keys
  ## Country will be the country selected to return the population
  result = list(filter(lambda x: x['Country'] == country, data))
  return result