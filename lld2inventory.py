import pandas as pd
import yaml, xlrd

def main():
    my_dict = pd.read_excel("LLD.xlsx", sheet_name="VM").to_dict('index')
    yaml_dict = { "all": { "children" : {}} }
    for i, j in my_dict.items():
        print("i: ", i, "    j: ", type(j))
        #SÍK hozzáadása,ha még nem volt
        if j["Sík"] not in yaml_dict["all"]["children"]:
            yaml_dict["all"]["children"].update({ j["Sík"] : { "hosts" : {} } })

        #VM hozzáadása, ha még nincs
        if j["VM neve"] not in yaml_dict["all"]["children"][j["Sík"]]["hosts"]:
            yaml_dict["all"]["children"][j["Sík"]]["hosts"].update({ j["VM neve"] : {} })

        #paraméterek hozzáadás dinamikusan
        if i not in yaml_dict["all"]["children"][j["Sík"]]["hosts"][j["VM neve"]]:
            yaml_dict["all"]["children"][j["Sík"]]["hosts"][j["VM neve"]] = j

        #custom paraméterek hozzáadása
        if "ansible_host" not in yaml_dict["all"]["children"][j["Sík"]]["hosts"][j["VM neve"]]:
            yaml_dict["all"]["children"][j["Sík"]]["hosts"][j["VM neve"]]["ansible_host"] = j["IP cím"]
        if "netmask_cidr" not in yaml_dict["all"]["children"][j["Sík"]]["hosts"][j["VM neve"]]:
            yaml_dict["all"]["children"][j["Sík"]]["hosts"][j["VM neve"]]["netmask_cidr"] = j["Netmask"][1:]

        for k, l in j.items():
            pass
#            print("kulcs: ", k, "    érték: ", l)
    print(yaml.dump(yaml_dict))


if __name__ == '__main__':
    main()