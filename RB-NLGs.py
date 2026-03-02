# simple weather report generation through rule based NLG

class WeatherReportGenerator:
    def __init__(self, data):
        self.data = data 
        
    def generate_report(self):
        report =[]

        # content determination 
        temp_sentence = self._generate_temperature_sentence(self.data['temperature'])
        humidity_sentence = f"The humidity is {self.data['humidity']}%."
        wind_sentence = self._generate_wind_sentence(self.data['wind_speed'])

        # document planning
        report.append(temp_sentence)
        report.append(humidity_sentence)
        report.append(wind_sentence)

        return " ".join(report)
    
    def _generate_temperature_sentence(self, temperature):
        if temperature> 35:
            return "It's an extremely hot day."
        elif temperature > 30:
            return "It's a hot day."
        elif temperature > 20:
            return "The weather is warm."
        elif temperature > 10 :
            return "It's a cool day."
        else:
            return "It's a cold day"
        
    def _generate_wind_sentence(self, wind_speed):
        if wind_speed > 25:
            return "It's very windy today."
        elif wind_speed > 15:
            return "There's a strong breeze."
        elif wind_speed > 5:
            return "There's a gentle breeze."
        else:
            return "The wind is calm."
        
example_date = {
    'temperature' : 28,
    'humidity' : 65,
    'wind_speed' : 15
}

generator = WeatherReportGenerator(example_date)
print(generator.generate_report())