module lab2_oc(
    input [31:0] x,
    input rst,
    input clk,
    output reg [31:0] y
);

always @(posedge clk) begin
    if (rst)
        y <= 0;
    else
        y <= x*x*x + x*x;
end

endmodule