module adder (
    input [31:0] a_bi,
    input [31:0] b_bi,
    
    output [31:0] c_bo
);

assign c_bo = a_bi + b_bi;

endmodule