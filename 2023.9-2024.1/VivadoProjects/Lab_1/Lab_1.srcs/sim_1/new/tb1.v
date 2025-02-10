`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/10/11 03:43:36
// Design Name: 
// Module Name: tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////



module tb;
reg clk_100MHz;
wire [15:0]gpio_rtl_0_tri_o;
wire [15:0]gpio_rtl_1_tri_i;
reg reset_rtl_0;

wire data_ack = gpio_rtl_0_tri_o[14];

sequencer seq(
    .clk(clk_100MHz),
    .rst(reset_rtl_0),
    .ack(data_ack),
    .data(gpio_rtl_1_tri_i)
    );
    
monitor mon(
    .clk(clk_100MHz),
    .rst(reset_rtl_0),
    .data_in(gpio_rtl_1_tri_i),
    .data_out(gpio_rtl_0_tri_o)
    );   

design_1_wrapper uut
   (.clk_100MHz(clk_100MHz),
    .gpio_rtl_0_tri_o(gpio_rtl_0_tri_o),
    .gpio_rtl_1_tri_i(gpio_rtl_1_tri_i),
    .reset_rtl_0(reset_rtl_0)
    );
    
always #5 clk_100MHz = ~clk_100MHz;
    
initial begin
    clk_100MHz = 0;
    reset_rtl_0 = 1;
    #100
    reset_rtl_0 = 0;
end
endmodule
