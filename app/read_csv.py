import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for line in reader:
      iterable = zip(header, line)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
  return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])