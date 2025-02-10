module lab2_pipe(
    input [31:0] x,
    input rst,
    input clk,
    input start,
    output reg [31:0] y,
    output reg rdy
);

reg [31:0] pow2, pow3;
reg [31:0] x1, x2;
reg rdy1, rdy2;

always @(posedge clk) begin
    if (rst) begin
        y <= 0;
        rdy <= 1;
        rdy1 <= 0;
        rdy2 <= 0;
        pow2 <= 0;
        pow3 <= 0;
        x1 <= 0;
        x2 <= 0;

    end else begin
        if (start) begin
            rdy <= 0;
            rdy1 <= 1;
        end
        
        rdy2 <= rdy1;
        rdy <= rdy2;

        x1 <= x;
        x2 <= x1;

        pow2 <= x*x;
        pow3 <= pow2 * x1; //x*x*x
        y <= pow3 + x2 * x2; // x*x*x + x*x
    end
end
endmodule