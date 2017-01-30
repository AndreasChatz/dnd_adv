import items, tiles


def main():
	gold = items.Gold(4)
	print(gold)
	dagger = items.Dagger()
	print(dagger)
	first = tiles.StartingRoom(1,2)
	print(first.intro_text())



if __name__ == "__main__":
	main()