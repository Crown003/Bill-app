def bill(a,b,c):
	"""
	hi! this is a bill creater module..
	it contain only one function
	> bill()
	bill requries 3 parameters.
	bill(<quantity of product>,<price of product>,<discount on product>)
	"""
	amount_with_quantity = int(b)*int(a)
	calculating_discount = amount_with_quantity*int(c)/100
	total_amount = amount_with_quantity - calculating_discount
	t = total_amount
	return t