module master(
    input HCLK_i,
    input HRESETn_i,
    input [31:0] HRDATA_bi,

    output reg [31:0] HADDR_bo,
    output reg [31:0] HWDATA_bo,
    output reg HWRITE_o

);

localparam STATUS_ADDR = 8'h0;
localparam OP_ADDR     = 8'h1;

task write(
    input [31:0] addr,
    input [31:0] data
);
    begin
        @(posedge HCLK_i);
        HADDR_bo <= addr;
        HWRITE_o <= 1;
        
        @(posedge HCLK_i);
        HWDATA_bo <= data;
        HWRITE_o <= 1;
        @(posedge HCLK_i);
        HWRITE_o <= 0;

    end
endtask

task read(
    input  [31:0] addr,
    output [31:0] data
);
    begin
        @(posedge HCLK_i);
        HADDR_bo <= addr;
        HWRITE_o <= 0;

        @(posedge HCLK_i);
        @(posedge HCLK_i);
        data <= HRDATA_bi;
        @(posedge HCLK_i);
    end


endtask

task wait_ready();

begin

    begin : wait_busy
        while(1) begin
            read(32'h0, data);
            if(data == 1)
                disable wait_busy;
        end
    end
    
    begin : wait_ready
        while(1) begin
            read(32'h0, data);
            if(data == 0)
                disable wait_ready;
        end
    end
end

endtask

reg [31:0] data = 1;

initial begin

    write(32'h1, {8'h0, STATUS_ADDR, 16'h1});
    wait_ready;
    write(32'h1, {8'h0, OP_ADDR, 8'h2, 8'h8});
    wait_ready;
    write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;
    read(32'h2, data);
    $display("READ DATA | data: %h", data);
    
    write(32'h1, {8'h0, OP_ADDR, 8'h2, 8'h4});
    wait_ready;
    write(32'h1, 0);
    wait_ready;
    write(32'h1, 0);
    wait_ready;
    read(32'h2, data);
    $display("READ DATA | data: %h", data);

    $finish;

end

endmodule
