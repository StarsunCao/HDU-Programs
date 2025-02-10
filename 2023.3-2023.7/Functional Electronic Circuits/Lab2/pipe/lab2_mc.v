module lab2_mc(
    input [31:0] x,
    input rst,
    input clk,
    input start,
    output reg [31:0] y,
    output reg rdy
);

reg [31:0] x_buf;
reg [2:0] ctr;

wire [2:0] ctr_next = (rdy)? 0: ctr + 1;
wire [31:0] y_next = (rdy)? 1: y*x_buf;

always @(posedge clk) begin
    if (rst) begin
        y <= 0;
        rdy <= 1;
        x_buf <= 0;
        ctr <= 0;
    end
    else begin
        ctr <= ctr_next;

        if (start) begin
            y <= 1;
            rdy <= 0;
            x_buf <= x;
        end

        if (!rdy)
            if (ctr == 2) begin
                y <= y_next + x_buf * x_buf;
                rdy <= 1;
            end else
                y <= y_next;
    end
    
end
endmodule
