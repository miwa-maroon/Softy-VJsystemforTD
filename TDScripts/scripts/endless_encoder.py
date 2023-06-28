# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	encoder_name = channel.name
	op_index = op(encoder_name)
	page = op_index.par.value0
	sub_index = op_index.par.value1
	index = op_index.par.value2

	print(index)
	
	# inclusive
	grid_divisions = 5
	threshold = 0.15
	# grid divisions TODO: make grid boundaries dynamic

	sub = "up" if val > prev else "down"
	# prevent negatives
	if sub == "down" and index == 0:
		sub_index.val = 0
		return
	if val >= 0 and val < 0.2:
		sub_index.val = 0
	elif val >= 0.2 and val < 0.4:
		sub_index.val = 1
	elif val >= 0.4 and val < 0.6:
		sub_index.val = 2
	elif val >= 0.6 and val < 0.8:
		sub_index.val = 3
	else:
		sub_index.val = 4
	

	# wraparounds
	# upwards
	if val >= 0 and val <= threshold and prev <= 1 and prev >= (1-threshold):
		print('------up------')
		page.val +=1
	
	# downwards
	elif prev >= 0 and prev <= threshold and val <= 1 and val >= (1 - threshold):
		print('------down-----')
		if index <= 0:
			print('>>>> STOPPING <<<<')
			# cant go negative
			return 
		page.val -=1
	
	index.val = page.val * grid_divisions + sub_index.val
	
	return
	