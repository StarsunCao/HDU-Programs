-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2019.1 (win64) Build 2552052 Fri May 24 14:49:42 MDT 2019
-- Date        : Wed Oct 11 20:44:29 2023
-- Host        : DESKTOP-HILJCAC running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub {C:/Users/kotoriee/Documents/Tencent
--               Files/1124911924/FileRecv/Lab1/Lab1/Lab_1/Lab_1.srcs/sources_1/bd/design_1/design_1_stub.vhdl}
-- Design      : design_1
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity design_1 is
  Port ( 
    clk_100MHz : in STD_LOGIC;
    gpio_rtl_0_tri_o : out STD_LOGIC_VECTOR ( 15 downto 0 );
    gpio_rtl_1_tri_i : in STD_LOGIC_VECTOR ( 15 downto 0 );
    reset_rtl_0 : in STD_LOGIC
  );

end design_1;

architecture stub of design_1 is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "clk_100MHz,gpio_rtl_0_tri_o[15:0],gpio_rtl_1_tri_i[15:0],reset_rtl_0";
begin
end;
