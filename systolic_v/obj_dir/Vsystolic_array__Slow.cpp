// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vsystolic_array.h for the primary calling header

#include "Vsystolic_array.h"
#include "Vsystolic_array__Syms.h"

//==========

VL_CTOR_IMP(Vsystolic_array) {
    Vsystolic_array__Syms* __restrict vlSymsp = __VlSymsp = new Vsystolic_array__Syms(this, name());
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Reset internal values
    
    // Reset structure values
    _ctor_var_reset();
}

void Vsystolic_array::__Vconfigure(Vsystolic_array__Syms* vlSymsp, bool first) {
    if (false && first) {}  // Prevent unused
    this->__VlSymsp = vlSymsp;
    if (false && this->__VlSymsp) {}  // Prevent unused
    Verilated::timeunit(-12);
    Verilated::timeprecision(-12);
}

Vsystolic_array::~Vsystolic_array() {
    VL_DO_CLEAR(delete __VlSymsp, __VlSymsp = NULL);
}

void Vsystolic_array::_initial__TOP__2(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_initial__TOP__2\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Variables
    WData/*95:0*/ __Vtemp17[3];
    WData/*95:0*/ __Vtemp18[3];
    // Body
    vlTOPp->systolic_array__DOT__clk = 0U;
    vlTOPp->systolic_array__DOT__reset = 0U;
    __Vtemp17[0U] = 0x2e747874U;
    __Vtemp17[1U] = 0x6e707574U;
    __Vtemp17[2U] = 0x69U;
    vlTOPp->systolic_array__DOT__file = VL_FOPEN_NN(
                                                    VL_CVT_PACK_STR_NW(3, __Vtemp17)
                                                    , 
                                                    std::string("r"));
    (void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                       64,&(vlTOPp->systolic_array__DOT__A
                            [0U][0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                           64,
                                                           &(vlTOPp->systolic_array__DOT__A
                                                             [0U]
                                                             [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [0U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [0U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [1U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [1U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [1U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [1U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [2U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [2U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [2U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [2U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [3U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [3U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [3U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__A
                                                                                [3U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [0U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [0U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [0U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [0U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [1U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [1U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [1U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [1U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [2U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [2U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [2U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [2U]
                                                                                [3U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [3U]
                                                                                [0U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [3U]
                                                                                [1U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [3U]
                                                                                [2U])) ;(void)VL_FSCANF_IX(vlTOPp->systolic_array__DOT__file,"%f",
                                                                                64,
                                                                                &(vlTOPp->systolic_array__DOT__B
                                                                                [3U]
                                                                                [3U])) ;VL_FCLOSE_I(vlTOPp->systolic_array__DOT__file); vlTOPp->systolic_array__DOT__file = 0;
    __Vtemp18[0U] = 0x2e747874U;
    __Vtemp18[1U] = 0x74707574U;
    __Vtemp18[2U] = 0x6f75U;
    vlTOPp->systolic_array__DOT__outfile = VL_FOPEN_NN(
                                                       VL_CVT_PACK_STR_NW(3, __Vtemp18)
                                                       , 
                                                       std::string("w"));
    VL_FWRITEF(vlTOPp->systolic_array__DOT__outfile,"%f %f %f %f\n",
               64,vlTOPp->systolic_array__DOT__PE00__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE01__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE02__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE03__DOT__accumulator);
    VL_FWRITEF(vlTOPp->systolic_array__DOT__outfile,"%f %f %f %f\n",
               64,vlTOPp->systolic_array__DOT__PE10__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE11__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE12__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE13__DOT__accumulator);
    VL_FWRITEF(vlTOPp->systolic_array__DOT__outfile,"%f %f %f %f\n",
               64,vlTOPp->systolic_array__DOT__PE20__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE21__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE22__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE23__DOT__accumulator);
    VL_FWRITEF(vlTOPp->systolic_array__DOT__outfile,"%f %f %f %f\n",
               64,vlTOPp->systolic_array__DOT__PE30__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE31__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE32__DOT__accumulator,
               64,vlTOPp->systolic_array__DOT__PE33__DOT__accumulator);
    VL_FCLOSE_I(vlTOPp->systolic_array__DOT__outfile); vlTOPp->systolic_array__DOT__outfile = 0;
    VL_FINISH_MT("systolic_array.v", 105, "");
}

void Vsystolic_array::_eval_initial(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_eval_initial\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    vlTOPp->__Vclklast__TOP____VinpClk__TOP__systolic_array__DOT__clk 
        = vlTOPp->__VinpClk__TOP__systolic_array__DOT__clk;
    vlTOPp->_initial__TOP__2(vlSymsp);
}

void Vsystolic_array::final() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::final\n"); );
    // Variables
    Vsystolic_array__Syms* __restrict vlSymsp = this->__VlSymsp;
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
}

void Vsystolic_array::_eval_settle(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_eval_settle\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
}

void Vsystolic_array::_ctor_var_reset() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_ctor_var_reset\n"); );
    // Body
    systolic_array__DOT__file = 0;
    systolic_array__DOT__outfile = 0;
    systolic_array__DOT__clk = VL_RAND_RESET_I(1);
    systolic_array__DOT__reset = VL_RAND_RESET_I(1);
    { int __Vi0=0; for (; __Vi0<4; ++__Vi0) {
            { int __Vi1=0; for (; __Vi1<4; ++__Vi1) {
                    systolic_array__DOT__A[__Vi0][__Vi1] = 0;
            }}
    }}
    { int __Vi0=0; for (; __Vi0<4; ++__Vi0) {
            { int __Vi1=0; for (; __Vi1<4; ++__Vi1) {
                    systolic_array__DOT__B[__Vi0][__Vi1] = 0;
            }}
    }}
    systolic_array__DOT__PE00__DOT__accumulator = 0;
    systolic_array__DOT__PE01__DOT__accumulator = 0;
    systolic_array__DOT__PE02__DOT__accumulator = 0;
    systolic_array__DOT__PE03__DOT__accumulator = 0;
    systolic_array__DOT__PE10__DOT__accumulator = 0;
    systolic_array__DOT__PE11__DOT__accumulator = 0;
    systolic_array__DOT__PE12__DOT__accumulator = 0;
    systolic_array__DOT__PE13__DOT__accumulator = 0;
    systolic_array__DOT__PE20__DOT__accumulator = 0;
    systolic_array__DOT__PE21__DOT__accumulator = 0;
    systolic_array__DOT__PE22__DOT__accumulator = 0;
    systolic_array__DOT__PE23__DOT__accumulator = 0;
    systolic_array__DOT__PE30__DOT__accumulator = 0;
    systolic_array__DOT__PE31__DOT__accumulator = 0;
    systolic_array__DOT__PE32__DOT__accumulator = 0;
    systolic_array__DOT__PE33__DOT__accumulator = 0;
    __VinpClk__TOP__systolic_array__DOT__clk = VL_RAND_RESET_I(1);
    __Vchglast__TOP__systolic_array__DOT__clk = VL_RAND_RESET_I(1);
}
