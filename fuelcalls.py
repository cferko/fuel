'''
Fuel module helper code
'''

def fuelStudy1(r1_mass,r2_mass,o2_mass,n2_mass):

	import matplotlib.pyplot as plt

	r1_molmass = 182.7 # g/mol
	r2_molmass = 152.57
	o2_molmass = 32.
	n2_molmass = 28.02
	h2o_molmass = 18.02
	h2_molmass = 2.02

	# get moles of reactants:
	mol_r1 = r1_mass/r1_molmass
	mol_r2 = r2_mass/r2_molmass
	mol_o2 = o2_mass/o2_molmass
	mol_n2 = n2_mass/n2_molmass

	# rxn 1:
	rxn_r1 = mol_r1 / 6.5
	# rxn_r2 = mol_r2 / 3.
	rxn_o2 = mol_o2 / 7.
	rxn_n2 = mol_n2 / 26.

	lim = min(rxn_r1, rxn_n2, rxn_o2) # the limiting reactant determines the amount of product

	product_mol_p1 = lim * 13.
	p1_molmass = product_mol_p1 * 140.31 # g / mol

	# rxn 2:

	rxn_r2 = mol_r2 / 3.
	rxn_o2 = mol_o2 / 5.
	rxn_n2 = mol_n2 / 10.

	lim = min(rxn_r2, rxn_n2, rxn_o2)
	
	product_mol_p2 = lim * 5.
	p2_molmass = product_mol_p2 * 140.31 # g / mol	

	fig = plt.figure(figsize = (12,8))

	plt.plot([p1_molmass, p1_molmass], [0.,1.], lw = 5, label = 'Reaction 1 Si3N4 Mass')
	plt.plot([p2_molmass, p2_molmass], [0.,1.], lw = 5, label = 'Reaction 2 Si3N4 Mass')
	plt.legend()
	plt.xlim([0,1600])
	plt.xlabel('Mass (grams) of Si3N4 Product')

	plt.show()

	return

def fuelStudy2(catalyst_a, catalyst_b):

	import numpy as np 
	import matplotlib.pyplot as plt

	speed = np.linspace(0,1,num=100)
	y = []
	y2 = []
	y3 = []
	avec = []
	bvec = []

	for s in range(len(speed)):

		a_opt = -7.1*speed[s]**2 + 4.1*speed[s] + 0.1
		b_opt = 0.83*speed[s]**2 + 0.27*speed[s] + 0.26
		if a_opt > 1.:
			a_opt = 2. - a_opt
		if a_opt < 0.:
			a_opt = 0.
		if b_opt > 1.:
			b_opt = 2. - b_opt
		if b_opt < 0.:
			b_opt = 0

		avec.append(a_opt)
		bvec.append(b_opt)
		y.append(1.-abs(catalyst_a-a_opt))
		y2.append(1.-abs(catalyst_b-b_opt))
		y3.append(3.-abs(catalyst_a-a_opt)-abs(catalyst_b-b_opt))
	fig = plt.figure(figsize = (12,8))

	# plt.plot( speed, y, lw = 5 )
	# plt.plot( speed, y2, lw = 5 )
	plt.plot( speed, y3, lw = 5)
	# plt.plot( speed, avec)
	# plt.plot( speed, bvec)
	plt.grid()
	plt.xlabel('speed (as fraction of speed of light)')
	plt.ylabel('energy released (Mega Joules)')
	plt.ylim([0,3.5])
	plt.show()

	return

def fuelStudy3(aperture_size,cruise_speed,fuel_capacity):

	import numpy as np 
	import matplotlib.pyplot as plt

	weight =  (0.001*fuel_capacity) + aperture_size
	cost = max(0,(6000*cruise_speed) + fuel_capacity) # - (1500.*aperture_size)**0.55)
	refuel_distance = max(0,50+ 0.01*fuel_capacity - (20*cruise_speed) - (10*aperture_size))


	fig = plt.figure(figsize=(18,8))

	ax1 = fig.add_subplot(131)
	ax1.plot( [1,1], [0,weight], lw = 50 ) 
	plt.ylabel('WEIGHT (megagrams)')
	plt.grid()
	plt.ylim([0,12])

	ax2 = fig.add_subplot(132)
	ax2.plot([1,1], [0,cost],  lw = 50 )
	plt.ylabel('COST (Andromeda Credits)')
	plt.ylim([0,12000])
	plt.grid()


	ax3 = fig.add_subplot(133)
	ax3.plot([1,1], [0,refuel_distance], lw = 50 )
	plt.ylabel('REFUEL DISTANCE (light years)')
	plt.ylim([0,150])
	plt.grid()

	plt.show()

	return
