import os
def read_com():
        while(True):
                input_string=input(">>>")
                commands=input_string.split(";") 
                for comms in commands:
                        comms=comms.strip()
                        elem=comms.split()
                        comm_desc=elem[0].split("_")
                        comm=comm_desc[0].strip()
                        try:
                            desc=comm_desc[1].strip()
                        except:
                            desc=[]
                        args=elem[1:]
                        args.append("")
                        #print(args)
                        match comm:
                                case "exit":
                                        break
                                case "clearc":
                                        os.system("cls")
                                case _:
                                        print("Function error")
                                        print("Command:",comm,"\nDescriptor:",desc,"\nArgs:",args)
os.system("cls")
read_com()