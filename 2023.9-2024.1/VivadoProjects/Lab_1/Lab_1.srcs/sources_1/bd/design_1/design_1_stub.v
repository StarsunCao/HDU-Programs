// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2019.1 (win64) Build 2552052 Fri May 24 14:49:42 MDT 2019
// Date        : Wed Oct 11 20:44:29 2023
// Host        : DESKTOP-HILJCAC running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub {C:/Users/kotoriee/Documents/Tencent
//               Files/1124911924/FileRecv/Lab1/Lab1/Lab_1/Lab_1.srcs/sources_1/bd/design_1/design_1_stub.v}
// Design      : design_1
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
module design_1(clk_100MHz, gpio_rtl_0_tri_o, 
  gpio_rtl_1_tri_i, reset_rtl_0)
/* synthesis syn_black_box black_box_pad_pin="clk_100MHz,gpio_rtl_0_tri_o[15:0],gpio_rtl_1_tri_i[15:0],reset_rtl_0" */;
  input clk_100MHz;
  output [15:0]gpio_rtl_0_tri_o;
  input [15:0]gpio_rtl_1_tri_i;
  input reset_rtl_0;
endmodule
