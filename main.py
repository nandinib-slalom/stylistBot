

from weather import get_weather
from stylist import suggest_outfit


def main():
	weather = get_weather()
	outfit = suggest_outfit(weather)
	print(f"Weather: {weather}")
	print("Suggested outfit:")
	for item, suggestion in outfit.items():
		print(f"  {item.capitalize()}: {suggestion}")

if __name__ == "__main__":
	main()