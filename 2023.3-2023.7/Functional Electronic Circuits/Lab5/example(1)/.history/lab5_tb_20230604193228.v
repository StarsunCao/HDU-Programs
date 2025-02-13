`timescale 1ns/1ps
module lab5_tb;


reg clk, rst;
wire [31:0] HRDATA;
wire [31:0] HADDR;
wire [31:0] HWDATA;
wire HWRITE;

parameter BASE_ADDR = 0;
parameter CLK_DIV   = 10;

wire sclk, mosi, cs;
wire miso;

master muut(
    .HCLK_i(clk),
    .HRESETn_i(rst),
    .HRDATA_bi(HRDATA),
    .HADDR_bo(HADDR),
    .HWDATA_bo(HWDATA),
    .HWRITE_o(HWRITE)
);

slave #(.BASE_ADDR(0), .CLK_DIV(5)) 
suut(
    .HCLK_i(clk),
    .HRESETn_i(rst),
    .HRDATA_bo(HRDATA),
    .HADDR_bi(HADDR),
    .HWDATA_bi(HWDATA),
    .HWRITE_i(HWRITE),
    
    .sclk_o(sclk),
    .mosi_o(mosi),
    .miso_i(miso),
    .cs_o(cs)
);

periph_dev pdev (    
    .sclk_i(sclk),
    .mosi_i(mosi),
    .miso_o(miso),
    .cs_i(cs)
);

always #5 clk = ~clk;


initial begin
    $dumpfile("time.vcd");
    $dumpvars(0, lab5_tb);
    clk = 0;
    rst = 0;

    #100
    rst = 1;
end 

endmodule
