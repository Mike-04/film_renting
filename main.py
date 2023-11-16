import os
import service as s
import presentation as ui
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
                    case "add":
                        match desc:
                            case "c":
                                s.add_client(args[0],args[1])
                            case "m":
                                s.add_movie(args[0],args[1],args[2])
                            case _:
                                print("Invalid descriptor!")
                    case "src":
                        prop={'property':args[0],'value':args[1]}
                        match desc:
                            case "c":
                                ids=s.search_client(prop)
                                ui.print_clients(ids)
                            case "m":
                                ids=s.search_movie(prop)
                                ui.print_movies(ids)
                            case _:
                                print("Invalid descriptor!")
                    case "del":
                        prop={'property':args[0],'value':args[1]}
                        match desc:
                            case "c":
                                ids=s.search_client(prop)
                                print("Folowing entries will be deleted:")
                                ui.print_clients(ids)
                                if(ui.get_confirm()):
                                    s.del_client(ids)
                            case "m":
                                ids=s.search_movie(prop)
                                print("Folowing entries will be deleted:")
                                ui.print_movies(ids)
                                if(ui.get_confirm()):
                                    s.del_movie(ids)
                            case _:
                                print("Invalid descriptor!")
                    case "view":
                        ids=[-1]
                        match desc:
                            case "c":
                                ui.print_clients(ids)
                            case "m":
                                ui.print_movies(ids)
                            case _:
                                print("Invalid descriptor!")
                    case "save":
                        ui.save()
                    case "load":
                        ui.load()
                    case "exit":
                        break
                    case "clearc":
                        os.system("cls")
                    case _:
                        print("Function error")
                        print("Command:",comm,"\nDescriptor:",desc,"\nArgs:",args)
ui.load()
os.system("cls")
read_com()