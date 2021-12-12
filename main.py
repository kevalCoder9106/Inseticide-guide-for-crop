import pandas

data = pandas.read_csv("data.csv")

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
    crop_name = input("Enter crop name: ")

    insectiside = get_insectiside(crop_name)
    
    if insectiside != 0:
        print("\nInsectiside data: \n")
        for data in insectiside:
            print(f"{data}\n")
        
        print("\n")
    else:
        print ("Data not found...")


