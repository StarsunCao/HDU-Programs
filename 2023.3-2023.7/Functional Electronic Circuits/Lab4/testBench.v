`timescale 1ns/1ps

module lab4_tb;
reg clk, rst;
wire [31:0] HRDATA, HADDR, HWDATA;
wire HWRITE;
wire [31:0] HRDATA_SLAVE_1, HADDR_SLAVE_1, HWDATA_SLAVE_1;
wire HWRITE_SLAVE_1;
wire [31:0] HRDATA_SLAVE_2, HADDR_SLAVE_2, HWDATA_SLAVE_2;
wire HWRITE_SLAVE_2;
bus buut (
    .HADDR_MASTER_bi(HADDR),
    .HWDATA_MASTER_bi(HWDATA),
    .HRDATA_MASTER_bo(HRDATA),
    .HWRITE_MASTER_i(HWRITE),
    .HADDR_SLAVE_1_bo(HADDR_SLAVE_1),
    .HWDATA_SLAVE_1_bo(HWDATA_SLAVE_1),
    .HRDATA_SLAVE_1_bi(HRDATA_SLAVE_1),
    .HWRITE_SLAVE_1_o(HWRITE_SLAVE_1),
    .HADDR_SLAVE_2_bo(HADDR_SLAVE_2),
    .HWDATA_SLAVE_2_bo(HWDATA_SLAVE_2),
    .HRDATA_SLAVE_2_bi(HRDATA_SLAVE_2),
    .HWRITE_SLAVE_2_o(HWRITE_SLAVE_2)
);
master muut(
    .HCLK_i(clk),
    .HRESETn_i(rst),
    .HRDATA_bi(HRDATA),
    .HADDR_bo(HADDR),
    .HWDATA_bo(HWDATA),
    .HWRITE_o(HWRITE)
);
slave suut1(
    .HCLK_i(clk),
    .HRESETn_i(rst),
    .HRDATA_bo(HRDATA_SLAVE_1),
    .HADDR_bi(HADDR_SLAVE_1),
    .HWDATA_bi(HWDATA_SLAVE_1),
    .HWRITE_i(HWRITE_SLAVE_1)
);
slave suut2(
    .HCLK_i(clk),
    .HRESETn_i(rst),
    .HRDATA_bo(HRDATA_SLAVE_2),
    .HADDR_bi(HADDR_SLAVE_2),
    .HWDATA_bi(HWDATA_SLAVE_2),
    .HWRITE_i(HWRITE_SLAVE_2)
);
always #5 clk = ~clk;
initial begin
    $dumpfile("time.vcd");
    $dumpvars(1, lab4_tb);
    clk = 0;
    rst = 0;
    #20 
    rst = 1;
    
end
endmodule
