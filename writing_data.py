def write_data(g, d_g):
    with open("result.txt",'w', encoding='utf-8') as outfile:
        outfile.write("g ± ∆g = " + str(g) + "±" + str(d_g) + "\n")
