package com.second.hand.trading.server.service;

import com.second.hand.trading.server.model.OperationModel;

public interface OperationService {

    /**
     * 新增接口
     * @param operationModel
     * @return
     */
    boolean createOperation(OperationModel operationModel);
}
