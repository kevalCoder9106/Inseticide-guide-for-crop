import pandas

data = pandas.read_csv("data.csv")

def get_all_crops_insectiside():
    index = 0
    insectiside = []

    while True:
        try:
            if data.iloc[index]['crop'] == "all":
                i = data.iloc[index]['i']
                insectiside.append(str(i).split(">>"))

            index = index + 1
        except:
            break

    return insectiside

def get_insectiside(crop_name):
    index = 0

    while True:
        try:
            if crop_name == data.iloc[index]['crop']:
                insectiside = data.iloc[index]['i']
                insectiside = str(insectiside).split(">>")
                return insectiside

            index = index + 1
        except:
            break

    return 0

if __name__ == "__main__":
    all_insectised = get_all_crops_insectiside()

    crop_name = input("Enter crop name: ")

    insectiside = get_insectiside(crop_name)
    all_insectised.append(insectiside)
    
    if insectiside != 0:
        print("\nInsectiside data: \n")
        for x in all_insectised:
            for y in x:
                print(f"{y}\n")
            
            print("\n")

