`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/10/19 17:21:36
// Design Name: 
// Module Name: sequencer
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



module sequencer(
    input clk,
    input rst,
    input ack,
    output [15:0] data
    );
    
    reg strb;
    reg [7:0] data_in;
    
    assign data = {strb, 7'b0, data_in};
    
    localparam OUTPUT_VALUE = 0;
    localparam WAIT_ACK = 1;
    
    reg state;
    
    class randomValues;
        rand int data_in;
        constraint c{
            data_in dist{
                [0:60] := 1,
                [100:255] := 6
            };
        };
        
    endclass
    
    randomValues r;
    
    initial begin
        r = new();
        strb = 0;
        state = OUTPUT_VALUE;
    end
    
    always@(posedge clk)
        if(rst == 0) begin
            case(state)
                OUTPUT_VALUE:begin
                    r.randomize();
                    data_in = r.data_in;
                    strb = 1;
                    state = WAIT_ACK;
                end
                WAIT_ACK:begin
                    if(ack) begin
                        strb = 0;
                        state = OUTPUT_VALUE;
                    end
                end
            endcase
        end
endmodule

