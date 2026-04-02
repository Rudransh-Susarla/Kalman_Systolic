// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Primary design header
//
// This header should be included by all source files instantiating the design.
// The class here is then constructed to instantiate the design.
// See the Verilator manual for examples.

#ifndef _VSYSTOLIC_ARRAY_H_
#define _VSYSTOLIC_ARRAY_H_  // guard

#include "verilated_heavy.h"

//==========

class Vsystolic_array__Syms;

//----------

VL_MODULE(Vsystolic_array) {
  public:
    
    // LOCAL SIGNALS
    // Internals; generally not touched by application code
    CData/*0:0*/ systolic_array__DOT__clk;
    CData/*0:0*/ systolic_array__DOT__reset;
    IData/*31:0*/ systolic_array__DOT__file;
    IData/*31:0*/ systolic_array__DOT__outfile;
    double systolic_array__DOT__PE00__DOT__accumulator;
    double systolic_array__DOT__PE01__DOT__accumulator;
    double systolic_array__DOT__PE02__DOT__accumulator;
    double systolic_array__DOT__PE03__DOT__accumulator;
    double systolic_array__DOT__PE10__DOT__accumulator;
    double systolic_array__DOT__PE11__DOT__accumulator;
    double systolic_array__DOT__PE12__DOT__accumulator;
    double systolic_array__DOT__PE13__DOT__accumulator;
    double systolic_array__DOT__PE20__DOT__accumulator;
    double systolic_array__DOT__PE21__DOT__accumulator;
    double systolic_array__DOT__PE22__DOT__accumulator;
    double systolic_array__DOT__PE23__DOT__accumulator;
    double systolic_array__DOT__PE30__DOT__accumulator;
    double systolic_array__DOT__PE31__DOT__accumulator;
    double systolic_array__DOT__PE32__DOT__accumulator;
    double systolic_array__DOT__PE33__DOT__accumulator;
    double systolic_array__DOT__A[4][4];
    double systolic_array__DOT__B[4][4];
    
    // LOCAL VARIABLES
    // Internals; generally not touched by application code
    CData/*0:0*/ __VinpClk__TOP__systolic_array__DOT__clk;
    CData/*0:0*/ __Vclklast__TOP____VinpClk__TOP__systolic_array__DOT__clk;
    CData/*0:0*/ __Vchglast__TOP__systolic_array__DOT__clk;
    
    // INTERNAL VARIABLES
    // Internals; generally not touched by application code
    Vsystolic_array__Syms* __VlSymsp;  // Symbol table
    
    // CONSTRUCTORS
  private:
    VL_UNCOPYABLE(Vsystolic_array);  ///< Copying not allowed
  public:
    /// Construct the model; called by application code
    /// The special name  may be used to make a wrapper with a
    /// single model invisible with respect to DPI scope names.
    Vsystolic_array(const char* name = "TOP");
    /// Destroy the model; called (often implicitly) by application code
    ~Vsystolic_array();
    
    // API METHODS
    /// Evaluate the model.  Application must call when inputs change.
    void eval() { eval_step(); }
    /// Evaluate when calling multiple units/models per time step.
    void eval_step();
    /// Evaluate at end of a timestep for tracing, when using eval_step().
    /// Application must call after all eval() and before time changes.
    void eval_end_step() {}
    /// Simulation complete, run final blocks.  Application must call on completion.
    void final();
    
    // INTERNAL METHODS
  private:
    static void _eval_initial_loop(Vsystolic_array__Syms* __restrict vlSymsp);
  public:
    void __Vconfigure(Vsystolic_array__Syms* symsp, bool first);
  private:
    static QData _change_request(Vsystolic_array__Syms* __restrict vlSymsp);
    static QData _change_request_1(Vsystolic_array__Syms* __restrict vlSymsp);
    void _ctor_var_reset() VL_ATTR_COLD;
  public:
    static void _eval(Vsystolic_array__Syms* __restrict vlSymsp);
  private:
#ifdef VL_DEBUG
    void _eval_debug_assertions();
#endif  // VL_DEBUG
  public:
    static void _eval_initial(Vsystolic_array__Syms* __restrict vlSymsp) VL_ATTR_COLD;
    static void _eval_settle(Vsystolic_array__Syms* __restrict vlSymsp) VL_ATTR_COLD;
    static void _initial__TOP__2(Vsystolic_array__Syms* __restrict vlSymsp) VL_ATTR_COLD;
    static void _sequent__TOP__1(Vsystolic_array__Syms* __restrict vlSymsp);
} VL_ATTR_ALIGNED(VL_CACHE_LINE_BYTES);

//----------


#endif  // guard
