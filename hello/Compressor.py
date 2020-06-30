import Parser
from Rule_management import Rule_Manager
from Rule_management import Rules
from Rule_management import Matching_Operator
from CDA import CDA

class Compressor:
    def __init__(self,RuleID,Header_field_list,Payload,Header_fields):
        self.rule_id = RuleID # has to start from 01
        self.header_field_list= Header_field_list #list containing field parameters such as FID, FL,FP...
        self.payload = Payload # the actual payload data
        self.header_fields = Header_fields # A dictionary containing all the header field labels and their values
        
    def header_compression(self,ipv6_header):
        #the argument ipv6_header has to come from the parser
        #The rule manager has the lookup table that is used for comparison purposes by the matching operator
        rule_manager = Rule_Manager(self.header_field_list,self.rule_id)
        #This class has the list of rules. Each rule is simply a dictionary that contains tow lists, the matching operator and the CDA instructions
        rule_used = Rules(self.header_field_list)

        #rule methods
        #rule.rule_add(rule) can be used to add a distionary of MO and CDA values
        #rule.rule_delete(position) deleted a rule at the specified position
        #rule.rule_edit(rule,position) replaces a rule with a new one at the givem position

        #The rule has to be invoked in order to proceed to the matching operation
        
        rule_used.invoke_rule(self.header_field_list,self.rule_id)
        final_status = 1 # this variable is multiplied with the final status values obtained from the Matching Operator in each loop 
        #invoking the matching operator for every field of the header
        for i in range(len(rule_used.field)): # This loops through every field in the header and uses the corresponding matching operator to check for correctness
            if rule_used.mo[i] == 0:
                MO = Matching_Operator(rule_manager.look_up_table)
                MO.equal_operation(rule_used.field_parameters_list,rule_manager.look_up_table,rule_used.field[i])
                final_status = final_status*MO.final_status
            elif rule_used.mo[i] == 1:
                MO = Matching_Operator(rule_manager.look_up_table)
                MO.ignore_operation()
                final_status = final_status*MO.final_status
        self.final_status = int(final_status)
        #Checking the final_status value before proceeding for CDA 
        if (self.final_status == 1):
            cda = CDA(rule_used.cda,self.header_fields)
            cda.compression_action(self.header_fields)
            compressed_header = cda.compressed_header
        else:
            print('The Header does not satisfy all matching operations and is thus discarded')
            compressed_header = None

        
        print('Compressed Header\n')
        print(compressed_header)
        self.Payload=""

        for i in range(len(self.payload)):
            if self.payload[i] !=" ":
                self.Payload +=self.payload[i] 
                

        self.compressed_header = compressed_header
        #the final form of the compressed SCHC message
        self.schc_message =  "0"+ str(self.rule_id) + str(self.compressed_header) +str(Payload)

        
        
            
            
    
