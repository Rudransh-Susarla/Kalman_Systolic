// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vsystolic_array.h for the primary calling header

#include "Vsystolic_array.h"
#include "Vsystolic_array__Syms.h"

//==========

void Vsystolic_array::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate Vsystolic_array::eval\n"); );
    Vsystolic_array__Syms* __restrict vlSymsp = this->__VlSymsp;  // Setup global symbol table
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
#ifdef VL_DEBUG
    // Debug assertions
    _eval_debug_assertions();
#endif  // VL_DEBUG
    // Initialize
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) _eval_initial_loop(vlSymsp);
    // Evaluate till stable
    int __VclockLoop = 0;
    QData __Vchange = 1;
    do {
        VL_DEBUG_IF(VL_DBG_MSGF("+ Clock loop\n"););
        _eval(vlSymsp);
        if (VL_UNLIKELY(++__VclockLoop > 100)) {
            // About to fail, so enable debug to see what's not settling.
            // Note you must run make with OPT=-DVL_DEBUG for debug prints.
            int __Vsaved_debug = Verilated::debug();
            Verilated::debug(1);
            __Vchange = _change_request(vlSymsp);
            Verilated::debug(__Vsaved_debug);
            VL_FATAL_MT("systolic_array.v", 1, "",
                "Verilated model didn't converge\n"
                "- See DIDNOTCONVERGE in the Verilator manual");
        } else {
            __Vchange = _change_request(vlSymsp);
        }
    } while (VL_UNLIKELY(__Vchange));
}

void Vsystolic_array::_eval_initial_loop(Vsystolic_array__Syms* __restrict vlSymsp) {
    vlSymsp->__Vm_didInit = true;
    _eval_initial(vlSymsp);
    // Evaluate till stable
    int __VclockLoop = 0;
    QData __Vchange = 1;
    do {
        _eval_settle(vlSymsp);
        _eval(vlSymsp);
        if (VL_UNLIKELY(++__VclockLoop > 100)) {
            // About to fail, so enable debug to see what's not settling.
            // Note you must run make with OPT=-DVL_DEBUG for debug prints.
            int __Vsaved_debug = Verilated::debug();
            Verilated::debug(1);
            __Vchange = _change_request(vlSymsp);
            Verilated::debug(__Vsaved_debug);
            VL_FATAL_MT("systolic_array.v", 1, "",
                "Verilated model didn't DC converge\n"
                "- See DIDNOTCONVERGE in the Verilator manual");
        } else {
            __Vchange = _change_request(vlSymsp);
        }
    } while (VL_UNLIKELY(__Vchange));
}

VL_INLINE_OPT void Vsystolic_array::_sequent__TOP__1(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_sequent__TOP__1\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    if (vlTOPp->systolic_array__DOT__reset) {
        vlTOPp->systolic_array__DOT__PE33__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE32__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE31__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE30__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE23__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE22__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE21__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE20__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE13__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE12__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE11__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE10__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE03__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE02__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE01__DOT__accumulator = 0.0;
        vlTOPp->systolic_array__DOT__PE00__DOT__accumulator = 0.0;
    } else {
        vlTOPp->systolic_array__DOT__PE33__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE33__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[3U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][3U]));
        vlTOPp->systolic_array__DOT__PE32__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE32__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[3U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][2U]));
        vlTOPp->systolic_array__DOT__PE31__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE31__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[3U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][1U]));
        vlTOPp->systolic_array__DOT__PE30__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE30__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[3U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][0U]));
        vlTOPp->systolic_array__DOT__PE23__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE23__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[2U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][3U]));
        vlTOPp->systolic_array__DOT__PE22__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE22__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[2U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][2U]));
        vlTOPp->systolic_array__DOT__PE21__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE21__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[2U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][1U]));
        vlTOPp->systolic_array__DOT__PE20__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE20__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[2U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][0U]));
        vlTOPp->systolic_array__DOT__PE13__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE13__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[1U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][3U]));
        vlTOPp->systolic_array__DOT__PE12__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE12__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[1U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][2U]));
        vlTOPp->systolic_array__DOT__PE11__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE11__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[1U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][1U]));
        vlTOPp->systolic_array__DOT__PE10__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE10__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[1U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][0U]));
        vlTOPp->systolic_array__DOT__PE03__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE03__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[0U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][3U]));
        vlTOPp->systolic_array__DOT__PE02__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE02__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[0U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][2U]));
        vlTOPp->systolic_array__DOT__PE01__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE01__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[0U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][1U]));
        vlTOPp->systolic_array__DOT__PE00__DOT__accumulator 
            = (vlTOPp->systolic_array__DOT__PE00__DOT__accumulator 
               + (vlTOPp->systolic_array__DOT__A[0U]
                  [0U] * vlTOPp->systolic_array__DOT__B
                  [0U][0U]));
    }
}

void Vsystolic_array::_eval(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_eval\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    if (((IData)(vlTOPp->__VinpClk__TOP__systolic_array__DOT__clk) 
         & (~ (IData)(vlTOPp->__Vclklast__TOP____VinpClk__TOP__systolic_array__DOT__clk)))) {
        vlTOPp->_sequent__TOP__1(vlSymsp);
    }
    // Final
    vlTOPp->__Vclklast__TOP____VinpClk__TOP__systolic_array__DOT__clk 
        = vlTOPp->__VinpClk__TOP__systolic_array__DOT__clk;
    vlTOPp->__VinpClk__TOP__systolic_array__DOT__clk 
        = vlTOPp->systolic_array__DOT__clk;
}

VL_INLINE_OPT QData Vsystolic_array::_change_request(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_change_request\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    return (vlTOPp->_change_request_1(vlSymsp));
}

VL_INLINE_OPT QData Vsystolic_array::_change_request_1(Vsystolic_array__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_change_request_1\n"); );
    Vsystolic_array* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    // Change detection
    QData __req = false;  // Logically a bool
    __req |= ((vlTOPp->systolic_array__DOT__clk ^ vlTOPp->__Vchglast__TOP__systolic_array__DOT__clk));
    VL_DEBUG_IF( if(__req && ((vlTOPp->systolic_array__DOT__clk ^ vlTOPp->__Vchglast__TOP__systolic_array__DOT__clk))) VL_DBG_MSGF("        CHANGE: systolic_array.v:6: systolic_array.clk\n"); );
    // Final
    vlTOPp->__Vchglast__TOP__systolic_array__DOT__clk 
        = vlTOPp->systolic_array__DOT__clk;
    return __req;
}

#ifdef VL_DEBUG
void Vsystolic_array::_eval_debug_assertions() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vsystolic_array::_eval_debug_assertions\n"); );
}
#endif  // VL_DEBUG
