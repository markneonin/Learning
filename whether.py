# Приложение может выводит день с максимальным АД за предстоящие 5 дней,
# также может выводить день с минимальной разницей ночной и утренней t

import requests
from collections import defaultdict as dd


class WheatherApp:
	
	def __init__(self, city, key):
		self.key = key
		self.city = city
		self.get_wheather_data(self.city)
	
	def get_wheather_data(self, city):
		url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.key}'
		res = requests.get(url)
		new_wh_data = res.json()
		self.wh_data = new_wh_data
		return new_wh_data
	
	def get_max_pressure(self):
		pressure = 0
		day = None
		
		for item in self.wh_data['list']:
			press =  item['main']['pressure']
			if press > pressure:
				pressure = press
				date = item['dt_txt'].split()[0]
		
		return date, pressure
	
	def to_celsius(self, kelvin):
		celsius = kelvin - 273.15
		return celsius
	
	def get_day_with_min_diff(self):
		diff = dd(list)
		
		for item in self.wh_data['list']:
			date, time = item['dt_txt'].split()
			if time == '03:00:00' or '09:00:00' == time:
				diff[date].append(item['main']['temp'])
		diff_list = []
		for date, values in diff.items():
			if len(values) == 2:
				morn = self.to_celsius(values[1])
				night = self.to_celsius(values[0])
	
				difference = round(abs(morn - night), 2)
				diff_list.append((date, difference))
		
		diff_list.sort(key=lambda x: x[1])
		date, diff = diff_list[0]
		
		return date, diff


if __name__ == '__main__':
	API_key = 'ec9ba0fb7778aaef12d0c3e19bc64da7'
	app = WheatherApp('Perm', API_key)
	
	date, pressure = app.get_max_pressure()
	print(f'Максимальное атмосферное давление будет {date}, оно составит {pressure} mm Hg\n')
	
	date, diff = app.get_day_with_min_diff()
	print( f'Минимальная разница между ночной (03:00) и утренней (09:00) температурами будет {date} и составит {diff}℃')
	
	
	
	
	
	
	
				
	
		








