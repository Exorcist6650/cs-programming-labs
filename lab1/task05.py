def main():
	distance_km, fuel_consumption_100km, fuel_price_1km = (
		float(input()), 
		float(input()), 
		float(input())
	)

	required_fuel = fuel_consumption_100km / 100 * distance_km
	required_price = required_fuel * fuel_price_1km

	print(f'Топливо: {required_fuel:.2f} л\n'
	   f'Стоимость: {required_price:.2f} руб')

if __name__ == "__main__":
	main()