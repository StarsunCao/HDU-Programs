module bus(
    input [31:0] HADDR_MASTER_bi,
    input [31:0] HWDATA_MASTER_bi,
    input HWRITE_MASTER_i,
    output reg [31:0] HRDATA_MASTER_bo,

    output [31:0] HADDR_SLAVE_1_bo,
    output [31:0] HWDATA_SLAVE_1_bo,
    output reg HWRITE_SLAVE_1_o,
    input [31:0] HRDATA_SLAVE_1_bi,
    output [31:0] HADDR_SLAVE_2_bo,
    output [31:0] HWDATA_SLAVE_2_bo,
    output reg HWRITE_SLAVE_2_o,
    input [31:0] HRDATA_SLAVE_2_bi
);
assign HADDR_SLAVE_1_bo = HADDR_MASTER_bi;
assign HADDR_SLAVE_2_bo = HADDR_MASTER_bi;
assign HWDATA_SLAVE_1_bo = HWDATA_MASTER_bi;
assign HWDATA_SLAVE_2_bo = HWDATA_MASTER_bi;
always@*
    if (HADDR_MASTER_bi < 32'h80) begin
        HWRITE_SLAVE_1_o <= HWRITE_MASTER_i;
        HRDATA_MASTER_bo <= HRDATA_SLAVE_1_bi;
    end else begin
        HWRITE_SLAVE_2_o <= HWRITE_MASTER_i;
        HRDATA_MASTER_bo <= HRDATA_SLAVE_2_bi;
    end
endmodule
