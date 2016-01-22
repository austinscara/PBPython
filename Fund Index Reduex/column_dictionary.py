def column_dic():
	## this functions's only purpose is to serve as an interpreter for the raw data coming from the csv
	## this will be refernced often as a way to index through lists by simply naming the value you want to index it

	return{'Report Date': 0,  ##
			'Report YYYY': 1, ##
			'Report Q': 2, ##
			'Report YYYYQ': 3, ##
			'Close to Report Q': 4, ##
			'Close to Report Y': 5, ##
			'Fund ID': 6, ##
			'Fund Name': 7,
			'Fund Type': 8,
			'Investor Name': 9, ##
			'Fund Close Date': 10, ##
			'Fund Close YYYY': 11, ##
			'Fund Close Q': 12, ##
			'Fund Region': 13,
			'LP beID': 14, ##
			'LP Name': 15, ##
			'Fund-LP Unique ID': 16, ##
			'Return NAV': 17, ##
			'Return Contributed': 18, ##
			'Return Distributed': 19, ##
			'Fund Initial Amount': 20,  ##
			'Consistency': 21,
			'Committed': 22,
			'Liquidated Percent': 23,
			'Liquidated': 24,
			'Cash Weight':25,
			'Net Flows': 26}
