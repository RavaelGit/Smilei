#ifndef PROJECTOR_H
#define PROJECTOR_H

#include <complex>

#include "Params.h"
#include "Field.h"

class PicParams;
class Patch;

class ElectroMagn;
class Field;
class Particles;


//----------------------------------------------------------------------------------------------------------------------
//! class Projector: contains the virtual operators used during the current projection
//----------------------------------------------------------------------------------------------------------------------
class Projector
{

public:
    //! Creator for the Projector
    Projector( Params &, Patch * );
    virtual ~Projector() {};
    virtual void mv_win( unsigned int shift ) = 0;
    virtual void setMvWinLimits( unsigned int shift ) = 0;
    
    //! Project global current charge (EMfields->rho_ , J), for initialization and diags
    virtual void densityFrozen( double               *rhoj, Particles &particles, unsigned int ipart, unsigned int type ) {};
    virtual void densityFrozenComplex( std::complex<double> *rhoj, Particles &particles, unsigned int ipart, unsigned int type, int imode ) {};
    
    //! Project global current densities if Ionization in Species::dynamics,
    virtual void ionizationCurrents( Field *Jx, Field *Jy, Field *Jz, Particles &particles, int ipart, LocalFields Jion ) = 0;
    
    //!Wrapper
    virtual void currentsAndDensityWrapper( ElectroMagn *EMfields, Particles &particles, SmileiMPI *smpi, int istart, int iend, int ithread, int ibin, int clrw, bool diag_flag, bool is_spectral, std::vector<unsigned int> &b_dim, int ispec, int ipart_ref = 0 ) = 0;
    
    
    virtual void susceptibility( ElectroMagn *EMfields, Particles &particles, double species_mass, SmileiMPI *smpi, int istart, int iend,  int ithread, int ibin, int ipart_ref = 0 )
    {
        ERROR( "Envelope not implemented with this geometry and this order" );
    };
    
protected:
    double inv_cell_volume;
};

#endif

