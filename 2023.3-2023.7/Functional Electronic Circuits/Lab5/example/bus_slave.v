module bus_slave(
    input HCLK_i,
    input HRESETn_i,
    output reg [31:0] HRDATA_bo,

    input [31:0] HADDR_bi,
    input [31:0] HWDATA_bi,
    input HWRITE_i,

    input  [31:0] data_rx_bi,
    input  data_rx_wr_i,
    input  busy_i,
    output reg [31:0] data_tx_bo,
    output reg data_tx_wr_o
);

parameter BASE_ADDR        = 0;

localparam STATUS_REG_ADDR = BASE_ADDR + 0;
localparam DATA_TX_ADDR    = BASE_ADDR + 1;
localparam DATA_RX_ADDR    = BASE_ADDR + 2;

reg [7:0]  status_r;
reg [31:0] data_rx_r;

always@(posedge HCLK_i)
    if(HRESETn_i == 0) begin
        HRDATA_bo     <= 0;
        data_tx_bo    <= 0;
        data_tx_wr_o  <= 0;    
    end else begin
        data_tx_wr_o <= 0;

        if(HWRITE_i)
            case(HADDR_bi)
                DATA_TX_ADDR:
                    begin
                        data_tx_bo   <= HWDATA_bi;
                        data_tx_wr_o <= 1;
                    end
            endcase
        else begin
            case(HADDR_bi)
                STATUS_REG_ADDR:
                    HRDATA_bo <= {24'h0, status_r};
                DATA_TX_ADDR:
                    HRDATA_bo <= data_tx_bo;
                DATA_RX_ADDR:
                    HRDATA_bo <= data_rx_r;
                default:
                    HRDATA_bo <= 0;
            endcase
        end
    end

always@(posedge HCLK_i)
    if(HRESETn_i == 0) begin
        status_r  <= 0;
        data_rx_r <= 0;
    end else begin
        status_r <= {7'h0, busy_i};
        
        if(data_rx_wr_i)
            data_rx_r <= data_rx_bi;
    end


endmodule
