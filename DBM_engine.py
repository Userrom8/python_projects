# max number of companies :
n = 6

# database :

IDs = ["none" for i in range (n)]
names = ["none" for i in range (n)]
capacity = ["none" for i in range (n)]
share = ["none" for i in range (n)]
revenue = ["none" for i in range (n)]
data_Base = {"CompanyID" : IDs, "CompanyName" : names, "Capacity" : capacity, "MarketShare" : share, "Revenue" : revenue}

# dev_utility functions :

def add():
	add_index = -1
	add_ID = str(input("\nEnter ID : "))
	if add_ID == "none":
		print("\nPlease enter valid ID !\n")
		return
	for i in range(n):
		if IDs[i] == add_ID :
			print("\nID already in database !")
			return 0
		if IDs[i] == "none":
			add_index = i
			break
	if add_index == -1:
		print("\nDatabase full ! no more titles can be added.\n")
		return 0
	IDs[add_index] = add_ID
	names[add_index] = str(input("\nEnter company name : "))
	return 1

def update():
	index = -1
	idn = str(input("\nPlease enter the company ID to modify the data : "))
	if idn == "none":
		print("\nPlease enter valid ID !\n")
		return
	for i in range(n):
		if IDs[i] == idn:
			index = i
	if index == -1:
		print("\nNo matches found !\nPlease check the ID or add it first.\n")
		return 0
	attr = str(input("\nPlease enter the attribute to modify :\nName(1)\nProduction capacity(2)\nMarket share(3)\nRevenue(4)\n_"))
	val = str(input("\nEnter data : "))
	match attr:
		case "1" :
			names[index] = val
		case "2" :
			try:
				capacity[index] = float(val)
			except:
				print("\nPlase check input !\n(production capacity must be in integer format)")
				return 0
		case "3" :
			try :
			    if float(val) > 100:
				    print("\nMarket share can not be more than 100% !\n")
				    return
			    share[index] = float(val)
			except:
				print("\nPlase check input !\n(market share must be in integer format)")
				return 0
		case "4" :
			try:
				revenue[index] = float(val)
			except:
				print("\nPlase check input !\n(revenue must be in integer format)\n")
				return 0
		case _:
			print("Invalid input !")
			return 0
	return 1

def delete():
	del_index = -1
	cn = str(input("\nEnter the company ID to remove : "))
	if cn == "none":
		print("\nPlease enter valid ID !\n")
		return
	for i in range (n):
		if IDs[i] == cn:
			del_index = i
	if del_index == -1:
		print("\nNo such IDs found !\n")
		return 0
	confirmation = str(input(F"\nAre you sure to delete \'{names[del_index]}\' and, all it's attributes ?\n\nPress 1 to confirm\nPress 0 to exit_"))
	match confirmation :
		case "1":
			IDs[del_index] = "none"
			names[del_index] = "none"
			capacity[del_index] = "none"
			share[del_index] = "none"
			revenue[del_index] = "none"
		case "0":
			return 0
		case _:
			print("\nInvalid input !")
	return 1

def table_print(dict):
		print("\n")
		print("{:<10}\t ".format("attributes"), end = " ")
		for i in range (n):
			print("{:<10}\t ".format(F"company_{i+1}"), end = " ")
		print("\n")
		for k, v in dict.items():
			print("{:<10}\t ".format(k), end = " ")
			for j in range (n):
				print("{:<10}\t ". format(v[j]), end = " ")
			print("\n")
		print("\n")
		
def showInfo():
    infoin = str(input("\nEnter company name or ID : "))
    showtemp = -1
    for i in range(n):
    	if IDs[i] == infoin or names[i] == infoin:
    		showtemp = i
    		break
    if showtemp == -1 or IDs[showtemp] == "none":
    	print("\nNo match found !\n(please check the input)\n")
    	return
    print("\nEnter attribute to display :\n")
    l = []
    for i in data_Base:
    	l.append(i)
    for i in range(2, 5):
    	print(F"Press {i-1} to display {l[i]} of {names[showtemp]}")
    sic = int(input("_"))
    try :
    	print(F"\nID : {IDs[showtemp]}\tName : {names[showtemp]}\t{l[sic+1]} : {data_Base[l[sic+1]][showtemp]}", end = " ")
    	if data_Base[l[sic+1]][showtemp] == "none":
    		print("\n")
    		return
    	match sic:
    		case 1:
    			print("units\n")
    		case 2:
    			print("%\n")
    		case 3:
    			print("Rupees\n")
    except :
    	print("\nPlease check the values\n")
		
# user utility tools :
	
def bulk_entry(dict):
	for i in range(n):
		if IDs[i] == "none":
			run = str(input("Press 0 to exit\nPress 1 to continue\n_"))
			try:
				if not int(run):
					return
			except:
				print("\nPlease enter 0 or 1\n")
				return
			IDs[i] = str(input("Enter ID : "))
			names[i] = str(input("Enter Name : "))
			try:
				capacity[i] = float(input(F"Enter Production capacity of {names[i]} : "))
			except:
				print("\nPlease check the values !\n")
			try:
				ms_temp = float(input(F"Enter Market share of {names[i]} : "))
				if ms_temp <= 100:
					share[i] = ms_temp
				else:
					print("\nInvalid market share !\n")
			except:
				print("\nPlease check the values !\n")
			try:
				revenue[i] = float(input(F"Enter revenue of {names[i]} : "))
			except:
				print("\nPlease check the values !\n")
	print("\nDatabase is full !\n")
	
def total_titles():
	ccount = 0
	tlist = []
	for i in range(n):
		if IDs[i] != "none":
			tlist.append(names[i])
			ccount += 1
	if not ccount:
		print("\nDatabase is empty !\n")
		return
	print(F"\nTotal number of companies in database : {ccount}\n")
	for j in range (len(tlist)):
		print(F"{j+1}. tlist[j]")
	print("\n")
	
def total_avg_revenue(switch):
	rsum = 0
	rcount = 0
	for i in revenue:
		if i != "none":
			rsum += i
			rcount += 1
	if not rcount:
		print("\nNo data on revenues in database !\n")
		return
	if switch == 1:
		print(F"\nTotal revenue generated by all the companies combined : {rsum} Rupees.\n")
		return
	print(F"\nAverage revenue : {rsum/rcount} Rupees.\n")
		
def avg_productionCapacity(pcswitch):
	pcsum = 0
	pccount = 0
	for i in capacity:
		if i != "none":
			pcsum += i
			pccount += 1
	if pcswitch:
		if not pccount:
			return 0
		return pcsum/pccount
	if not pccount:
		print("\nNo data on production capacities in database !\n")
		return
	print(F"\nAverage Production Capacity : {pcsum/pccount} units\n")
	
def greater_pc():
	variable = avg_productionCapacity(1)
	newl = []
	if not variable:
		print("\nNot enough data !\n")
		return
	for i in range(n):
		if capacity[i] != "none" and capacity[i] > variable:
			newl.append(i)
	print("\nList of companies with production capacity higher than average :")
	for k in newl:
		print(F"{names[k]} : {capacity[k]}")
	print("\n")
	
def market_dom():
		mssum = 0
		mscount = 0
		max = 0
		maxi = 0
		for i in range(n):
			if share[i] != "none":
				mssum += share[i]
				mscount += 1
				if share[i] > max:
					max = share[i]
					maxi = i
		if not mscount:
			print("\nNo data on market share in database !\n")
			return
		print(F"\n{names[maxi]}({max}%) has the highest market share.\nTotal market share held by {names[maxi]} on total market share by all companies combined is {max/mssum*100}%\n")
		
def pc_specific_range(pin1, pin2):
		if pin1>pin2:
			in1 = pin2
			in2 = pin1
		else:
			in1 = pin1
			in2 = pin2
		pcsrl = []
		for i in range(n):
			if capacity[i] != "none":
				if capacity[i] >= in1 and capacity[i] <= in2:
					pcsrl.append(i)
		if len(pcsrl) == 0:
			print("\nNo companies found !\n")
			return
		print(F"\nList of companies with production capacities between {in1} and {in2} :\n")
		for i in pcsrl:
			print(F"{names[i]}({capacity[i]} units)")
		print("\n")
		
def highest_rev_cap():
		res = 0
		hrct = -1
		for i in range(n):
			if revenue[i] != "none" and capacity[i] != "none":
				restemp = revenue[i]/capacity[i]
				if restemp>res:
					res = restemp
					hrct = i
		if hrct == -1:
			print("\nNot enough data !\n")
			return
		print(F"\n{names[hrct]} has the highest revenue per unit of production capacity : {res:.2f} Rupees/unit\n")
		
def avg_rev_cap():
		avgressum = 0
		avgRevCapCount = 0
		for i in range(n):
			if revenue[i] != "none" and capacity[i] != "none":
				avgressum += revenue[i]/capacity[i]
				avgRevCapCount += 1
		if not avgRevCapCount:
			print("\nNot enough data !\n")
			return
		print(F"\nAverage revenue per unit of production capacity : {avgressum/avgRevCapCount:.2f} Rupees/unit\n")
		
# driver code :

iter = 1
while iter :
	main_input = str(input("Press 1 to update the database\nPress 2 to show company details\nPress 3 to print the entire database\nPress 4 to use utility tools\nPress 0 to exit\n_"))
	match main_input:
		case "0":
			iter = 0
		case "1":
			updateCaseInput = str(input("\nPress 1 to add a company\nPress 2 to update the attributes\nPress 3 to remove a company\n_"))
			match updateCaseInput :
				case "1" :
					temp1 = add()
					if temp1:
						print("\nTitle added succsessfully !\n")
				case "2" :
					temp2 = update()
					if temp2 :
						print("\ndatabase updated succsessfully !\n")
				case "3" :
					temp3 = delete()
					if temp3:
						print("\nTitle removed succsessfully !\n")
				case _:
					print("\nPlease check the input !\n")
		case "2":
			showInfo()
		case "3":
			table_print(data_Base)
		case "4":
			utilt = str(input("\nPress 1 for bulk entry\nPress 2 to display quick access panel\n_"))
			match utilt:
				case "1":
					bulk_entry(data_Base)
				case "2":
					qc = str(input("\nPress 1 to list all the companies\nPress 2 to display total revenue\nPress 3 to display average revenue\nPress 4 to display average production capacity\nPress 5 to display companies with higher than average production capacity\nPress 6 to display heighst market share\nPress 7 to list production capacities between custom range\nPress 8 to display revenue per unit production capacity\n_"))
					match qc:
						case "1":
							total_titles()
						case "2":
							total_avg_revenue(1)
						case "3":
							total_avg_revenue(2)
						case "4":
							avg_productionCapacity(0)
						case "5":
							greater_pc()
						case "6":
							market_dom()
						case "7":
							try:
								in1 = float(input("\nEnter starting range : "))
								in2 = float(input("Enter ending range : "))
								pc_specific_range(in1, in2)
							except:
								print("\nPlease check the input !\n")
						case "8":
							print("\nHighest :")
							highest_rev_cap()
							print("\nAverage :")
							avg_rev_cap()
						case _:
							print("\nPlease check the input !\n")
				case _:
					print("\nPlease check the input !\n")
		case _:
			print("\nPlease check the input !\n")