// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table internal header
//
// Internal details; most calling programs do not need this header,
// unless using verilator public meta comments.

#ifndef _VSYSTOLIC_ARRAY__SYMS_H_
#define _VSYSTOLIC_ARRAY__SYMS_H_  // guard

#include "verilated_heavy.h"

// INCLUDE MODULE CLASSES
#include "Vsystolic_array.h"

// SYMS CLASS
class Vsystolic_array__Syms : public VerilatedSyms {
  public:
    
    // LOCAL STATE
    const char* __Vm_namep;
    bool __Vm_didInit;
    
    // SUBCELL STATE
    Vsystolic_array*               TOPp;
    
    // CREATORS
    Vsystolic_array__Syms(Vsystolic_array* topp, const char* namep);
    ~Vsystolic_array__Syms() {}
    
    // METHODS
    inline const char* name() { return __Vm_namep; }
    
} VL_ATTR_ALIGNED(VL_CACHE_LINE_BYTES);

#endif  // guard
