var b='Shimla'
var city = document.getElementById('text_input')
const btn = document.getElementById('sbtn')
btn.addEventListener('click',function(e)
{	console.log("teh btn clk ed!")
	fetch('https://api.openweathermap.org/data/2.5/weather?q='+city.value+'&appid=ebdc273af541d30735dc7c4ac0407927')
		.then(response => response.json())

		.then(jsonData => {

			var tk=jsonData.main.temp
			var tc=tk-273.15

			document.getElementById("place").innerHTML = city.value
			document.getElementById("country_code").innerHTML = jsonData.sys.country

			document.getElementById("text_temp").innerHTML = tc.toFixed(2)

			document.getElementById("c_main").innerHTML = jsonData.weather[0].main
			document.getElementById("c_type").innerHTML = jsonData.weather[0].description

		})
		.catch(error => document.getElementById("place").innerHTML = "Place not found");
	})
