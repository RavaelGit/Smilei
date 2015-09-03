# ----------------------------------------------------------------------------------------
# 					SIMULATION PARAMETERS FOR THE PIC-CODE SMILEI
# ----------------------------------------------------------------------------------------
#
# Remember: never override the following names:
#           SmileiComponent, Species, Laser, Collisions, DiagProbe, DiagParticles,
#           DiagScalar, DiagPhase or ExtField
#
import math

l0 = 2.0*math.pi		# laser wavelength
t0 = l0					# optical cicle
Lsim = [20.*l0,20.*l0]	# length of the simulation
Tsim = 10.*t0			# duration of the simulation
resx = 10.				# nb of cells in on laser wavelength
rest = 15.				# time of timestep in one optical cycle 

# dim: Geometry of the simulation
#      1d3v = cartesian grid with 1d in space + 3d in velocity
#      2d3v = cartesian grid with 2d in space + 3d in velocity
#      3d3v = cartesian grid with 3d in space + 3d in velocity
#      2drz = cylindrical (r,z) grid with 3d3v particles
#
dim = '2d3v'

# order of interpolation
#
interpolation_order = 2 

# SIMULATION BOX : for all space directions (use vector)
# cell_length: length of the cell
# sim_length: length of the simulation in units of the normalization wavelength 
#
cell_length = [l0/resx,l0/resx]
sim_length  = Lsim

# SIMULATION TIME
# timestep: duration of the timestep
# sim_time: duration of the simulation in units of the normalization period 
#
timestep = t0/rest
sim_time = Tsim
 
# ELECTROMAGNETIC BOUNDARY CONDITIONS
# bc_em_type_x/y/z : boundary conditions used for EM fields 
#                    periodic = periodic BC (using MPI topology)
#                    silver-muller = injecting/absorbing BC
#                    reflective = consider the ghost-cells as a perfect conductor
#
bc_em_type_x = ['silver-muller']
bc_em_type_y = ['silver-muller']

# RANDOM seed 
# this is used to randomize the random number generator
random_seed = 0

print_every = 1
# ---------------------
# DIAGNOSTIC PARAMETERS
# ---------------------

globalEvery = 1
    
Antenna(
field='Jz',
time_profile= lambda t: math.sin(2*t/t0),
space_profile=gaussian(1.0, xfwhm=l0, yfwhm=l0, xcenter=sim_length[0]*0.6, ycenter=sim_length[1]*0.6)
)

Antenna(
field='Jz',
time_profile= lambda t: -math.sin(2*t/t0),
space_profile=gaussian(1.0, xfwhm=l0, yfwhm=l0, xcenter=sim_length[0]*0.4, ycenter=sim_length[1]*0.4)
)

# DIAG ON SCALARS
# every = number of time-steps between each output
#
DiagScalar(every=globalEvery)

fieldDump_every = globalEvery
#fieldsToDump = ['Jz','Ex','Ey','Ez','Bx','By','Ez']

