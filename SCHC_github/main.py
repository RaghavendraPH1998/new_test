# Main Function (Execution begins here)

print("Select Appropriate Rule ID:\n")
print("")
current_rule_id = input("01.IPv6\n02.UDP\n03.CoAP\nINPUT: ")

try:
    if current_rule_id == "01":
        header=get_header("68 01 00 00 31 02 02 FF 2A 01 3F 4D 9C 7E 11 14 56 19 DE A0 BD CD 17 FF CD DF 01 03 04 BC 2B 3A 4E 9D AB DE 9D AE 07 FF")
    elif current_rule_id =="02":
        #UDP CODE HERE
        print("NOT DEFINED")
    elif current_rule_id =="03":
        #CoAP CODE HERE
        print("NOT DEFINED")
except:
    print("ERR: INPUT VALUE DOESNT MATCH Rule-ID")
