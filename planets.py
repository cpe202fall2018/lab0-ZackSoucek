def weight_on_planets():
    weight = float(input("What do you weigh on earth? \n"))
    jupiterWeight = weight * 2.34
    marsWeight = weight * 0.38
    print("On Mars you would weigh", marsWeight ,"pounds.\nOn Jupiter you would weigh", jupiterWeight, "pounds.")


if __name__ == '__main__':
    weight_on_planets()
