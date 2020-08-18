from django.shortcuts import render


def home(request):
	import json
	import requests

	if request.method == "POST":
		area = request.POST['area']
		api_request = requests.get('https://api.waqi.info/feed/'+ area +'/?token=*********')
		# API key goes in **** above

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error"

		if api['data']['aqi'] < 51:
			category = "Good"
			category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk"
			category_color = "good"
		elif api['data']['aqi'] < 101:
			category = "Moderate"
			category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api['data']['aqi'] < 151:
			category = "Unhealthy for Sensitive Groups"
			category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			category_color = "usg"
		elif api['data']['aqi'] < 201:
			category = "Unhealthy"
			category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
			category_color = "unhealthy"
		elif api['data']['aqi'] < 301:
			category = "Very Unhealthy"
			category_description = "(201 - 300) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "veryunhealthy"
		else:
			category = "Hazardous"
			category_description = "(300+) Health alert: everyone may experience more serious health effects"
			category_color = "hazardous"


		return render(request, 'home.html', {
			'api' : api, 
			'category': category, 
			'category_description' : category_description, 
			'category_color': category_color,
			})

	else:
		api_request = requests.get('https://api.waqi.info/feed/london/?token=*****')
		# API key goes in **** above

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api['status'] = "error"

		if api['data']['aqi'] < 51:
			category = "Good"
			category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk"
			category_color = "good"
		elif api['data']['aqi'] < 101:
			category = "Moderate"
			category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api['data']['aqi'] < 151:
			category = "Unhealthy for Sensitive Groups"
			category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			category_color = "usg"
		elif api['data']['aqi'] < 201:
			category = "Unhealthy"
			category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
			category_color = "unhealthy"
		elif api['data']['aqi'] < 301:
			category = "Very Unhealthy"
			category_description = "(201 - 300) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "veryunhealthy"
		else:
			category = "Hazardous"
			category_description = "(300+) Health alert: everyone may experience more serious health effects"
			category_color = "hazardous"


		return render(request, 'home.html', {
			'api' : api, 
			'category': category, 
			'category_description' : category_description, 
			'category_color': category_color,
			})

def about(request):
	return render(request, 'about.html', {})

